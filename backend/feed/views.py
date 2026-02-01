
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.db import IntegrityError
from django.utils.timezone import now, timedelta
from django.db.models import Sum, Case, When, IntegerField, F

from .models import Post, Comment, Like
from .serializers import PostSerializer

class FeedView(APIView):

    def get(self, request):
        posts = Post.objects.prefetch_related('comments__likes', 'likes')
        return Response(PostSerializer(posts, many=True).data)

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request):
        post_id = request.data.get("id")
        post = get_object_or_404(Post, id=post_id)
        post.delete()
        return Response({"deleted": True})

class LikePostView(APIView):
    def post(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        try:
            Like.objects.create(user=request.user, post=post)
        except IntegrityError:
            pass
        return Response({"status": "ok"})

class LikeCommentView(APIView):
    def post(self, request, comment_id):
        comment = get_object_or_404(Comment, id=comment_id)
        try:
            Like.objects.create(user=request.user, comment=comment)
        except IntegrityError:
            pass
        return Response({"status": "ok"})

class LeaderboardView(APIView):
    def get(self, request):
        since = now() - timedelta(hours=24)
        likes = Like.objects.filter(created_at__gte=since)

        leaderboard = likes.annotate(
            karma=Case(
                When(post__isnull=False, then=5),
                When(comment__isnull=False, then=1),
                output_field=IntegerField()
            ),
            owner=Case(
                When(post__isnull=False, then=F('post__author')),
                When(comment__isnull=False, then=F('comment__author')),
            )
        ).values('owner').annotate(
            total_karma=Sum('karma')
        ).order_by('-total_karma')[:5]

        return Response(leaderboard)

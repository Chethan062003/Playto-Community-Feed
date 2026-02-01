from rest_framework import serializers
from .models import Post, Comment


class CommentSerializer(serializers.ModelSerializer):
    replies = serializers.SerializerMethodField()
    like_count = serializers.IntegerField(source='likes.count', read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'content', 'like_count', 'replies']

    def get_replies(self, obj):
        children = self.context['comment_map'].get(obj.id, [])
        return CommentSerializer(children, many=True, context=self.context).data


class PostSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField()
    like_count = serializers.IntegerField(source='likes.count', read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'content', 'like_count', 'comments']

    # 🔥 THIS FIX IS IMPORTANT FOR POST
    def create(self, validated_data):
        return Post.objects.create(
            content=validated_data['content'],
            author=None
        )

    def get_comments(self, obj):
        all_comments = obj.comments.all()

        comment_map = {}
        roots = []

        for c in all_comments:
            if c.parent_id is None:
                roots.append(c)
            comment_map.setdefault(c.parent_id, []).append(c)

        context = {'comment_map': comment_map}
        return CommentSerializer(roots, many=True, context=context).data

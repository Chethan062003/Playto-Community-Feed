
from django.urls import path
from .views import FeedView, LikePostView, LikeCommentView, LeaderboardView

urlpatterns = [
    path('feed/', FeedView.as_view()),
    path('like/post/<int:post_id>/', LikePostView.as_view()),
    path('like/comment/<int:comment_id>/', LikeCommentView.as_view()),
    path('leaderboard/', LeaderboardView.as_view()),
]

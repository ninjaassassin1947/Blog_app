from django.urls import path ,include
from .views import PostList, PostDetail, PostUpdate, AllPostsView, PostView, CommentList

# Blog-related URLs
blog_patterns = [
    path('posts/', PostList.as_view(), name='post-list'),
    path('posts/<slug:slug>/', PostDetail.as_view(), name='post-detail'),
    path('posts/<slug:slug>/edit/', PostUpdate.as_view(), name='post-update'),
    path('all-posts/', AllPostsView.as_view(), name='all-posts'),
    path('post/<slug:slug>/', PostView.as_view(), name='post-view'),
]

# Comment-related URLs
comment_patterns = [
    path('comments/', CommentList.as_view(), name='comment-list'),
]

# Main URL patterns
urlpatterns = [
    path('', include((blog_patterns, 'blog'), namespace='blog')),
    path('', include((comment_patterns, 'comments'), namespace='comments')),
]

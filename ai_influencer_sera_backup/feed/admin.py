from django.contrib import admin
from .models import FeedPost, FeedComment, FeedLike

@admin.register(FeedPost)
class FeedPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'get_likes_count', 'comment_count']
    list_filter = ['created_at']
    search_fields = ['title', 'content']

@admin.register(FeedComment)
class FeedCommentAdmin(admin.ModelAdmin):
    list_display = ['post', 'author', 'content', 'created_at']
    list_filter = ['created_at']

@admin.register(FeedLike)
class FeedLikeAdmin(admin.ModelAdmin):
    list_display = ['post', 'user', 'created_at']
    list_filter = ['created_at']

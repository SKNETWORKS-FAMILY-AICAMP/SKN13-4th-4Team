from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

class FeedPost(models.Model):
    """피드 포스트 모델"""
    title = models.CharField(max_length=200, verbose_name='제목')
    content = models.TextField(verbose_name='내용')
    image = models.CharField(max_length=100, verbose_name='이미지 파일명')  # 정적 이미지 파일명
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='작성일')
    likes_count = models.PositiveIntegerField(default=0, verbose_name='좋아요 수')

    class Meta:
        verbose_name = '피드 포스트'
        verbose_name_plural = '피드 포스트들'
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def content_preview(self):
        """내용 미리보기"""
        return self.content[:100] + '...' if len(self.content) > 100 else self.content
    content_preview.short_description = '내용 미리보기'

    def comment_count(self):
        """댓글 수"""
        return self.comments.count()
    comment_count.short_description = '댓글 수'


class FeedComment(models.Model):
    """피드 댓글 모델"""
    post = models.ForeignKey(FeedPost, on_delete=models.CASCADE, related_name='comments', verbose_name='포스트')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='작성자')
    content = models.TextField(verbose_name='댓글 내용')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='작성일')

    class Meta:
        verbose_name = '피드 댓글'
        verbose_name_plural = '피드 댓글들'
        ordering = ['created_at']

    def __str__(self):
        return f"{self.author.username}: {self.content[:50]}"

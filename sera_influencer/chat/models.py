from django.db import models
from django.conf import settings

class ChatHistory(models.Model):
    """채팅 대화 기록 모델"""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='사용자')
    user_message = models.TextField(verbose_name='사용자 메시지')
    assistant_message = models.TextField(verbose_name='AI 응답')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='생성일')

    class Meta:
        verbose_name = '채팅 기록'
        verbose_name_plural = '채팅 기록들'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user.username}: {self.user_message[:50]}"


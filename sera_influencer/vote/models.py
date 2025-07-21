from django.db import models
from django.conf import settings

class VoteOption(models.Model):
    """
    투표 선택지 모델
    """
    CONTENT_CHOICES = [
        ('pilates', '🧘‍♀️ 필라테스 기초 동작'),
        ('rehabilitation', '🏥 재활 운동 루틴'),
        ('stretching', '🤸‍♀️ 스트레칭 가이드'),
        ('nutrition', '🥗 운동 영양학'),
    ]
    
    content_type = models.CharField(max_length=20, choices=CONTENT_CHOICES, unique=True, verbose_name='컨텐츠 타입')
    title = models.CharField(max_length=100, verbose_name='제목')
    vote_count = models.PositiveIntegerField(default=0, verbose_name='투표 수')

    class Meta:
        verbose_name = '투표 선택지'
        verbose_name_plural = '투표 선택지들'
        ordering = ['-vote_count']

    def __str__(self):
        return self.title

class Vote(models.Model):
    """
    사용자 투표 기록 모델
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='사용자')
    option = models.ForeignKey(VoteOption, on_delete=models.CASCADE, verbose_name='선택한 옵션')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='투표일자')

    class Meta:
        verbose_name = '투표'
        verbose_name_plural = '투표들'
        unique_together = ('user',)  # 한 사용자당 하나의 투표만 허용
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user.username} -> {self.option.title}"

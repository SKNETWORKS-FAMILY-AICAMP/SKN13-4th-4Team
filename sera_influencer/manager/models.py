from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # 필요하면 사용자 정보 필드 추가
    # nickname = models.CharField(max_length=30, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    last_name = None
    

    def __str__(self):
        return self.username

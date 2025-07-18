#!/usr/bin/env python3
"""
테스트용 사용자 생성 스크립트
Django 환경이 설정된 후 실행하세요.

사용법:
python3 manage.py shell < create_test_user.py
또는
python3 create_test_user.py (Django 환경 설정 후)
"""

import os
import django

# Django 설정
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth.models import User

def create_test_user():
    """테스트용 사용자 생성"""
    username = 'testuser'
    password = 'testpass123'
    email = 'test@example.com'
    
    # 이미 존재하는 사용자인지 확인
    if User.objects.filter(username=username).exists():
        print(f"사용자 '{username}'가 이미 존재합니다.")
        return
    
    # 새 사용자 생성
    user = User.objects.create_user(
        username=username,
        password=password,
        email=email
    )
    
    print(f"테스트 사용자가 생성되었습니다:")
    print(f"아이디: {username}")
    print(f"비밀번호: {password}")
    print(f"이메일: {email}")

if __name__ == '__main__':
    create_test_user()

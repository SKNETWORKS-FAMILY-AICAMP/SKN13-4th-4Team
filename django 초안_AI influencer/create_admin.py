#!/usr/bin/env python3
"""
관리자 계정 생성 스크립트
Django 환경이 설정된 후 실행하세요.

사용법:
python3 create_admin.py
"""

import os
import django

# Django 설정
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth.models import User

def create_admin_user():
    """관리자 계정 생성"""
    username = 'admin'
    email = 'admin@sera.com'
    password = 'admin123'
    
    # 이미 존재하는 관리자인지 확인
    if User.objects.filter(username=username).exists():
        print(f"관리자 계정 '{username}'가 이미 존재합니다.")
        admin_user = User.objects.get(username=username)
        print(f"기존 관리자 정보:")
        print(f"- 아이디: {admin_user.username}")
        print(f"- 이메일: {admin_user.email}")
        print(f"- 슈퍼유저: {admin_user.is_superuser}")
        return admin_user
    
    # 새 관리자 계정 생성
    admin_user = User.objects.create_superuser(
        username=username,
        email=email,
        password=password,
        first_name='관리자',
        last_name='SERA'
    )
    
    print(f"✅ 관리자 계정이 생성되었습니다:")
    print(f"- 아이디: {username}")
    print(f"- 비밀번호: {password}")
    print(f"- 이메일: {email}")
    print(f"\n🌐 관리자 페이지 접속:")
    print(f"- URL: http://localhost:8000/admin/")
    print(f"- 위 계정 정보로 로그인하세요.")
    
    return admin_user

def create_test_users():
    """테스트 사용자들 생성"""
    test_users = [
        {'username': 'user1', 'email': 'user1@test.com', 'first_name': '김철수'},
        {'username': 'user2', 'email': 'user2@test.com', 'first_name': '이영희'},
        {'username': 'user3', 'email': 'user3@test.com', 'first_name': '박민수'},
    ]
    
    created_users = []
    for user_data in test_users:
        username = user_data['username']
        if not User.objects.filter(username=username).exists():
            user = User.objects.create_user(
                username=username,
                email=user_data['email'],
                password='test123',
                first_name=user_data['first_name']
            )
            created_users.append(user)
            print(f"테스트 사용자 생성: {username}")
        else:
            print(f"테스트 사용자 '{username}'가 이미 존재합니다.")
    
    return created_users

if __name__ == '__main__':
    print("🚀 SERA 관리자 설정을 시작합니다...\n")
    
    # 관리자 계정 생성
    admin_user = create_admin_user()
    
    print("\n" + "="*50)
    
    # 테스트 사용자들 생성
    print("\n📝 테스트 사용자들을 생성합니다...")
    test_users = create_test_users()
    
    print("\n" + "="*50)
    print("\n✨ 설정 완료!")
    print("\n📋 다음 단계:")
    print("1. python3 manage.py runserver 실행")
    print("2. http://localhost:8000/admin/ 접속")
    print("3. admin / admin123 으로 로그인")
    print("4. 피드 포스트, 댓글, 사용자 프로필 등을 확인하세요!")
    
    if test_users:
        print(f"\n👥 테스트 사용자 계정 (비밀번호: test123):")
        for user in test_users:
            print(f"- {user.username} ({user.first_name})")

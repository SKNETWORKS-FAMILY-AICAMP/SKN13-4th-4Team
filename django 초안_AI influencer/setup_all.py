#!/usr/bin/env python3
"""
전체 SERA 시스템 설정 스크립트
Django 환경이 설정된 후 실행하세요.

사용법:
python3 setup_all.py
"""

import os
import django

# Django 설정
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth.models import User
from core.models import FeedPost, FeedComment, UserProfile

def setup_admin():
    """관리자 계정 설정"""
    print("👑 관리자 계정 설정 중...")
    
    username = 'admin'
    email = 'admin@sera.com'
    password = 'admin123'
    
    if User.objects.filter(username=username).exists():
        print(f"✅ 관리자 계정 '{username}'가 이미 존재합니다.")
        return User.objects.get(username=username)
    
    admin_user = User.objects.create_superuser(
        username=username,
        email=email,
        password=password,
        first_name='관리자',
        last_name='SERA'
    )
    
    print(f"✅ 관리자 계정 생성 완료: {username}")
    return admin_user

def setup_test_users():
    """테스트 사용자들 설정"""
    print("\n👥 테스트 사용자들 설정 중...")
    
    test_users_data = [
        {'username': 'sera_fan1', 'email': 'fan1@test.com', 'first_name': '김철수', 'last_name': ''},
        {'username': 'pilates_lover', 'email': 'pilates@test.com', 'first_name': '이영희', 'last_name': ''},
        {'username': 'fitness_guru', 'email': 'fitness@test.com', 'first_name': '박민수', 'last_name': ''},
    ]
    
    created_users = []
    for user_data in test_users_data:
        username = user_data['username']
        if not User.objects.filter(username=username).exists():
            user = User.objects.create_user(
                username=username,
                email=user_data['email'],
                password='test123',
                first_name=user_data['first_name'],
                last_name=user_data['last_name']
            )
            created_users.append(user)
            print(f"✅ 테스트 사용자 생성: {username}")
        else:
            created_users.append(User.objects.get(username=username))
            print(f"✅ 테스트 사용자 '{username}' 이미 존재")
    
    return created_users

def setup_feed_posts():
    """피드 포스트들 설정"""
    print("\n📝 피드 포스트들 설정 중...")
    
    if FeedPost.objects.exists():
        print("✅ 피드 포스트들이 이미 존재합니다.")
        return FeedPost.objects.all()
    
    sample_posts = [
        {
            'title': '오늘의 필라테스 루틴 💪',
            'content': '''아침 일찍 일어나서 30분 필라테스 루틴을 완료했어요! 코어 운동 위주로 진행했는데 정말 시원하네요 😊 

여러분도 함께 해보세요!

#필라테스 #모닝루틴 #건강한하루 #SERA''',
            'image': 'AI_influencere_img_4.png',
            'likes_count': 42
        },
        {
            'title': '새로운 운동복 추천 ✨',
            'content': '''요즘 즐겨 입는 운동복이에요! 신축성도 좋고 땀 흡수도 빨라서 운동할 때 정말 편해요 💕 

색상도 예쁘죠?

운동복 선택할 때는 기능성이 가장 중요한 것 같아요. 이 제품은 정말 만족스러워요!

#운동복추천 #필라테스웨어 #협찬''',
            'image': 'AI_influencere_img_7.png',
            'likes_count': 67
        },
        {
            'title': '홈트레이닝 필수템 🏠',
            'content': '''집에서 운동할 때 꼭 필요한 아이템들을 소개해드릴게요!

1. 요가매트 - 기본 중의 기본
2. 저항밴드 - 다양한 운동 가능  
3. 폼롤러 - 마사지와 스트레칭

이 세 가지만 있어도 집에서 충분히 좋은 운동을 할 수 있어요! 💪

#홈트레이닝 #운동용품 #필라테스''',
            'image': 'AI_influencere_img_11.png',
            'likes_count': 89
        }
    ]
    
    created_posts = []
    for post_data in sample_posts:
        post = FeedPost.objects.create(**post_data)
        created_posts.append(post)
        print(f"✅ 포스트 생성: {post.title}")
    
    return created_posts

def setup_comments(posts, users):
    """댓글들 설정"""
    print("\n💬 댓글들 설정 중...")
    
    if FeedComment.objects.exists():
        print("✅ 댓글들이 이미 존재합니다.")
        return
    
    sample_comments = [
        [
            "정말 좋은 루틴이네요! 저도 따라해볼게요 😊",
            "매일 하면 효과가 있을까요?",
            "아침 운동 정말 좋아요! 💪"
        ],
        [
            "운동복 정보 감사해요!",
            "어디서 구매할 수 있나요?",
            "색상이 정말 예뻐요 💕",
            "저도 같은 브랜드 써봤는데 정말 좋더라구요!"
        ],
        [
            "홈트레이닝 아이템 추천 너무 유용해요 👍",
            "폼롤러 정말 필요한가요?",
            "요가매트는 어떤 브랜드가 좋을까요?",
            "집에서 운동하기 딱 좋은 아이템들이네요!"
        ]
    ]
    
    comment_count = 0
    for i, post in enumerate(posts):
        if i < len(sample_comments):
            for j, comment_text in enumerate(sample_comments[i]):
                if j < len(users):
                    FeedComment.objects.create(
                        post=post,
                        author=users[j % len(users)],
                        content=comment_text
                    )
                    comment_count += 1
    
    print(f"✅ {comment_count}개의 댓글 생성 완료")

def main():
    """메인 설정 함수"""
    print("🚀 SERA AI 인플루언서 시스템 전체 설정을 시작합니다...\n")
    print("="*60)
    
    # 1. 관리자 계정 설정
    admin_user = setup_admin()
    
    # 2. 테스트 사용자들 설정
    test_users = setup_test_users()
    
    # 3. 피드 포스트들 설정
    posts = setup_feed_posts()
    
    # 4. 댓글들 설정
    setup_comments(posts, test_users)
    
    print("\n" + "="*60)
    print("✨ 전체 설정이 완료되었습니다!")
    
    print(f"\n📊 생성된 데이터:")
    print(f"- 관리자 계정: 1개")
    print(f"- 테스트 사용자: {len(test_users)}개")
    print(f"- 피드 포스트: {FeedPost.objects.count()}개")
    print(f"- 댓글: {FeedComment.objects.count()}개")
    print(f"- 사용자 프로필: {UserProfile.objects.count()}개")
    
    print(f"\n🌐 접속 정보:")
    print(f"- 웹사이트: http://localhost:8000/")
    print(f"- 관리자 페이지: http://localhost:8000/admin/")
    print(f"- 관리자 계정: admin / admin123")
    print(f"- 테스트 계정들: 비밀번호 test123")
    
    print(f"\n📋 다음 단계:")
    print(f"1. python3 manage.py runserver")
    print(f"2. 브라우저에서 위 URL들 접속")
    print(f"3. 관리자 페이지에서 데이터 확인")
    print(f"4. 웹사이트에서 기능 테스트")

if __name__ == '__main__':
    main()

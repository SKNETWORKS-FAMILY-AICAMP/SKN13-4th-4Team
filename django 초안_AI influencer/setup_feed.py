#!/usr/bin/env python3
"""
피드 기능 설정 스크립트
Django 환경이 설정된 후 실행하세요.

사용법:
python3 setup_feed.py
"""

import os
import django

# Django 설정
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from core.models import FeedPost, FeedComment
from django.contrib.auth.models import User

def setup_feed_data():
    """샘플 피드 데이터 생성"""
    
    # 기존 데이터 확인
    if FeedPost.objects.exists():
        print("피드 데이터가 이미 존재합니다.")
        return
    
    # 샘플 포스트 데이터
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
    
    # 포스트 생성
    created_posts = []
    for post_data in sample_posts:
        post = FeedPost.objects.create(**post_data)
        created_posts.append(post)
        print(f"포스트 생성됨: {post.title}")
    
    # 샘플 댓글 생성 (사용자 계정이 있는 경우)
    try:
        users = User.objects.all()[:3]  # 최대 3명의 사용자
        if users:
            sample_comments = [
                ["정말 좋은 루틴이네요! 저도 따라해볼게요 😊", "매일 하면 효과가 있을까요?"],
                ["운동복 정보 감사해요!", "어디서 구매할 수 있나요?", "색상이 정말 예뻐요 💕"],
                ["홈트레이닝 아이템 추천 너무 유용해요 👍", "폼롤러 정말 필요한가요?"]
            ]

            for i, post in enumerate(created_posts):
                if i < len(sample_comments):
                    # 각 포스트에 여러 댓글 추가
                    for j, comment_text in enumerate(sample_comments[i]):
                        if j < len(users):
                            FeedComment.objects.create(
                                post=post,
                                author=users[j],
                                content=comment_text
                            )
                            print(f"댓글 생성됨: {users[j].username}이 {post.title}에 댓글 추가")
    except Exception as e:
        print(f"댓글 생성 중 오류: {e}")
    
    print(f"\n✅ 피드 설정 완료!")
    print(f"- 생성된 포스트: {len(created_posts)}개")
    print(f"- 이제 /feed/ 페이지에서 인스타그램 스타일 피드를 확인할 수 있습니다!")

if __name__ == '__main__':
    setup_feed_data()

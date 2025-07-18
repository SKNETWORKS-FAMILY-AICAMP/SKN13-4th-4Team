import os
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from feed.models import FeedPost, FeedComment


def feed(request):
    """인스타그램 스타일 피드 페이지"""
    # 피드 포스트들을 가져오기 (없으면 샘플 데이터 생성)
    posts = FeedPost.objects.all()

    # 샘플 데이터가 없으면 생성
    if not posts.exists():
        sample_posts = [
            {
                'title': '오늘의 필라테스 루틴 💪',
                'content': '아침 일찍 일어나서 30분 필라테스 루틴을 완료했어요! 코어 운동 위주로 진행했는데 정말 시원하네요 😊 여러분도 함께 해보세요!\n\n#필라테스 #모닝루틴 #건강한하루 #SERA',
                'image': 'AI_influencere_img_4.png'
            },
            {
                'title': '새로운 운동복 추천 ✨',
                'content': '요즘 즐겨 입는 운동복이에요! 신축성도 좋고 땀 흡수도 빨라서 운동할 때 정말 편해요 💕 색상도 예쁘죠?\n\n운동복 선택할 때는 기능성이 가장 중요한 것 같아요. 이 제품은 정말 만족스러워요!\n\n#운동복추천 #필라테스웨어 #협찬',
                'image': 'AI_influencere_img_7.png'
            },
            {
                'title': '홈트레이닝 필수템 🏠',
                'content': '집에서 운동할 때 꼭 필요한 아이템들을 소개해드릴게요!\n\n1. 요가매트 - 기본 중의 기본\n2. 저항밴드 - 다양한 운동 가능\n3. 폼롤러 - 마사지와 스트레칭\n\n이 세 가지만 있어도 집에서 충분히 좋은 운동을 할 수 있어요! 💪\n\n#홈트레이닝 #운동용품 #필라테스',
                'image': 'AI_influencere_img_11.png'
            }
        ]

        for post_data in sample_posts:
            FeedPost.objects.create(**post_data)

        posts = FeedPost.objects.all()
    return render(request, 'feed.html', {'posts': posts})


def feed_view(request):
    """피드 뷰"""
    return feed(request)
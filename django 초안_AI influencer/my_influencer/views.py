# core/views.py

from django.shortcuts import render

def home(request):
    links = [
        {"name": "재활 질문하기", "url": "/chat/", "bg": "#ff7eb9"},
        {"name": "운동 피드 보기", "url": "/feed/", "bg": "#ff0ea1"},
        {"name": "추천 운동 아이템", "url": "/products/", "bg": "#cc678d"},
        {"name": "다음 컨텐츠 투표", "url": "https://example.com/vote", "bg": "#c71585"},
    ]
    context = {
        "name": "AI 필라테스 강사 세라",
        "bio": "재활&운동 전문가 | 하루 5분으로 건강한 삶을 만들어요 💕",
        "profile_image": "images/profile_img.png",
        "links": links,
    }
    return render(request, "home.html", context)

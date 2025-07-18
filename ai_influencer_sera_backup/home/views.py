from django.shortcuts import render


def home_view(request):
    """홈페이지 뷰"""
    context = {
        **PROFILE_INFO,
        "links": NAVIGATION_LINKS,
        "social_links": SOCIAL_LINKS
    }
    return render(request, "home.html", context)


# 링크 
NAVIGATION_LINKS = [
    {"name": "재활운동 질문하기", "url": "/chat/", "bg": "#FF69B4"},
    {"name": "운동 피드 보기", "url": "/feed/", "bg": "#FF1493"},
    {"name": "추천 운동 아이템", "url": "#", "bg": "#DB7093", "onclick": "showComingSoon()"},
    {"name": "다음 컨텐츠 투표", "url": "/vote/", "bg": "#C71585", "login_required": True},
]

# 소셜 링크 
SOCIAL_LINKS = {
    'instagram': 'https://instagram.com/',
    'tiktok': 'https://tiktok.com/',
    'x': 'https://x.com/',
    'email': 'mailto:sera@example.com',
    'youtube': 'https://youtube.com/'
}

PROFILE_INFO = {
    "profile_image": 'static/images/profile_img.png',
    "name": "AI 필라테스 강사 세라",
    "bio": "재활&운동 전문가 | 하루 5분으로 건강한 삶을 만들어요 💕",
}

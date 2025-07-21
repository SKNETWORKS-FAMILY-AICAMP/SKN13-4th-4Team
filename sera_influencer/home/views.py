from django.shortcuts import render


def home(request):
    """
    홈페이지 뷰 - 처음 로딩되는 페이지

    - 로그인, 회원가입, 로그아웃 버튼
    - 네비게이션 바
    - 프로필 정보
    - 소셜 링크
    - 네비게이션 링크
    를 볼 수 있습니다. 
    
    로그인 상태에 따라 네비게이션 링크의 기능이 달라집니다.
    - 로그인하지 않은 경우, "다음 컨텐츠 투표" 링크를 클릭하면 로그인 페이지로 이동합니다.

    """
    context = {
        **PROFILE_INFO,
        "links": NAVIGATION_LINKS,
        "social_links": SOCIAL_LINKS
    }
    return render(request, "home.html", context)


# 링크 
NAVIGATION_LINKS = [
    {"name": "재활운동 질문하기", "url": "/chat/", "bg": "#FF69B4", "login_required": True},
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

# core/views.py

from django.shortcuts import render

def home(request):
    links = [
        {"name": "재활운동 질문하기", "url": "/chat/", "bg": "#ff7eb9"},
        {"name": "운동 피드 보기", "url": "/feed/", "bg": "#ff0ea1"},
        {"name": "추천 운동 아이템", "url": "/products/", "bg": "#cc678d"},
        {"name": "다음 컨텐츠 투표", "url": "https://example.com/vote", "bg": "#c71585"},
    ]
    # 소셜 아이콘 링크 목록
    social_links = {
        'instagram': 'https://instagram.com/sera_influencer',
        'tiktok': 'https://tiktok.com/@sera',
        'x': 'https://x.com/sera',
        'email': 'mailto:sera@example.com',
        'youtube': 'https://youtube.com/@sera_channel'
    }

    # 템플릿에 전달할 전체 context
    context = {
        "profile_image": "",  # 추후 AI 이미지 URL로 교체
        "name": "AI 필라테스 강사 세라",
        "bio": "재활&운동 전문가 | 하루 5분으로 건강한 삶을 만들어요 💕",
        "links": links,
        "social_links": social_links
    }

    return render(request, "home.html", context)

from django.views.decorators.csrf import csrf_exempt
import random  # 예시 응답용

# 실제로는 LLM 연동할 수도 있음 (예: OpenAI API 등)

def chat_view(request):
    response = None

    if request.method == 'POST':
        user_input = request.POST.get('user_input')

        # 여기에 AI 응답 생성 로직을 추가하면 됩니다.
        # 현재는 예시용으로 랜덤 응답을 설정합니다.
        sample_responses = [
            "어깨 통증이 있으시군요. 어깨 회전근 스트레칭을 추천드려요!",
            "거북목 증상이 의심돼요. 자세 교정 루틴을 같이 해볼까요?",
            "좋은 질문이에요! 정확한 진단을 위해 스트레칭을 함께 해봐요.",
            "통증 부위에 따라 5분짜리 루틴을 준비해드릴게요. 😄",
        ]

        # 실제 AI 응답으로 대체 가능
        response = random.choice(sample_responses)

    return render(request, 'chat.html', {'response': response})



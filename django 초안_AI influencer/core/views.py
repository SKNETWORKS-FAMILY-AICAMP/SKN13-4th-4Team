# core/views.py
import os
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

from django.shortcuts import render

def home(request):
    links = [
        {"name": "재활/운동 질문하기", "url": "/chat/", "bg": "#FF69B4"},
        {"name": "운동 피드 보기", "url": "/feed/", "bg": "#FF1493"},
        {"name": "추천 운동 아이템", "url": "/products/", "bg": "#DB7093"},
        {"name": "다음 컨텐츠 투표", "url": " ", "bg": "#C71585"},
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



def profile_view(request):
    return render(request, 'profile.html')

comments = []

def feed(request):
    global comments
    if request.method == 'POST':
        comment = request.POST.get('comment')
        if comment:
            comments.insert(0, comment)  # 최신 댓글이 위로
    return render(request, 'feed.html', {'comments': comments})

# core/views.py

# def chat(request):
#     response = None
#     if request.method == 'POST':
#         user_input = request.POST.get('user_input')
#         # TODO: LLM 또는 RAG 응답 처리
#         response = f"'{user_input}'에 대해 더 자세히 알려드릴게요!"
#     return render(request, 'chat.html', {'response': response})


from dotenv import load_dotenv
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def chat(request):
    response = None
    if request.method == 'POST':
        user_input = request.POST.get('user_input')

        completion = client.chat.completions.create(model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_input}])
        response = completion.choices[0].message.content
    return render(request, 'chat.html', {'response': response})



def products(request):
    return render(request, "products.html")


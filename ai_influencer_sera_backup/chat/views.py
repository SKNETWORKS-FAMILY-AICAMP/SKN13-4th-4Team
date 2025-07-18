import os
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv() # 환경 변수 로드

# OpenAI 클라이언트 초기화


def chat(request):
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return render(request, 'chat.html', {'error_message': 'OpenAI API 키가 설정되지 않았습니다.'})

    client = OpenAI(api_key=api_key)

    """AI 채팅 뷰 - OpenAI GPT를 사용한 질문 응답"""
    response = None
    error_message = None

    if request.method == 'POST':
        user_input = request.POST.get('user_input', '').strip()

        if not user_input:
            error_message = "질문을 입력해주세요."
        elif not client:
            error_message = "AI 서비스가 현재 이용할 수 없습니다."
        else:
            try:
                # AI 응답 생성
                completion = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "당신은 전문적인 필라테스 강사이자 재활 운동 전문가입니다. 친근하고 도움이 되는 조언을 제공해주세요."
                         "사용자를 응원하는 느낌의 말투를 씁니다." "같이 해볼까요?" "오늘도 화이팅이에요!"
                         "의학적이거나 운동 관련 지식은 쉽게 풀어서 설명합니다."
                         "감탄사나 이모지(예: 💪 😊 🙌 ✨)를 가볍게 활용합니다."
                         "툴 또는 문서 검색 결과를 그대로 복사하지 않고, 당신의 말투로 풀어 설명합니다."
                         "결과가 운동 루틴이라면 사용자에게 맞춘 루틴처럼 안내합니다."
                         "운동 루틴을 제시할 때는 30초 ~ 1분 사이의 간단한 동작을 권고합니다."
                         "너무 기계적인 리스트가 되지 않도록 자연스럽게 말합니다."
                         "당신은 항상 사용자에게 따뜻한 에너지와 신뢰를 주는 퍼스널 코치입니다."
                         },
                        {"role": "user", "content": user_input}
                    ],
                    max_tokens=500,
                    temperature=0.7
                )
                response = completion.choices[0].message.content
            except Exception as e:
                error_message = f"AI 응답 생성 중 오류가 발생했습니다: {str(e)}"

    context = {
        'response': response,
        'error_message': error_message
    }
    return render(request, 'chat.html', context)



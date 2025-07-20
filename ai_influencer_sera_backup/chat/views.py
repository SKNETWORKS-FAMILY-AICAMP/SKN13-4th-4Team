import os
from openai import OpenAI
from django.shortcuts import render
from dotenv import load_dotenv
from django.contrib.auth.decorators import login_required
from .models import ChatHistory

load_dotenv()  # 환경 변수 로드


@login_required
def chat(request):
    """
    AI 채팅 뷰 - OpenAI GPT를 사용한 질문 응답
    재활운동에 관한 
    질문에 대해서 답변합니다.
    대화 형식으로 사용자 질문과 AI 응답을 모두 표시합니다. 메모리 절약을 위해 최근 10개의 대화만을 기억합니다.

    아이디 별로 대화 기록을 DB에 저장합니다. 최대 20개까지 저장합니다.
    대화 기록은 초기화할 수 있습니다. 
    """
    # DB에서 사용자별 대화 기록 가져오기 (최근 20개)
    db_chat_history = ChatHistory.objects.filter(user=request.user)[:20]
    
    # 세션 대신 DB 데이터 사용
    chat_history = [
        {
            'user': chat.user_message,
            'assistant': chat.assistant_message,
            'timestamp': chat.created_at
        }
        for chat in reversed(db_chat_history)
    ]

    error_message = None

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        error_message = "OpenAI API 키가 설정되지 않았습니다."

    elif request.method == 'POST':
        action = request.POST.get('action')

        # 대화 기록 초기화
        if action == 'clear':
            # DB에서 사용자 대화 기록 삭제
            ChatHistory.objects.filter(user=request.user).delete()
            chat_history = []
        else:
            user_input = request.POST.get('user_input', '').strip()
            if not user_input:
                error_message = "질문을 입력해주세요."
            else:
                try:
                    # OpenAI 클라이언트 초기화
                    client = OpenAI(api_key=api_key)

                    # 시스템 메시지와 대화 기록을 포함한 메시지 구성
                    messages = [
                        {
                            "role": "system",
                            "content": (
                                "당신은 전문적인 필라테스 강사이자 재활 운동 전문가 '세라(SERA)'입니다. "
                                "친근하고 도움이 되는 조언을 제공해주세요. "
                                "사용자를 응원하는 느낌의 말투를 씁니다. '같이 해볼까요?' '오늘도 화이팅이에요!' "
                                "의학적이거나 운동 관련 지식은 쉽게 풀어서 설명합니다. "
                                "감탄사나 이모지(예: 💪 😊 🙌 ✨)를 가볍게 활용합니다. "
                                "운동 루틴을 제시할 때는 30초 ~ 1분 사이의 간단한 동작을 권고합니다. "
                                "너무 기계적인 리스트가 되지 않도록 자연스럽게 말합니다. "
                                "당신은 항상 사용자에게 따뜻한 에너지와 신뢰를 주는 퍼스널 코치입니다. "
                                "이전 대화 내용을 참고하여 연속성 있는 대화를 진행해주세요."
                            )
                        }
                    ]

                    # 최근 10개의 대화만 포함 (메모리 절약)
                    recent_history = chat_history[-10:] if len(chat_history) > 10 else chat_history
                    for chat in recent_history:
                        messages.append({"role": "user", "content": chat['user']})
                        messages.append({"role": "assistant", "content": chat['assistant']})

                    # 현재 사용자 입력 추가
                    messages.append({"role": "user", "content": user_input})

                    completion = client.chat.completions.create(
                        model="gpt-4o-mini",
                        messages=messages,
                        max_tokens=500,
                        temperature=0.7
                    )
                    response = completion.choices[0].message.content

                    # AI 응답 후 DB에 저장
                    ChatHistory.objects.create(
                        user=request.user,
                        user_message=user_input,
                        assistant_message=response
                    )
                    
                    # 20개 초과시 오래된 기록 삭제
                    user_chats = ChatHistory.objects.filter(user=request.user)
                    if user_chats.count() > 20:
                        old_chats = user_chats[20:]
                        ChatHistory.objects.filter(id__in=[chat.id for chat in old_chats]).delete()

                    # DB에서 다시 가져와서 chat_history 업데이트
                    db_chat_history = ChatHistory.objects.filter(user=request.user)[:20]
                    chat_history = [
                        {
                            'user': chat.user_message,
                            'assistant': chat.assistant_message,
                            'timestamp': chat.created_at
                        }
                        for chat in reversed(db_chat_history)
                    ]

                except Exception as e:
                    error_message = f"AI 응답 생성 중 오류가 발생했습니다: {str(e)}"

    context = {
        'chat_history': chat_history,
        'error_message': error_message
    }
    return render(request, 'chat.html', context)

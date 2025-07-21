import os
from openai import OpenAI
from django.shortcuts import render
from dotenv import load_dotenv
from django.contrib.auth.decorators import login_required
from .models import ChatHistory
from .agent import create_agent

load_dotenv()  # 환경 변수 로드


@login_required
def chat(request):
    """
    AI 채팅 뷰 - LangChain Agent를 사용한 질문 응답
    재활운동에 관한 질문에 대해서 답변합니다.
    대화 형식으로 사용자 질문과 AI 응답을 모두 표시합니다.
    """
    # DB에서 사용자별 대화 기록 가져오기 (최근 20개)
    db_chat_history = ChatHistory.objects.filter(user=request.user)[:20]
    
    chat_history = [
        {
            'user': chat.user_message,
            'assistant': chat.assistant_message,
            'timestamp': chat.created_at
        }
        for chat in reversed(db_chat_history)
    ]

    error_message = None

    if request.method == 'POST':
        action = request.POST.get('action')

        # 대화 기록 초기화
        if action == 'clear':
            ChatHistory.objects.filter(user=request.user).delete()
            chat_history = []
        else:
            user_input = request.POST.get('user_input', '').strip()
            if not user_input:
                error_message = "질문을 입력해주세요."
            else:
                try:
                    print(f"💬 사용자 질문: {user_input}")
                    # 파일에도 로그 기록
                    with open("debug.log", "a", encoding="utf-8") as f:
                        f.write(f"[{request.user}] 질문: {user_input}\n")

                    # LangChain Agent 사용
                    print("🤖 Agent 생성 중...")
                    # agent = create_agent()
                    # print("🤖 Agent 생성 완료!")
                    # print("🤖 Agent 실행 중...")
                    # response = agent.invoke(user_input)
                    # print(f"🤖 Agent 응답: {response}...")
                    agent = create_agent()
                    result = agent.invoke(user_input)
                    response = result.get("output", "AI 응답이 없습니다.")

                    # 슬라이싱 안전하게 처리
                    print(f":robot: Agent 응답: {str(response)[:100]}...")

                    # 파일에도 응답 기록
                    with open("debug.log", "a", encoding="utf-8") as f:
                        f.write(f"[{request.user}] 응답: {response[:200]}...\n\n")

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


try:
    agent = create_agent()
    result = agent.invoke(user_input)
    response = result.get("output", "AI 응답이 없습니다.")

    # 슬라이싱 안전하게 처리
    print(f":robot: Agent 응답: {str(response)[:100]}...")

    # 로그에도 기록
    with open("debug.log", "a", encoding="utf-8") as f:
        f.write(f"[{request.user}] 응답: {str(response)[:200]}...\n\n")

    # DB 저장 등 처리...
except Exception as e:
    error_message = f"AI 응답 생성 중 오류가 발생했습니다: {str(e)}"
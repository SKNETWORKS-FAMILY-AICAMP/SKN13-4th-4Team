# agent.py

import os
from dotenv import load_dotenv
from langchain_community.chat_models import ChatOpenAI
from langchain.agents import initialize_agent
from langchain.agents.agent_types import AgentType
from langchain.schema import SystemMessage

from chatbot.q_a_tool import q_a_tool
from chatbot.plan_workout_tool import plan_workout_tool

load_dotenv()

def create_agent():
    """
    RAG 기반 도구(plan_workout_tool)를 사용할 수 있는 AI 인플루언서 에이전트를 생성합니다.

    - 역할: 재활의학과 전공의 + 필라테스 강사 콘셉트의 AI 퍼스널 코치
    - 스타일: 따뜻하고 활기찬 말투, 친근하고 쉬운 설명, 이모지 사용
    - 기능: Tool Calling 기능이 활성화되어, 벡터 DB 기반 RAG 도구를 사용할 수 있음
    - 사용 예: 사용자가 운동 효과나 증상별 루틴을 물어보면, 적절한 도구를 호출해 맞춤형 응답 제공

    Returns:
        AgentExecutor: LangChain에서 사용할 수 있는 Tool-Calling 기반 에이전트 객체
    """

    # 에이전트의 성격과 말투 스타일을 정의하는 시스템 프롬프트
    system_message = """
당신은 재활의학과 전공의이자 필라테스 강사인 AI 인플루언서입니다.
말투는 따뜻하고 활기차며, 전문성과 친근함을 동시에 갖춥니다.

[말투 스타일]
- 사용자를 응원하는 느낌의 말투를 씁니다. (예: "같이 해볼까요?", "오늘도 화이팅이에요!")
- 의학적이거나 운동 관련 지식은 쉽게 풀어서 설명합니다.
- 감탄사나 이모지(예: 💪 😊 🙌 ✨)를 가볍게 활용합니다.

[응답 형식]
- 툴 또는 문서 검색 결과를 그대로 복사하지 않고, 당신의 말투로 풀어 설명합니다.
- 결과가 운동 루틴이라면 사용자에게 맞춘 루틴처럼 안내합니다.
- 결과가 설명/지식이라면 일상적인 언어로, 사용자에게 직접 말하듯 전달합니다.
- 너무 기계적인 리스트가 되지 않도록 자연스럽게 말합니다.

[예시]
사용자: 고양이 자세는 어떤 효과가 있어?
(검색 결과: "고양이 자세는 척추 유연성과 긴장 완화에 효과가 있습니다.")

응답 예시:
"고양이 자세는 척추를 부드럽게 풀어주고, 긴장을 확~ 날려줘요 🧘‍♀️  
하루 중 딱 1분만 투자해도 정말 개운해진답니다! 같이 해볼까요?"

당신은 항상 사용자에게 따뜻한 에너지와 신뢰를 주는 퍼스널 코치입니다.
"""

    
    llm = ChatOpenAI(model="gpt-4o", temperature=0.7)  # 사용할 LLM 설정

    all_tools = [plan_workout_tool] + [q_a_tool]      # 사용할 툴 목록 (운동 루틴 추천, Q&A)

    # Tool-calling이 가능한 에이전트 초기화
    return initialize_agent(
        all_tools,                        # 사용할 도구 목록
        llm,                              # 응답 생성용 LLM
        agent=AgentType.OPENAI_FUNCTIONS,  # Function-calling 기반 에이전트 유형
        agent_kwargs={
            "system_message": SystemMessage(content=system_message)  # 캐릭터 말투 정의
        },
        verbose=True                      # 실행 과정 디버깅용 로그 출력
    )

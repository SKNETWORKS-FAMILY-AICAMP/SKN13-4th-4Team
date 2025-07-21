from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain.tools.retriever import create_retriever_tool

def get_plan_workout_tool():
    """운동 계획 도구를 생성하는 함수"""
    # RAG 세팅
    vectordb = Chroma(                                              # 저장된 Chroma 벡터 DB 불러오기
        persist_directory="./vector_db",                            # 벡터 DB 경로
        collection_name="rehabilitation_articles_openai",
        embedding_function=OpenAIEmbeddings(model="text-embedding-3-large")  # 동일한 임베딩 모델로 설정
    )

    retriever = vectordb.as_retriever(search_kwargs={"k": 3})       # 관련 문서 최대 3개 검색하는 retriever 생성

    # Tool 생성
    return create_retriever_tool(                      # Tool-calling 에이전트가 사용할 검색용 툴 생성
        retriever,                                                  # 위에서 만든 retriever를 사용
        name="plan_workout_tool",                                   # 툴 이름 (Agent 내부 식별자)
        description="사용자의 증상 또는 회복 목표에 따라 운동 루틴을 문서 기반으로 추천합니다."  # 툴 기능 설명
    )

# 호환성을 위해 변수로도 제공 (실제 사용 시에만 초기화됨)
plan_workout_tool = None

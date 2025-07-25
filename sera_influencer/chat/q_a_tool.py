from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain.tools.retriever import create_retriever_tool

def get_q_a_tool():
    """Q&A 도구를 생성하는 함수"""
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
        name="q_a_tool",                                   # 툴 이름 (Agent 내부 식별자)
        description = "사용자의 의학 관련 궁금증에 대해, 재활의학 논문을 바탕으로 이해하기 쉽게 설명하는 도구입니다."   # 툴 기능 설명
    )

# 호환성을 위해 변수로도 제공 (실제 사용 시에만 초기화됨)
q_a_tool = None


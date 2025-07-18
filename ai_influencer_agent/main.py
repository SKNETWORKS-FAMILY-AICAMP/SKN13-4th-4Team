# main.py

from agent import create_agent

if __name__ == "__main__":
    agent = create_agent()
    while True:
        user_input = input("\n🧘‍♀️ 사용자 질문: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        response = agent.run(user_input)
        print("\n🤖 AI 인플루언서:\n", response)

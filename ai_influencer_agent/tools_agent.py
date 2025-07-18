# tools.py

from langchain.agents import Tool

# ===== Tool Functions =====

def plan_recovery_workout(info: str):
    if "피곤" in info and "회복" in info:
        return "\n".join([
            "✔ Cat-Cow Stretch 10회",
            "✔ Deep Breathing 2분",
            "✔ Side Lying Stretch 30초 x 2"
        ])
    elif "무릎" in info:
        return "\n".join([
            "✔ Clamshell 10회",
            "✔ 힙 브릿지 15회",
            "✔ 종아리 스트레칭 20초"
        ])
    return "오늘은 가벼운 워킹 10분부터 시작해보자!"


def build_mind_body_schedule(days_per_week, minutes_per_day):
    return "\n".join([
        f"Day {i+1}: {minutes_per_day}분 동안 필라테스 + 5분 스트레칭 + 2분 복식호흡"
        for i in range(days_per_week)
    ])

def recommend_pose_tutorial(target_area):
    tutorials = {
        "허리": "✔ 숄더 브릿지: 허리 근육 강화와 안정성 향상에 좋아요!",
        "어깨": "✔ 와이 자세 스트레칭: 거북목 개선에도 효과적이에요!",
        "무릎": "✔ 힙 브릿지: 무릎 부담 줄이고 엉덩이 근육 활성화!"
    }
    return tutorials.get(target_area, "✔ Cat-Cow로 부드럽게 시작해봐요!")

def generate_instagram_caption(pose):
    captions = {
        "힙 브릿지": "🔥힙업 루틴의 핵심! 힙 브릿지로 하루 한 걸음 더 💪✨",
        "플랭크": "🙌 전신 근육 자극엔 플랭크! 자세 잡고, 나만의 시간 갖기 💫",
        "고양이자세": "🧘‍♀️ 마음도 허리도 풀어주는 힐링 동작, 오늘도 고양이처럼~"
    }
    return captions.get(pose, f"오늘의 {pose} 동작, 나랑 같이 해볼래요? 💖")

def generate_edu_card(topic):
    cards = {
        "테니스엘보": {
            "증상": "팔꿈치 바깥쪽 통증",
            "원인": "손목 과사용",
            "운동": "손목 굽힘/펴기 스트레칭 추천"
        },
        "거북목": {
            "증상": "목 통증, 어깨 결림",
            "원인": "고개 전방자세",
            "운동": "턱 당기기, 어깨 열기 스트레칭"
        }
    }
    card = cards.get(topic, {"증상": "정보 없음", "운동": "담당 전문가에게 상담하세요!"})
    return "\n".join([f"{k}: {v}" for k, v in card.items()])

def start_7day_challenge(focus_area):
    routine = {
        "힙업": ["힙 브릿지", "클램셸", "던키 킥"],
        "체형교정": ["숄더 브릿지", "플랭크", "고양이자세"]
    }
    selected = routine.get(focus_area, ["스트레칭", "복식호흡", "걷기"])
    return "\n".join([f"Day {i+1}: {selected[i % len(selected)]} 10회" for i in range(7)])

def explain_pose_with_emotion(pose: str) -> str:
    explanations = {
        "숄더 브릿지": "이 동작은 허리 보호에 정말 좋아요! 아침에 하면 하루가 개운~✨",
        "플랭크": "코어 근육이 불타는 느낌! 힘들지만 끝나고 나면 몸이 꽉 잡힌 느낌이에요 💪",
        "고양이자세": "척추가 쭉 펴지는 느낌, 긴장이 싹 풀리면서 마음까지 편안해져요 🧘‍♀️",
        "클램셸": "엉덩이가 타오르지만~ 라인을 살리는 데는 최고예요! 🔥",
        "던키 킥": "힘찬 킥 한 방! 탄력 있는 힙을 만들 수 있어요 🍑"
    }
    return explanations.get(pose, f"{pose}은(는) 몸에 좋은 동작이에요! 나랑 같이 해볼까요? 😊")

# ===== Tool 리스트 정의 =====

tools = [
Tool.from_function(func=plan_recovery_workout, name="plan_recovery_workout", description="사용자의 증상이나 목적을 문자열로 입력받아 회복 운동 루틴을 추천합니다."),
    Tool.from_function(func=build_mind_body_schedule, name="build_mind_body_schedule", description="운동 루틴 + 스트레칭 + 호흡 루틴을 주간 계획으로 짜줍니다."),
    Tool.from_function(func=recommend_pose_tutorial, name="recommend_pose_tutorial", description="통증 부위나 운동 목적에 맞춘 필라테스 동작 튜토리얼을 추천합니다."),
    Tool.from_function(func=generate_instagram_caption, name="generate_instagram_caption", description="필라테스 동작에 어울리는 인스타그램 문구를 생성합니다."),
    Tool.from_function(func=generate_edu_card, name="generate_edu_card", description="재활 의학 용어 또는 개념에 대한 짧은 카드 정보를 제공합니다."),
    Tool.from_function(func=start_7day_challenge, name="start_7day_challenge", description="힙업, 체형교정 등 주제에 맞는 7일 운동 챌린지를 추천합니다."),
    Tool.from_function(func=explain_pose_with_emotion, name="explain_pose_with_emotion", description="포즈에 대해 감정이 담긴 설명을 친근한 말투로 제공합니다.")
    
]


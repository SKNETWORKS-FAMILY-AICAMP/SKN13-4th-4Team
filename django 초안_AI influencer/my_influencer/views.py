import os
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from openai import OpenAI
from dotenv import load_dotenv
from core.models import FeedPost, FeedComment

# 환경 변수 로드
load_dotenv()

# OpenAI 클라이언트 초기화
try:
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
except Exception as e:
    client = None
    print(f"OpenAI 클라이언트 초기화 실패: {e}")


def chat(request):
    """AI 채팅 뷰 - OpenAI GPT를 사용한 질문 응답"""
    response = None
    error_message = None

    agent = create_agent()

    if request.method == 'POST':
        user_input = request.POST.get('user_input', '').strip()

        if not user_input:
            error_message = "질문을 입력해주세요."
        elif not client:
            error_message = "AI 서비스가 현재 이용할 수 없습니다."
        elif user_input.lower() in ["exit", "quit"]:
            response = "세션을 종료합니다. 다음에 또 이용해주세요!"  
        else:
            try:
                response = agent.run(user_input)
            except Exception as e:
                error_message = f"AI 응답 생성 중 오류가 발생했습니다: {str(e)}"

    context = {
        'response': response,
        'error_message': error_message
    }
    return render(request, 'chat.html', context)


def feed(request):
    """인스타그램 스타일 피드 페이지"""
    # 피드 포스트들을 가져오기 (없으면 샘플 데이터 생성)
    posts = FeedPost.objects.all()

    # 샘플 데이터가 없으면 생성
    if not posts.exists():
        sample_posts = [
            {
                'title': '오늘의 필라테스 루틴 💪',
                'content': '아침 일찍 일어나서 30분 필라테스 루틴을 완료했어요! 코어 운동 위주로 진행했는데 정말 시원하네요 😊 여러분도 함께 해보세요!\n\n#필라테스 #모닝루틴 #건강한하루 #SERA',
                'image': 'AI_influencere_img_4.png'
            },
            {
                'title': '새로운 운동복 추천 ✨',
                'content': '요즘 즐겨 입는 운동복이에요! 신축성도 좋고 땀 흡수도 빨라서 운동할 때 정말 편해요 💕 색상도 예쁘죠?\n\n운동복 선택할 때는 기능성이 가장 중요한 것 같아요. 이 제품은 정말 만족스러워요!\n\n#운동복추천 #필라테스웨어 #협찬',
                'image': 'AI_influencere_img_7.png'
            },
            {
                'title': '홈트레이닝 필수템 🏠',
                'content': '집에서 운동할 때 꼭 필요한 아이템들을 소개해드릴게요!\n\n1. 요가매트 - 기본 중의 기본\n2. 저항밴드 - 다양한 운동 가능\n3. 폼롤러 - 마사지와 스트레칭\n\n이 세 가지만 있어도 집에서 충분히 좋은 운동을 할 수 있어요! 💪\n\n#홈트레이닝 #운동용품 #필라테스',
                'image': 'AI_influencere_img_11.png'
            }
        ]

        for post_data in sample_posts:
            FeedPost.objects.create(**post_data)

        posts = FeedPost.objects.all()

    # 댓글 추가 처리
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        comment_content = request.POST.get('comment', '').strip()

        if post_id and comment_content:
            if request.user.is_authenticated:
                post = get_object_or_404(FeedPost, id=post_id)
                FeedComment.objects.create(
                    post=post,
                    author=request.user,
                    content=comment_content
                )
                messages.success(request, '댓글이 등록되었습니다.')
            else:
                messages.error(request, '댓글을 작성하려면 로그인이 필요합니다.')

        return redirect('feed')

    context = {'posts': posts}
    return render(request, 'feed.html', context)


def products(request):
    """상품 페이지 뷰"""
    return render(request, "products.html")


@login_required
@require_POST
def delete_comment(request, comment_id):
    """댓글 삭제 뷰"""
    comment = get_object_or_404(FeedComment, id=comment_id)

    # 작성자만 삭제 가능
    if comment.author != request.user:
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({'success': False, 'error': '권한이 없습니다.'})
        else:
            messages.error(request, '자신의 댓글만 삭제할 수 있습니다.')
            return redirect('feed')

    # 댓글 삭제
    post_id = comment.post.id
    comment.delete()

    # AJAX 요청인 경우 JSON 응답
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({'success': True, 'message': '댓글이 삭제되었습니다.'})

    # 일반 요청인 경우 리다이렉트
    messages.success(request, '댓글이 삭제되었습니다.')
    return redirect('feed')

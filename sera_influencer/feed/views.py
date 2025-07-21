import os
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from feed.models import FeedPost, FeedComment, FeedLike


def feed(request):
    """
    인스타그램 스타일 피드 페이지
    사진이 들어가고, 좋아요 버튼, 댓글 기능이 있습니다.
    로그인한 사용자만 댓글을 달 수 있습니다.
    로그인한 사용자는 자신이 단 댓글을 삭제할 수 있습니다. 
    
    댓글은 DB에 저장됩니다. 
    """
    # 댓글 추가 처리
    if request.method == 'POST' and request.user.is_authenticated:
        post_id = request.POST.get('post_id')
        comment_content = request.POST.get('comment', '').strip()

        if post_id and comment_content:
            try:
                post = FeedPost.objects.get(id=post_id)
                FeedComment.objects.create(
                    post=post,
                    author=request.user,
                    content=comment_content
                )
                messages.success(request, '댓글이 추가되었습니다.')
            except FeedPost.DoesNotExist:
                messages.error(request, '포스트를 찾을 수 없습니다.')

        return redirect('feed')

    # 피드 포스트들을 가져오기 (없으면 샘플 데이터 생성)
    posts = FeedPost.objects.all()

    # 각 포스트에 현재 사용자의 좋아요 상태 추가
    for post in posts:
        post.user_liked = post.is_liked_by_user(request.user)

    print(f"DEBUG: Found {posts.count()} posts in database")

    # 샘플 데이터가 없으면 생성
    if not posts.exists():
        print("DEBUG: No posts found, creating sample data...")
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
            post = FeedPost.objects.create(**post_data)
            print(f"DEBUG: Created post: {post.title}")

        posts = FeedPost.objects.all()
        # 새로 생성된 포스트들에도 좋아요 상태 추가
        for post in posts:
            post.user_liked = post.is_liked_by_user(request.user)
        print(f"DEBUG: After creation, found {posts.count()} posts")

    print(f"DEBUG: Rendering template with {posts.count()} posts")
    return render(request, 'feed.html', {'posts': posts})


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
    comment.delete()

    # AJAX 요청인 경우 JSON 응답
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({'success': True, 'message': '댓글이 삭제되었습니다.'})

    # 일반 요청인 경우 리다이렉트
    messages.success(request, '댓글이 삭제되었습니다.')
    return redirect('feed')


@login_required
@require_POST
def toggle_like(request, post_id):
    """좋아요 토글 기능"""
    try:
        post = get_object_or_404(FeedPost, id=post_id)
        like, created = FeedLike.objects.get_or_create(
            post=post,
            user=request.user
        )

        if not created:
            # 이미 좋아요가 있으면 삭제
            like.delete()
            liked = False
        else:
            # 새로 좋아요 추가
            liked = True

        # 실제 좋아요 수 계산
        likes_count = post.get_likes_count()

        return JsonResponse({
            'success': True,
            'liked': liked,
            'likes_count': likes_count
        })

    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        })

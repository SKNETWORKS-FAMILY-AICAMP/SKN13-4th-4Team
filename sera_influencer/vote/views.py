from django.db.models import F
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import VoteOption, Vote

@login_required
def vote(request):
    if request.method == 'POST':
        content_type = request.POST.get('content_type')
        
        if content_type:
            try:
                # 선택한 옵션 가져오기 (없으면 생성)
                option, created = VoteOption.objects.get_or_create(
                    content_type=content_type,
                    defaults={
                        'title': dict(VoteOption.CONTENT_CHOICES).get(content_type, content_type)
                    }
                )
                
                # 기존 투표 확인 (모든 선택지에 대해)
                existing_vote = Vote.objects.filter(user=request.user).first()
                
                if existing_vote:
                    # 기존 투표가 있으면 중복 투표 방지
                    messages.error(request, '중복 투표는 불가합니다.')
                    return redirect('vote')
                else:
                    # 새로운 투표 생성
                    Vote.objects.create(user=request.user, option=option)
                    
                    # 투표 수 증가
                    option.vote_count = F('vote_count') + 1
                    option.save(update_fields=['vote_count'])
                    
                    messages.success(request, '투표가 완료되었습니다! 감사합니다 💕')
                    
                    # 투표 결과 데이터 준비
                    options = VoteOption.objects.all().order_by('-vote_count')
                    total_voters = Vote.objects.values('user').distinct().count()
                    
                    context = {
                        'options': options,
                        'total_votes': total_voters,
                    }
                    return render(request, 'vote_result.html', context)
                    
            except Exception as e:
                messages.error(request, f'투표 처리 중 오류가 발생했습니다: {str(e)}')
        else:
            messages.error(request, '선택지를 선택해주세요.')
    
    return render(request, 'vote.html')

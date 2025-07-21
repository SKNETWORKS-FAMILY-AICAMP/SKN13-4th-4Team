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
                
                # 중복 투표 방지 및 투표 생성
                vote, vote_created = Vote.objects.get_or_create(
                    user=request.user, 
                    option=option
                )
                
                if not vote_created:
                    messages.warning(request, '이미 해당 항목에 투표하셨습니다!')
                else:
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

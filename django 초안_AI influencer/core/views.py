from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import JsonResponse
from django.db import IntegrityError
from .models import UserProfile

# 홈페이지 관련 상수
NAVIGATION_LINKS = [
    {"name": "재활/운동 질문하기", "url": "/chat/", "bg": "#FF69B4"},
    {"name": "운동 피드 보기", "url": "/feed/", "bg": "#FF1493"},
    {"name": "추천 운동 아이템", "url": "/products/", "bg": "#DB7093"},
    {"name": "다음 컨텐츠 투표", "url": "/vote/", "bg": "#C71585", "login_required": True},
]

SOCIAL_LINKS = {
    'instagram': 'https://instagram.com/',
    'tiktok': 'https://tiktok.com/',
    'x': 'https://x.com/',
    'email': 'mailto:sera@example.com',
    'youtube': 'https://youtube.com/'
}

PROFILE_INFO = {
    "profile_image": "",  # 추후 AI 이미지 URL로 교체
    "name": "AI 필라테스 강사 세라",
    "bio": "재활&운동 전문가 | 하루 5분으로 건강한 삶을 만들어요 💕",
}


def home(request):
    """홈페이지 뷰"""
    context = {
        **PROFILE_INFO,
        "links": NAVIGATION_LINKS,
        "social_links": SOCIAL_LINKS
    }
    return render(request, "home.html", context)



@login_required
def profile_view(request):
    """회원정보 페이지 뷰"""
    user = request.user

    if request.method == 'POST':
        # 회원정보 수정 처리
        first_name = request.POST.get('first_name', '').strip()
        email = request.POST.get('email', '').strip()
        address = request.POST.get('address', '').strip()
        current_password = request.POST.get('current_password', '').strip()
        new_password = request.POST.get('new_password', '').strip()
        new_password_confirm = request.POST.get('new_password_confirm', '').strip()

        # 필수 필드 검사
        if not first_name or not email:
            messages.error(request, '이름과 이메일은 필수 항목입니다.')
            return render(request, 'profile.html', {'user': user, 'profile': getattr(user, 'profile', None)})

        # 비밀번호 변경 요청이 있는 경우
        if current_password or new_password or new_password_confirm:
            if not all([current_password, new_password, new_password_confirm]):
                messages.error(request, '비밀번호 변경을 위해서는 모든 비밀번호 필드를 입력해주세요.')
                return render(request, 'profile.html', {'user': user, 'profile': getattr(user, 'profile', None)})

            if not user.check_password(current_password):
                messages.error(request, '현재 비밀번호가 올바르지 않습니다.')
                return render(request, 'profile.html', {'user': user, 'profile': getattr(user, 'profile', None)})

            if new_password != new_password_confirm:
                messages.error(request, '새 비밀번호가 일치하지 않습니다.')
                return render(request, 'profile.html', {'user': user, 'profile': getattr(user, 'profile', None)})

            if len(new_password) < 6:
                messages.error(request, '새 비밀번호는 6자 이상이어야 합니다.')
                return render(request, 'profile.html', {'user': user, 'profile': getattr(user, 'profile', None)})

            # 비밀번호 변경
            user.set_password(new_password)

        # 기본 사용자 정보 업데이트
        user.first_name = first_name
        user.email = email
        user.save()

        # 프로필 정보 업데이트
        if hasattr(user, 'profile'):
            user.profile.address = address
            if request.FILES.get('profile_image'):
                user.profile.profile_image = request.FILES['profile_image']
            user.profile.save()

        # 비밀번호가 변경된 경우 다시 로그인 필요
        if current_password and new_password:
            messages.success(request, '회원정보와 비밀번호가 성공적으로 수정되었습니다. 다시 로그인해주세요.')
            logout(request)
            return redirect('login')
        else:
            messages.success(request, '회원정보가 성공적으로 수정되었습니다.')
            return redirect('profile')

    context = {
        'user': user,
        'profile': getattr(user, 'profile', None)
    }
    return render(request, 'profile.html', context)


def login_view(request):
    """로그인 뷰"""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, '로그인되었습니다.')
            # 로그인 후 이전 페이지로 리다이렉트 또는 홈으로
            next_url = request.GET.get('next', '/')
            return redirect(next_url)
        else:
            messages.error(request, '아이디 또는 비밀번호가 올바르지 않습니다.')

    return render(request, 'auth/login.html')


def logout_view(request):
    """로그아웃 뷰"""
    logout(request)
    messages.success(request, '로그아웃되었습니다.')
    return redirect('/')


def signup_view(request):
    """회원가입 뷰"""
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()
        password_confirm = request.POST.get('password_confirm', '').strip()
        first_name = request.POST.get('first_name', '').strip()
        email = request.POST.get('email', '').strip()
        address = request.POST.get('address', '').strip()

        # 유효성 검사
        if not all([username, password, password_confirm, first_name, email]):
            messages.error(request, '필수 항목을 모두 입력해주세요.')
            return render(request, 'auth/signup.html')

        if password != password_confirm:
            messages.error(request, '비밀번호가 일치하지 않습니다.')
            return render(request, 'auth/signup.html')

        if len(password) < 6:
            messages.error(request, '비밀번호는 6자 이상이어야 합니다.')
            return render(request, 'auth/signup.html')

        try:
            # 사용자 생성
            user = User.objects.create_user(
                username=username,
                password=password,
                email=email,
                first_name=first_name
            )

            # 프로필 정보 업데이트 (프로필은 시그널로 자동 생성됨)
            if hasattr(user, 'profile'):
                user.profile.address = address
                if request.FILES.get('profile_image'):
                    user.profile.profile_image = request.FILES['profile_image']
                user.profile.save()

            messages.success(request, '회원가입이 완료되었습니다. 로그인해주세요.')
            return redirect('login')

        except IntegrityError:
            messages.error(request, '이미 존재하는 아이디입니다.')
            return render(request, 'auth/signup.html')
        except Exception as e:
            messages.error(request, f'회원가입 중 오류가 발생했습니다: {str(e)}')
            return render(request, 'auth/signup.html')

    return render(request, 'auth/signup.html')


@login_required
def vote_view(request):
    """다음 컨텐츠 투표 뷰 - 로그인 필요"""
    return render(request, 'vote.html')


def check_login_status(request):
    """로그인 상태 확인 API"""
    return JsonResponse({
        'is_authenticated': request.user.is_authenticated,
        'username': request.user.username if request.user.is_authenticated else None
    })


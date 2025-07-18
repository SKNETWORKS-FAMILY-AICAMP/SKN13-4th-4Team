# 회원가입 기능 구현 완료

## 🎯 구현된 기능

### 1. 회원가입 페이지 (`/signup/`)
- **필수 항목**: 아이디, 비밀번호, 비밀번호 확인, 이름, 이메일
- **선택 항목**: 주소, 프로필 이미지

### 2. 폼 유효성 검사
- **클라이언트 사이드**: JavaScript로 실시간 검사
- **서버 사이드**: Django에서 최종 검사
- **비밀번호**: 6자 이상, 확인 일치 검사
- **이메일**: 형식 검사
- **파일 업로드**: 5MB 이하 제한

### 3. 데이터베이스 모델
- **User 모델**: Django 기본 사용자 모델
- **UserProfile 모델**: 추가 정보 (주소, 프로필 이미지)
- **자동 연결**: 사용자 생성 시 프로필 자동 생성

## 🚀 사용 방법

### 1. 마이그레이션 실행
```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

### 2. 서버 실행
```bash
python3 manage.py runserver
```

### 3. 테스트
1. `http://localhost:8000/login/` 접속
2. "회원가입" 링크 클릭
3. 회원가입 폼 작성
4. 가입 완료 후 로그인 페이지로 리다이렉트

## 📁 파일 구조

```
core/
├── models.py          # UserProfile 모델
├── views.py           # signup_view 추가
└── ...

my_influencer/templates/auth/
├── login.html         # 회원가입 링크 추가
└── signup.html        # 새로 생성된 회원가입 페이지

config/
├── urls.py           # /signup/ URL 추가
└── settings.py       # MEDIA 설정 추가
```

## 🎨 디자인 특징

- **일관된 디자인**: 로그인 페이지와 동일한 스타일
- **반응형**: 모바일에서도 최적화
- **실시간 피드백**: 입력 시 즉시 유효성 검사
- **애니메이션**: 부드러운 페이드인 효과

## 🔧 추가 기능 (향후 확장 가능)

- 이메일 인증
- 소셜 로그인 (구글, 카카오 등)
- 프로필 이미지 크롭 기능
- 비밀번호 강도 표시
- 아이디 중복 검사 AJAX

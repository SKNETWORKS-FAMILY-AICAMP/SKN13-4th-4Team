# SKN13-3rd-3Team

## 1. Introduce Team
### 💡 프로젝트명: AI 인플루언서, 필라테스 강사 SERA(Smart Exercise & Rehabilitation AI)
 – 재활&운동 전문가 AI SERA
<br/><br/>
#### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 인플루언서후원자들
<table align=center>
  <tbody>
   <tr>
      <td align=center><b>구재회</b></td>
      <td align=center><b>모지호</b></td>
      <td align=center><b>박현아</b></td>
      <td align=center><b>이재범</b></td>
      <td align=center><b>장진슬</b></td>
    </tr>
    <tr>
      <td align="center">
        <img src="image_readme/profile_jaehoi.png" width="200px;"/>
      </td>
      <td align="center">
        <img src="image_readme/profile_jiho.png" width="200px;"/>
      </td>
      <td align="center">
        <img src="image_readme/profile_hyuna.png" width="200px;"/>
      </td>
      <td align="center">
        <img src="image_readme/profile-jaebeom.png" width="200px;"/>
      </td>
      <td align="center">
        <img src="image_readme/profile_jinseul.png" width="200px;"/>
      </td>
    </tr>
    <tr>
        <td align="center">
       <a href="https://github.com/jaehoi-koo">
         <img src="https://img.shields.io/badge/GitHub-jaehoi--koo-FEFFAB?logo=github" alt="구재회 GitHub"/>
       </a>
       </td>  
       <td align="center">
       <a href="https://github.com/mojiho">
         <img src="https://img.shields.io/badge/GitHub-mojiho-FEFFAB?logo=github" alt="모지호 GitHub"/>
       </a>
        <td align="center">
       <a href="https://github.com/hyun-ah-1">
         <img src="https://img.shields.io/badge/GitHub-hyun--ah--1-BD9FFF?logo=github" alt="박현아 GitHub"/>
       </a>
       </td>
       <td align="center">
       <a href="https://github.com/iPad7">
         <img src="https://img.shields.io/badge/GitHub-iPad7-B9FF92?logo=github" alt="이재범 GitHub"/>
       </a>
       </td>
       <td align="center">
       <a href="https://github.com/Jennie-ai333">
         <img src="https://img.shields.io/badge/GitHub-Jennie--ai333-FFAFB0?logo=github" alt="장진슬 GitHub"/>
       </a>
       </td>
    </tr>
  </tbody>
</table>
<br>
<br/><br/>

### R&R


<img src="image_readme/rnr.png" width="600" />



## 2.1 Project Overview - 프로젝트 소개

🧐 **"기억하고, 반응하고, 시간을 느끼는 - 사람같은 챗봇의 탄생"** <br>

💬 왜 사람처럼 느껴지는 AI인가?
우리는 AI가 사람처럼 느껴지기 위해서는 다음의 세 가지 요소가 필수적이라고 보았습니다:

1. 일관된 성격: 시간과 상황이 달라져도 변하지 않는 말투와 태도, 특정 인격처럼 느껴지는 일관된 커뮤니케이션 스타일

2. 개별 사용자에 대한 기억: 사용자마다 이전 대화 내용을 기억하고, 개인 취향이나 과거 이력에 맞춘 맞춤형 응답을 지속하는 능력
   
3. 사용자와의 마지막 상호작용: 마지막 대화 이후 얼마나 시간이 흘렀는지를 인지하고, “오랜만이에요”, “다시 찾아주셨네요” 같은
자연스럽고 상황에 맞는 반응을 제공하는 능력


나아가, 챗봇이 ‘자신의 목표’를 표현하고 행동하는 의지까지 지니게 한다면, 이는 단순한 도구를 넘어 진짜 인플루언서로 작동할 수 있다고 판단했습니다.




🧠 **LLM 기반 RAG(Retrieval-Augmented Generation)** 구조로 **재활운동 제안, 통증부위 상담 챗봇**을 구현. <br>

> 회원가입 된 사용자의 아이디를 세션으로 기억하여 개인화된 상담 제공 <br>
<br>

✔️ **기억하는 AI**의 재활운동 제안, 통증부위 상담을 통해 **AI와 사용자의 유대감 형성, 지속적인 관계 형성**을 목표 <br>


<br><br>

## 2.2 프로젝트 목표

1. 재활 논문, 필라테스 블로그 기반 RAG 챗봇
  - 논문, 필라테스 블로그의 게시물을 크롤링
  - 전문성을 위한 데이터 구축
  - 사용자 정보와 연동되어 개인화된 응답을 제공

2. Django 기반 AI Influencer 스타일의 홈페이지 구현, 회원 관리
  - 핑크 톤의 홈페이지 구축을 통해 활기찬 운동 전문 AI 인플루언서를 표현
  - 관리자 페이지에서 회원 정보, 피드, 투표 항목을 생성/수정/삭제 가능

3. AWS
  - EC2 인스턴스, Gunicorn 활용 웹 서버 환경 구축 및 웹 배포

<br>

### 2.2.3 🛠️ 사용한 기술 스택
<br/><br/>
<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white">
  <img src="https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=selenium&logoColor=white">
  <img src="https://img.shields.io/badge/Chroma-DB-8A2BE2?style=for-the-badge&logo=databricks&logoColor=white">
  <img src="https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white">
  <img src="https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=OpenAI&logoColor=white">
  <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white">
  <img src="https://img.shields.io/badge/AWS-232F3E?style=for-the-badge&logo=amazonaws&logoColor=white">
</p>
<br/><br/>

크로마, sqlite3, selenium, github, AWS, 


--------------------------------------------
## 3. System Architecture
<br>
<p align="center">
  <img src="image_readme/system_architecture.png" width="500"/>
</p>
<br>
--------------------------------------------

## 4. 주요 기능
### 4.1 💬 채팅 시스템
<br>

### 4.2 📊 투표 시스템
<br>

### 4.3 🔐 사용자 인증
<br>

### 4.4 ⚙️ 세션 관리

<br><br>

--------------------------------------------
## 5. 구현 화면 
### 5.1 Home
<br>
  <img src="image_readme/login_home.png" width="500" />
<br>

### 5.2 Login
<br>
  <img src="image_readme/login.png" width="500" />
<br>

### 5.3 Sign up
<br>
  <img src="image_readme/signup.png" width="500" />
<br>  

### 5.4 Chat
<br>
  <img src="image_readme/login_chat.png" width="500" />
<br>

### 5.5 Feed
<br>
  <img src="image_readme/login_feed.png" width="500" />
<br>

### 5.6 Vote / Vote result
<br>
  <img src="image_readme/login_vote.png" width="500" />
  <img src="image_readme/login_vote_result.png" width="500" />
<br>

### 5.7 Profile change
<br>
  <img src="image_readme/login_profile_change1.png" width="500" />
  <img src="image_readme/login_profile_change2.png" width="500" />
<br><br>

--------------------------------------------
## 6. DB 구축

* 💽 DB 선택: Chroma


  <img src="image_readme/ERD.png" width="500" />


<br><br>

--------------------------------------------
## 7. AWS 배포
EC2, Gunicorn
<br><br>

--------------------------------------------
### 8. 최종프로젝트에 구현할 것
AI가 먼저 말을 걸고, 사용자의 과거 대화를 기억하며,
**“오랜만이에요, 지난번 통증은 좀 나아지셨어요?”**와 같은 시간기반/기억기반 반응을 실현할 예정입니다.
또한 **“더 나은 트레이너가 되고 싶다”**, “앞으로 이런 피드백을 더 잘 반영하고 싶다”는 식의 **의지 표현**을 통해,
AI가 **목표를 가진 존재처럼 반응하는 인간형 인플루언서**의 모습을 구현하고자 합니다.
<br>
<br>
여기에 더해, 사용자의 운동 목적이나 증상에 맞춰
**운동 방법과 재활 동작을 이미지, 영상, 음성으로 안내하고**,
스트레칭 도구, 자세 보조 용품, 생활 습관 팁 등도 함께 제안함으로써
**실질적인 운동 조력자 역할까지 수행하는 멀티모달 AI 인플루언서**를 목표로 합니다.

<br><br>

--------------------------------------------
### 9. 한 줄 회고 💭

| 이름 | 한 줄 회고 |
|:------:|-------------------|
| 재회 | |
| 지호 | |
| 현아 | |
| 재범 | |
| 진슬 | |




<br/><br/>
<br/><br/>
<br/><br/>


끝.




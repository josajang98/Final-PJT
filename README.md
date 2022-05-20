[TOC]

# final-pjt

| 항목        | 설명                                                         |
| ----------- | ------------------------------------------------------------ |
| 팀명        | 잘굴러가유<br /><img src="README.assets/KakaoTalk_20220516_170422236.jpg" style="zoom: 10%;" /> |
| 팀원        | 강장호,권다솜,조항주                                         |
| 역할        | front : 권다솜, 조항주<br />back : 강장호                    |
| 프로젝트 명 | 잘골라줘유<br />![](README.assets/Free_Sample_By_Wix.jpg)    |

## 1.목표

`잘골라줘유`를 사용하는 user 개인의 취향을 반영하여 영화를 추천한다.

## 2.준비사항

- 언어 : django, vue, python, javascript
- 도구 : vscode, chrome, figma, ERDCloud, TMDB API, git, Typora

## 3.프로젝트 컨셉 주요기능

- 컨셉 : 잘 골라주는 사이트

- 주요 기능 : 장르 월드컵

## 4.요구사항

**[ accounts ]**

| HTTP method | URL 패턴            | component       | 설명                   |
| ----------- | ------------------- | :-------------- | ---------------------- |
| GET         | /                   | MainUnlogin.vue |                        |
| GET         | /accounts/login     | LoginView.vue   | 로그인 페이지 렌더링   |
| POST        | /accounts/login     |                 | 로그인 요청            |
| POST        | /accounts/logout    |                 | 로그아웃 요청          |
| GET         | /accounts/signup    | SignupView.vue  | 회원가입 페이지 렌더링 |
| POST        | /accounts/signup    |                 | 회원가입 요청          |
| GET         | /accounts/{user_id} |                 | 유저페이지 렌더링      |

**[ articles ]**

| HTTP method | URL 패턴                                 | component            | 설명                          |
| ----------- | ---------------------------------------- | :------------------- | ----------------------------- |
| GET         | /articles                                | MainLogin.vue        | 메인페이지 렌더링             |
| GET         | /articles/genrewc                        | Genrewc.vue          | 장르월드컵 페이지 렌더링      |
| GET         | /articles/genrewc/{genre_id}             | GenrewcResult.vue    | 장르월드컵 결과 페이지 렌더링 |
| POST        | /articles/genrewc/{genre_id}             |                      | db에 유저의 장르 id 저장      |
| GET         | /articles/{movie_id}                     |                      | 영화 상세페이지 렌더링        |
| POST        | /articles/{movie_id}/create              |                      | 리뷰생성 요청                 |
| POST        | /articles/{movie_id}/{review_id}/like    |                      | 리뷰 좋아요 요청              |
| GET         | /articles/{movie_id}/{review_id}/update/ | ReviewUpdateForm.vue | 리뷰업데이트 페이지 렌더링    |
| POST        | /articles/{movie_id}/{review_id}/update/ |                      | 리뷰수정 요청                 |
| POST        | /articles/{movie_id}/{review_id}/delete/ |                      | 리뷰삭제 요청                 |



articles(유배)

| HTTP method | URL 패턴                         | component            | 설명                          |
| ----------- | -------------------------------- | :------------------- | ----------------------------- |
| GET         | /                                | MainLogin.vue        |                               |
| GET         | /articles/genrewc                | Genrewc.vue          | 장르월드컵 페이지 렌더링      |
| GET         | /articles/genrewc/{genre_id}     | GenrewcResult.vue    | 장르월드컵 결과 페이지 렌더링 |
| POST        | /articles/genrewc/{genre_id}     |                      | db에 유저의 장르 id 저장      |
| GET         | /articles/reviewlist             | ReviewList.vue       | 리뷰게시판 페이지 렌더링      |
| GET         | /articles/reviewlist/create      | ReviewCreateForm.vue | 리뷰생성 페이지 렌더링        |
| POST        | /articles/reviewlist/create      |                      | 리뷰생성 요청                 |
| GET         | /articles/reviewlist/{id}detail/ | ReviewDetail.vue     | 리뷰디테일 페이지 렌더링      |
| GET         | /articles/reviewlist/{id}update/ | ReviewUpdateForm.vue | 리뷰업데이트 페이지 렌더링    |
| POST        | /articles/reviewlist/{id}update/ |                      | 리뷰수정 요청                 |
| POST        | /articles/reviewlist/{id}delete/ |                      | 리뷰삭제 요청                 |
| GET         | /articles/{movie_id}             |                      |                               |



## 5. 프로젝트 개발 일지

### 0517

#### 오늘의 진행과정

1. 피그마(툴)를 사용하여 웹 레이아웃 작성

   ![](README.assets/SmartSelectImage_2022-05-20-16-34-50.png)

   ![](README.assets/SmartSelectImage_2022-05-20-16-37-09.png)

2. ERDCloud를 사용하여 ERD 작성

   ![](README.assets/SmartSelectImage_2022-05-20-16-38-18.png)

#### 오늘의 위기

1. `진행과정1` 피그마 사용법 미숙
   - 해결방법 : 몸으로 부딪힌다... (with. 구선생님)
2. `진행과정1` 메인 색상 팔레트 결정 난제
   - 해결방법 : 여러색상을 적용하여 제일 나은 색 조합을 선택함 -> 테마는 학교 칠판

---

### 0519 

#### 오늘의 진행과정

1. django pjt 생성
2. model 작성

#### 오늘의 위기

1. `진행과정2` movie 데이터를 db에 저장하지 않아 fk 설정에 어려움 발생 
   - 해결방법 : review model에서 movie_id 필드를 fk로 안하고 int로 설정 후 우리가 fk처럼 사용하기로 정함

---

### 0520

#### 오늘의 진행과정

1. db에 데이터 저장 여부 결정

   - 결정 사항 : 저장하지 않고 필요한 경우에만, 필요 데이터 호출하여 사용함

     | 페이지    | component      | api                                      | 비고                                           |
     | --------- | -------------- | ---------------------------------------- | ---------------------------------------------- |
     | 메인      | 제일 상단 사진 | **GET**/movie/now_playing                |                                                |
     | 메인      | 장르 같은 영화 | **GET**/movie/popular                    | 렌덤으로 페이지 정해서 같은 장르 영화 가져오기 |
     | 메인      | 배우 영화      | **GET**/person/{person_id}/movie_credits |                                                |
     | 디테일    | 예고편         | **GET**/movie/{movie_id}/videos          |                                                |
     | 찜한 목록 | 디테일         | GET movie/{movie_id}                     |                                                |

2. Components 재확인 및 model & ERD 수정

   - 메인 페이지 : 베너는 넷플릭스처럼 한가지만 보임 (영화 제목 + 포스터)

3. front(조항주,권다솜) 와 back(강장호)으로 역할 분담

   - front(vue) : login / logout / signup
   - back(django) : login / logout / signup / profile(without articles)

#### 오늘의 위기

1. `진행과정2` django의 accounts/model.py에서 genre_id가 user를 생성할 때 에러가 발생함
   - 해결방법 : default=0 속성을 준다.
2. `진행과정3` vue : login 하는 과정에서 이해가 부족함
   - 해결방법 : 유튜브 라이브 교수님 코드를 천천히 살펴봄.

---


# final-pjt

제목

## 목차

1. 목표
2. 준비사항
3. 프로젝트 컨셉 주요기능
4. 요구사항
   1. 컴포넌트 구조
   2. DB 모델링
   3. router
   4. 레이아웃 구성



### 1.목표

### 2.준비사항

### 3.프로젝트 컨셉 주요기능

### 4.요구사항

accounts

| HTTP method | URL 패턴            | component       | 설명                   |
| ----------- | ------------------- | :-------------- | ---------------------- |
| GET         | /                   | MainUnlogin.vue |                        |
| GET         | /accounts/login     | LoginView.vue   | 로그인 페이지 렌더링   |
| POST        | /accounts/login     |                 | 로그인 요청            |
| POST        | /accounts/logout    |                 | 로그아웃 요청          |
| GET         | /accounts/signup    | SignupView.vue  | 회원가입 페이지 렌더링 |
| POST        | /accounts/signup    |                 | 회원가입 요청          |
| GET         | /accounts/{user_id} |                 | 유저페이지 렌더링      |

articles

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



0519 

django에서 review에 movie_id를  fk 로 사용하려면 movie 모델이 있어야 함

근데 우리는 movie데이터를 db에 저장안하고 api에서 가져와서 사용하기로 했음

그래서 movie_id 필드를 fk로 안하고 int로 설정 후 우리가 fk처럼 사용하기로 정함



0520

- 메인페이지
  - 제일 상단 사진
    **GET**/movie/now_playing 
  - 장르 같은 영화
    **GET**/movie/popular 에서 렌덤으로 페이지 정해서 같은 장르 영화 가져오기
  - 배우 영화
    **GET**/person/{person_id}/movie_credits
- 디테일 페이지 
  - 예고편 
    **GET**/movie/{movie_id}/videos
- 찜한 목록
  - 디테일
    GET movie/{movie_id}

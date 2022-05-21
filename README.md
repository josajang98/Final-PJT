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

| HTTP method | URL 패턴                                  | component            | 설명                          |
| ----------- | ----------------------------------------- | :------------------- | ----------------------------- |
| GET         | /articles                                 | MainLogin.vue        | 메인페이지 렌더링             |
| GET         | /articles/genrewc                         | Genrewc.vue          | 장르월드컵 페이지 렌더링      |
| GET         | /articles/genrewc/{genre_id}              | GenrewcResult.vue    | 장르월드컵 결과 페이지 렌더링 |
| POST        | /articles/genrewc/{genre_id}              |                      | db에 유저의 장르 id 저장      |
| GET         | /articles/{movie_id}/reviews/             |                      | 영화 상세페이지 렌더링        |
| POST        | /articles/{movie_id}reviews/              |                      | 리뷰생성 요청                 |
| POST        | /articles/{movie_id}/like/{review_id}/    |                      | 리뷰 좋아요 요청              |
| GET         | /articles/{movie_id}/reviews/{review_id}/ | ReviewUpdateForm.vue | 리뷰업데이트 페이지 렌더링    |
| POST        | /articles/{movie_id}/reviews/{review_id}/ |                      | 리뷰수정 요청                 |
| POST        | /articles/{movie_id}/reviews/{review_id}/ |                      | 리뷰삭제 요청                 |
| GET         | /articles/wishlist/                       |                      | 사용자가 찜한 영화            |
| POST        | /articles/wishlist/                       |                      | 찜한 영화 사용자에 저장       |



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

---

**[ 야근 ]**

4. front(조항주,권다솜) & back(강장호)
   - front : 로그인 했을 때 보이는 메인 페이지 생성 [ navbar만 생성했음,,, search bar 어케하는거냐고,,,, ]
   - back : 영화 리뷰 생성 [ 현재 진행상황 : 실패,,,:bomb: ]

#### 오늘의 위기

1. `진행과정2` django의 accounts/model.py에서 genre_id가 user를 생성할 때 에러가 발생함
   - 해결방법 : default=0 속성을 준다.
   
2. `진행과정3` vue : login 하는 과정에서 이해가 부족함
   - 해결방법 : 유튜브 라이브 교수님 코드를 천천히 살펴봄.
   
3. `진행과정4` front : views에 `Ariticles.vue`로 파일명을 정했을때, **Component name "Articles" should always be multi-word  vue/multi-word(컴포넌트 이름은 항상 여러 단어로 되어야 한다.)**
   - 해결방법 : ArticlesView로 이름을 변경해줌.
   
4. `진행과정4` back : review 생성이 안됨,,,,,,, 왜 안돼? ,,,,, 좀 잘 되면 얼마나 좋겠냐!!!!!!!

   - 해결방법 : 

     ```python
     reviews = get_list_or_404(Review)
     serializer.save(user=user)
     ```

     리뷰모델이 비어있을 때 get_list_or_404를 호출하는 경우를 고려했음

     serializer 데이터를 저장할 때 movie_id를 따로 인자로 받지 않게 수정

---

### 0521

#### 오늘의 진행과정

1. review CRUD 구현 및 테스트

   ```python
       def seleted_movie(reviews, movie_pk):
           reviews_seleted_movie = []
           for review in reviews:
               if review.movie_id == movie_pk:
                   reviews_seleted_movie.append(review)
           return reviews_seleted_movie
   ```

   - movie를 장고에 저장하지 않기때문에 orm함수를 사용할 수 없음
   - 따라서 list전체를 받고 거기서 movie_pk값에 맞는 review들을 Response해주어야 함
   - 그에 따른 함수를 구현 => movie_id와 movie_pk이 같은 값들을 리스트에 모아 json으로 보내준다

2. review_ like 구현








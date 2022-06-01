[TOC]



# 🏆Final-pjt

SSAFY 상반기 관통 최종 프로젝트 **최우수상** 수상작

# 결과물 Preview

- 로그인 & 회원가입
  ![login](README.assets/login.gif)
- 메인페이지
  ![mainpage](README.assets/mainpage.gif)
- 장르월드컵
  ![genrewc](README.assets/genrewc.gif)
- 영화 상세페이지
  ![detail](README.assets/detail.gif)
- 유저페이지
  ![userpage](README.assets/userpage.gif)
- 검색페이지
  ![search](README.assets/search.gif)

## 1.목표

`잘골라줘유`를 사용하는 user 개인의 취향을 반영하여 영화를 추천한다.



## 2.준비사항

- 언어 : django, vue, python, javascript
- 도구 : vscode, chrome, figma, ERDCloud, TMDB API, git, Typora



## 3.팀원 정보 및 업무 분담 내역

- 강장호: backend
- 권다솜: frontend
- 조항주: frontend



## 4.프로젝트 컨셉 

- 컨셉 : 사용자에게 맞는 영화를 추천하고 리뷰기능을 사용하여 다른 유저들과 소통 가능



## 5.실제 구현 정도

​	구현 정도: __400%__

​	기존 설계는 물론, 구현하고 싶은 기능들도 모두 구현했습니다



## 6.필수 기능

- drf

  - accounts

    | HTTP method | URL 패턴                                | component       | 설명                      |
    | ----------- | --------------------------------------- | :-------------- | ------------------------- |
    | GET         | /                                       | MainUnlogin.vue | 비로그인 메인페이지       |
    | GET         | /accounts/login                         | LoginView.vue   | 로그인 페이지 라우팅      |
    | GET         | /accounts/signup                        | SignupView.vue  | 회원가입 페이지 라우팅    |
    | GET         | /accounts/:username/profile             | ProfileView.vue | 유저 프로필 페이지 라우팅 |
    | POST        | /accounts/login                         |                 | 로그인 요청               |
    | POST        | /accounts/logout                        |                 | 로그아웃 요청             |
    | POST        | /accounts/signup                        |                 | 회원가입 요청             |
    | POST        | /accounts/wishlist                      |                 | 찜한목록 데이터 요청      |
    | POST        | /accounts/{username}/profile            |                 | 유저 데이터 요청          |
    | PUT         | /accounts/{username}/profile/{genre_id} |                 | 유저 선호 장르 업데이트   |

  - articles

    | HTTP method | URL 패턴                                  | component         | 설명                      |
    | ----------- | ----------------------------------------- | :---------------- | ------------------------- |
    | GET         | /articles                                 | ArticlesView.vue  | 메인페이지 라우팅         |
    | GET         | /articles/genrewc                         | Genrewc.vue       | 장르월드컵 페이지 라우팅  |
    | GET         | /articles/:movie_id                       | ArticleDetail.vue | 영화 디테일 페이지 라우팅 |
    | GET         | /accounts/wishList                        | WishList.vue      | 찜한 목록 페이지 라우팅   |
    | GET         | /articles/search/:query/                  | SearchResult.vue  | 검색결과 페이지 라우팅    |
    | GET         | /articles/person/:person_id               | PersonDetail      | 배우 디테일 페이지 라우팅 |
    | GET         | /articles/{movie_id}/reviews/             |                   | 리뷰 리스트 요청          |
    | PUT         | /articles/{movie_id}/reviews/{reviewId}/  |                   | 리뷰 수정 요청            |
    | POST        | /articles/{movie_id}/like/{review_id}/    |                   | 리뷰 좋아요 요청          |
    | DELETE      | /articles/{movie_id}/reviews/{review_id}/ |                   | 리뷰삭제 요청             |

  - tmdb

    ```js
    tmdb: {
        nowPlaying: () => BASE_URL + `movie/now_playing/?api_key=${api_key}&language=${language}`,
        popular: (page) => BASE_URL + `movie/popular/?api_key=${api_key}&language=${language}&page=${page}`,
        searchPerson: (query) => BASE_URL + `search/person/?api_key=${api_key}&language=${language}&query=${query}`,
        person: (person_id) => BASE_URL + `person/${person_id}/movie_credits?api_key=${api_key}&language=${language}`,
        personDetail: (person_id) => BASE_URL + `person/${person_id}?api_key=${api_key}&language=${language}`,
        credits: (movie_id) => BASE_URL + `movie/${movie_id}/credits?api_key=${api_key}&language=${language}`,
        detail: (movie_id) => BASE_URL + `movie/${movie_id}?api_key=${api_key}&language=${language}`,
        videos: (movie_id) => BASE_URL + `movie/${movie_id}/videos?api_key=${api_key}&language=${language}`,
        getMovieCreadit: (person_id) => BASE_URL + `person/${person_id}/movie_credits?api_key=${api_key}&language=${language}`,
        searchMovie: (query) => BASE_URL + `search/movie?api_key=${api_key}&language=${language}&query=${query}`,
      }
    ```

    

- 회원가입, 로그인, 로그아웃
  dj-rest-auth 라이브러리를 사용한 기능 구현  

- youtube api를 사용한 백그라운드 동영상

- 메인 페이지에서 사용자에게 다양한 영화 추천

  -  찜 목록에서 랜덤한 영화의 랜덤한 배우를 선택해서 출연한 영화를 추천
  -  유저가 선호하는 장르로 영화를 필터링해서 추천
  -  현재 상영중인 영화를 추천

- 영화 디테일 페이지에서 찜 및 리뷰 기능 사용

  - 영화를 찜 하면 "찜한 목록"페이지에서 내가 찜한 영화들을 볼 수 있음
  - 영화에 제목과 내용 평점으로 리뷰를 남기고, 이에 다른 유저들이 좋아요를 누를 수 있음 

- 장르월드컵을 통한 사용자가 선호하는 장르 선정

  - tmdb api에서 제공하는 영화장르 19개중 랜덤으로 16개를 선정한 후 16강 월드컵을 진행해 사용자가 선호하는 장르를 선정

- 영화제목과 배우이름으로 영화 검색

  - 검색창에 입력 받은 데이터로 영화와 배우 이름으로 tmdb api 검색 요청을 하고 이를 보여줌

- 프로필 페이지에서 내가 작성한 리뷰와 좋아요 누른 리뷰 확인



## 7.느낀점



## 8.프로젝트 개발 일지

### 0517

#### 오늘의 진행과정

1. 피그마(툴)를 사용하여 웹 레이아웃 작성

   ![](README.assets/SmartSelectImage_2022-05-20-16-34-50.png)

   ![](README.assets/SmartSelectImage_2022-05-20-16-37-09.png)

2. ERDCloud를 사용하여 ERD 작성

   ![image-20220527033913289](C:\Users\jo\Desktop\ssafy7\pjt\final-pjt\README.assets\erd.png)

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

##### django

- review CRUD 구현 및 테스트

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

- review_ like 구현

##### vue

- ArticlesView 의 MainMovieCard 컴포넌트 구현
  - dfs에 tmdb url 추가
  - axios 요청으로 nowPlaying 데이터를 가져와서 lodash 랜덤으로 영화의 backdrop_path와 title를 가져와서 페이지에 보여줌

#### 



### 0522

#### 오늘의 진행과정

##### django

- wish list show and save 구현 및 테스트

  ```python
  user = request.user
  movie_id = request.data['movie_id']
  wish_list = WishList.objects.all().filter(user_id=user)
  
  # 위시무비 id 값만 불러오기
  wish_movie_id = []
  for wish in wish_list:
  	wish_movie_id.append(wish.movie_id)
  
  # wish_movie_id값안에 값이 있으면 ==> 삭제
  if movie_id in wish_movie_id:
  	wish_object = get_object_or_404(WishList,user_id=user,movie_id=movie_id)
  	wish_object.delete()
  	serializers = WishListSerializer(wish_object)
  	return Response(serializers.data)
  
  else:
      없으면 저장
  
  ```

- 오늘의 위기

  - movie_id값을 request로 받아오기 때문에 데이터에서 dictionary로 받아와야 함
  - wish_list를 받아올때 get_list_or_404로 받아오지 못함
    - 왜냐하면 새로운 유저가 찜을 눌렀을때 아무것도 없을시에 404에러가 뜨게 된다
    - 이렇게 되면 안되기 때문에 빈리스트로 마무리를 시켜준다
  - for문을 이용하여 movie id 값만 받아와서 비교한다.
  - if 문을 사용해서 리스트에 있는 id값의 존재 여부를 비교한다.
    - 리스트를 써도 되는 이유 : 한유저가 아무리 많은 영화를 눌러도 얼마 안될 것이기 때문에

##### vue

- 데이터 흐름 변경
  MainMovieCard 컴포넌트에서 axios 요청을 통해 데이터를 가져오던걸 부모 컴포넌트인 ArticleView 컴포넌트에서 가져와서 props로 전달해주는 방식으로 변경

- ArticlesVies.vue의 getNowPlayingMovie() 메서드 분리
  기존에 api요청을 보내서 현재 상영중인 영화를 가져오고 그 안에서 렌덤으로 데이터 하나를 저장했던 getNowPlayingMovie() 를 
  현재 상영중인 영화 데이터를 저장하는 getNowPlayingMovieList()와 그 안에서 렌덤 영화를 저장하는 getRandMovieData()로 분리함

- 오늘의 위기
  created 라이프 싸이클 훅이 동기적으로 코드가 실행되지 않는거 같다,,, 현재 상영중인 영화 정보를 먼저 가져오고 랜덤 무비를 가져와야 되는데 그게 안돼

  ```js
  created(){
      this.getNowPlayingMovieList()
      this.getRandMovieData()
    },
  mounted() {
      this.getRandMovieData()
    },
  ```

  이런식으로 짜면 안돼 그래서 

  ```vue
  <template>
    <div>
      {{getRandMovieData()}}
      <MainMovieCard :backdrop-path="mainMovieBackdropPath" :title="mainMovietitle"></MainMovieCard>
    </div>
  </template>
  ```

  일단 임시로 이렇게 실행시켜놨습니다,,



### 0523

#### 오늘의 진행과정

##### django

- wish list save할때 반환 값이 object에서 list값으로 변경
- review를 달때 한영화에 하나의 review만 쓸수 있도록 변경
- review list에 평점 추가
- 프로필 창에 좋아하는 리뷰, 좋아하는 리뷰의 개수, 내가 작성한 리뷰와 개수 추가

**review list**

```python
# movie_id 모음
review_movie_list = []
for review_ojt in review_list:
    review_movie_list.append(review_ojt.movie_id)
        
# 작성되어 있을시 data보냄
if movie_pk in review_movie_list:
    data = {
        'exist':f'이미 작성하셨습니다'
    }
	return Response(data, status=status.HTTP_201_CREATED)

# 작성 안되어 있을시 저장
else:
	serializer = ReviewSerializer(data=request.data)
	if serializer.is_valid(raise_exception=True):
		serializer.save(user=user)
		reviews = get_list_or_404(Review)
		reviews_selected_movie = seleted_movie(reviews, movie_pk)
		serializer = ReviewSerializer(reviews, many=True)
		return Response(serializer.data, status=status.HTTP_201_CREATED)
```

- movie id 값을 모아두고 for문을 통해서 movie_pk가 있는지 확인
  - 있음 ==> 이미 작성 했다는 data를 보내준다
  - 없음 ==> review list로 받아서 보내준다

**rate**

```python
def rate_selected_movie(reviews, movie_pk):
    rate_selected_movie = []
    for review in reviews:
        if review.movie_id == movie_pk:
            rate_selected_movie.append(review.rate)
            return rate_selected_movie

rate_list = rate_selected_movie(reviews, movie_pk)
average_rate = round(sum(rate_list)/len(rate_list),1)
```

- 선택된 movie들을 list에 담아 평균을 구해준다.



**like_review, review_count in profile**

```python
like_review = ReviewSerializer(many=True, read_only=True)
review_count = serializers.IntegerField(source='review_set.count',read_only=True)
```

- ReviewSerializer는 새로 calss를 만들어서 커스텀 해줌

- ProfileSerializer에 이 두 값들을 추가 해준다



**genre_save**

```python
serializers = UserSerializer(instance=user, data=request.data)
```

- 업데이트 구현할때와 마찬가로 instance=user를 넣음으로서 기존것들을 가져오고 업데이트만 시킨다.



##### vue

- 로그인 시에도 8080/ 로 접속했을 때 로그인 페이지가 렌더링 되는 문제 해결
  MainUnlogin.vue 의 created 라이프사이클 훅에 로그인시 articles로 라우팅 되는 메서드를 걸어둠
  
- 비로그인 시 /articles로 접속되는 문제 해결

- 메인 페이지

  - 장르 영화 추천 목록 생성
  - 배우 영화 추천 목록 생성
  - 현재 상영중 영화 추천 목록 생성

- 무비 디테일 페이지 추가

  - get Detail api로 영화 정보 가져와서 랜더링

  - 리뷰 리스트 django에서 가져와서 랜더링
  - 리뷰 좋아요 버튼 추가 

- 장르월드컵 포스터 추가(메바솜)

### 0524

#### 오늘의 진행과정

##### django

- db저장
  - 위기 : settings.py 에 새로 만든 movie앱 등록을 안했음.

##### vue

- 기능 구현

  - 영화 상세 페이지의 리뷰
    - 리뷰 폼 생성
    - 리뷰 수정
    - 리뷰 삭제

  - 영화 찜

  - 위시리스트 페이지 생성

  - 찜 구현 

  - 프로필페이지 

  - 리뷰 상세페이지 

  - 리뷰리스트 데이터 수정,삭제,생성

  - 검색

  - 검색 결과페이지

  - 인물 컴포넌트

  - 영화 컴포넌트

- 버그 수정
  - 빨간색 에러
  - 찜 트루펄스
  - 데이터 폼 수정
  - 사진없는 데이터 핸들링
  - 프로필에서 댓글 작성자 보기 
  - 리뷰에 영화 제목 보이기

### 0525

##### vue

- 기능 구현
  - 인물상세 페이지
  - 검색에서 포스터 없는 데이터 랜더링안함
  - 하트 찜한거로 표시되나 안돼:?
  - 사람 디테일 가져오기
  - 장르월드컵
  - 프로필페이지에 장르 선택기능 추가
  - 찜한 목록에서 배우 정보 가져오기
  - 디테일 페이지에 유저 평점도 넣어주기
  - 인물 미리보기에 영화 3개 추가
  - 인물 디테일 api에서 인물 정보 가져오기
  - 프로필페이지 장르 선택에 내 장르 보여주기
  - 댓글 수정 버튼 
  - 배우 정보 가져올때 랜덤으로 가져오기
  - 장르월드컵 결과페이지에 같은 장르 영화 가져오기
- 버그 수정
  - 다른 사람이 쓴 댓글 내가 수정

### 0526

##### vue

- 기능 구현
  - 장르 월드컵 선택시 흔들리는 css
  - 시작페이지로 가야되는데 로그인페이지로감
  - 리뷰카드 사진 누르면 영화 디테일로 이동
  - 찜한 목록 호버시 데이터 
  - 인물상세페이지,장르월드컵 가로스크롤하고 스크롤 색상 변경
  - 로그아웃했을 때 메인으로가기
- 리팩토링
  - 인물 정보 data->vuex
- 버그 수정
  - 로그인 하고 다시 로그인 페이지 접속
  - 로그인 실패시 핸들링
  - 회원가입 실패시 핸들링
  - 메인페이지 새로고침시 장르 데이터 못불러옴 vuex-persistedstate
  - 사람 디테일 페이지 정보 잘못가져옴
  - 모달 나갈 때 멈춤
  - 장르월드컵 결과에서 '강'이 뜸




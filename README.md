[TOC]



# ๐Final-pjt

SSAFY ์๋ฐ๊ธฐ ๊ดํต ์ต์ข ํ๋ก์ ํธ **์ต์ฐ์์** ์์์

# ๊ฒฐ๊ณผ๋ฌผ Preview

- ๋ก๊ทธ์ธ & ํ์๊ฐ์
  ![login](README.assets/login.gif)
- ๋ฉ์ธํ์ด์ง
  ![mainpage](README.assets/mainpage.gif)
- ์ฅ๋ฅด์๋์ปต
  ![genrewc](README.assets/genrewc.gif)
- ์ํ ์์ธํ์ด์ง
  ![detail](README.assets/detail.gif)
- ์ ์ ํ์ด์ง
  ![userpage](README.assets/userpage.gif)
- ๊ฒ์ํ์ด์ง
  ![search](README.assets/search.gif)

## 1.๋ชฉํ

`์๊ณจ๋ผ์ค์ `๋ฅผ ์ฌ์ฉํ๋ user ๊ฐ์ธ์ ์ทจํฅ์ ๋ฐ์ํ์ฌ ์ํ๋ฅผ ์ถ์ฒํ๋ค.



## 2.์ค๋น์ฌํญ

- ์ธ์ด : django, vue, python, javascript
- ๋๊ตฌ : vscode, chrome, figma, ERDCloud, TMDB API, git, Typora



## 3.ํ์ ์ ๋ณด ๋ฐ ์๋ฌด ๋ถ๋ด ๋ด์ญ

- ๊ฐ์ฅํธ: backend
- ๊ถ๋ค์: frontend
- ์กฐํญ์ฃผ: frontend



## 4.ํ๋ก์ ํธ ์ปจ์ 

- ์ปจ์ : ์ฌ์ฉ์์๊ฒ ๋ง๋ ์ํ๋ฅผ ์ถ์ฒํ๊ณ  ๋ฆฌ๋ทฐ๊ธฐ๋ฅ์ ์ฌ์ฉํ์ฌ ๋ค๋ฅธ ์ ์ ๋ค๊ณผ ์ํต ๊ฐ๋ฅ



## 5.์ค์  ๊ตฌํ ์ ๋

โ	๊ตฌํ ์ ๋: __400%__

โ	๊ธฐ์กด ์ค๊ณ๋ ๋ฌผ๋ก , ๊ตฌํํ๊ณ  ์ถ์ ๊ธฐ๋ฅ๋ค๋ ๋ชจ๋ ๊ตฌํํ์ต๋๋ค



## 6.ํ์ ๊ธฐ๋ฅ

- drf

  - accounts

    | HTTP method | URL ํจํด                                | component       | ์ค๋ช                      |
    | ----------- | --------------------------------------- | :-------------- | ------------------------- |
    | GET         | /                                       | MainUnlogin.vue | ๋น๋ก๊ทธ์ธ ๋ฉ์ธํ์ด์ง       |
    | GET         | /accounts/login                         | LoginView.vue   | ๋ก๊ทธ์ธ ํ์ด์ง ๋ผ์ฐํ      |
    | GET         | /accounts/signup                        | SignupView.vue  | ํ์๊ฐ์ ํ์ด์ง ๋ผ์ฐํ    |
    | GET         | /accounts/:username/profile             | ProfileView.vue | ์ ์  ํ๋กํ ํ์ด์ง ๋ผ์ฐํ |
    | POST        | /accounts/login                         |                 | ๋ก๊ทธ์ธ ์์ฒญ               |
    | POST        | /accounts/logout                        |                 | ๋ก๊ทธ์์ ์์ฒญ             |
    | POST        | /accounts/signup                        |                 | ํ์๊ฐ์ ์์ฒญ             |
    | POST        | /accounts/wishlist                      |                 | ์ฐํ๋ชฉ๋ก ๋ฐ์ดํฐ ์์ฒญ      |
    | POST        | /accounts/{username}/profile            |                 | ์ ์  ๋ฐ์ดํฐ ์์ฒญ          |
    | PUT         | /accounts/{username}/profile/{genre_id} |                 | ์ ์  ์ ํธ ์ฅ๋ฅด ์๋ฐ์ดํธ   |

  - articles

    | HTTP method | URL ํจํด                                  | component         | ์ค๋ช                      |
    | ----------- | ----------------------------------------- | :---------------- | ------------------------- |
    | GET         | /articles                                 | ArticlesView.vue  | ๋ฉ์ธํ์ด์ง ๋ผ์ฐํ         |
    | GET         | /articles/genrewc                         | Genrewc.vue       | ์ฅ๋ฅด์๋์ปต ํ์ด์ง ๋ผ์ฐํ  |
    | GET         | /articles/:movie_id                       | ArticleDetail.vue | ์ํ ๋ํ์ผ ํ์ด์ง ๋ผ์ฐํ |
    | GET         | /accounts/wishList                        | WishList.vue      | ์ฐํ ๋ชฉ๋ก ํ์ด์ง ๋ผ์ฐํ   |
    | GET         | /articles/search/:query/                  | SearchResult.vue  | ๊ฒ์๊ฒฐ๊ณผ ํ์ด์ง ๋ผ์ฐํ    |
    | GET         | /articles/person/:person_id               | PersonDetail      | ๋ฐฐ์ฐ ๋ํ์ผ ํ์ด์ง ๋ผ์ฐํ |
    | GET         | /articles/{movie_id}/reviews/             |                   | ๋ฆฌ๋ทฐ ๋ฆฌ์คํธ ์์ฒญ          |
    | PUT         | /articles/{movie_id}/reviews/{reviewId}/  |                   | ๋ฆฌ๋ทฐ ์์  ์์ฒญ            |
    | POST        | /articles/{movie_id}/like/{review_id}/    |                   | ๋ฆฌ๋ทฐ ์ข์์ ์์ฒญ          |
    | DELETE      | /articles/{movie_id}/reviews/{review_id}/ |                   | ๋ฆฌ๋ทฐ์ญ์  ์์ฒญ             |

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

    

- ํ์๊ฐ์, ๋ก๊ทธ์ธ, ๋ก๊ทธ์์
  dj-rest-auth ๋ผ์ด๋ธ๋ฌ๋ฆฌ๋ฅผ ์ฌ์ฉํ ๊ธฐ๋ฅ ๊ตฌํ  

- youtube api๋ฅผ ์ฌ์ฉํ ๋ฐฑ๊ทธ๋ผ์ด๋ ๋์์

- ๋ฉ์ธ ํ์ด์ง์์ ์ฌ์ฉ์์๊ฒ ๋ค์ํ ์ํ ์ถ์ฒ

  -  ์ฐ ๋ชฉ๋ก์์ ๋๋คํ ์ํ์ ๋๋คํ ๋ฐฐ์ฐ๋ฅผ ์ ํํด์ ์ถ์ฐํ ์ํ๋ฅผ ์ถ์ฒ
  -  ์ ์ ๊ฐ ์ ํธํ๋ ์ฅ๋ฅด๋ก ์ํ๋ฅผ ํํฐ๋งํด์ ์ถ์ฒ
  -  ํ์ฌ ์์์ค์ธ ์ํ๋ฅผ ์ถ์ฒ

- ์ํ ๋ํ์ผ ํ์ด์ง์์ ์ฐ ๋ฐ ๋ฆฌ๋ทฐ ๊ธฐ๋ฅ ์ฌ์ฉ

  - ์ํ๋ฅผ ์ฐ ํ๋ฉด "์ฐํ ๋ชฉ๋ก"ํ์ด์ง์์ ๋ด๊ฐ ์ฐํ ์ํ๋ค์ ๋ณผ ์ ์์
  - ์ํ์ ์ ๋ชฉ๊ณผ ๋ด์ฉ ํ์ ์ผ๋ก ๋ฆฌ๋ทฐ๋ฅผ ๋จ๊ธฐ๊ณ , ์ด์ ๋ค๋ฅธ ์ ์ ๋ค์ด ์ข์์๋ฅผ ๋๋ฅผ ์ ์์ 

- ์ฅ๋ฅด์๋์ปต์ ํตํ ์ฌ์ฉ์๊ฐ ์ ํธํ๋ ์ฅ๋ฅด ์ ์ 

  - tmdb api์์ ์ ๊ณตํ๋ ์ํ์ฅ๋ฅด 19๊ฐ์ค ๋๋ค์ผ๋ก 16๊ฐ๋ฅผ ์ ์ ํ ํ 16๊ฐ ์๋์ปต์ ์งํํด ์ฌ์ฉ์๊ฐ ์ ํธํ๋ ์ฅ๋ฅด๋ฅผ ์ ์ 

- ์ํ์ ๋ชฉ๊ณผ ๋ฐฐ์ฐ์ด๋ฆ์ผ๋ก ์ํ ๊ฒ์

  - ๊ฒ์์ฐฝ์ ์๋ ฅ ๋ฐ์ ๋ฐ์ดํฐ๋ก ์ํ์ ๋ฐฐ์ฐ ์ด๋ฆ์ผ๋ก tmdb api ๊ฒ์ ์์ฒญ์ ํ๊ณ  ์ด๋ฅผ ๋ณด์ฌ์ค

- ํ๋กํ ํ์ด์ง์์ ๋ด๊ฐ ์์ฑํ ๋ฆฌ๋ทฐ์ ์ข์์ ๋๋ฅธ ๋ฆฌ๋ทฐ ํ์ธ



## 7.๋๋์ 



## 8.ํ๋ก์ ํธ ๊ฐ๋ฐ ์ผ์ง

### 0517

#### ์ค๋์ ์งํ๊ณผ์ 

1. ํผ๊ทธ๋ง(ํด)๋ฅผ ์ฌ์ฉํ์ฌ ์น ๋ ์ด์์ ์์ฑ

   ![](README.assets/SmartSelectImage_2022-05-20-16-34-50.png)

   ![](README.assets/SmartSelectImage_2022-05-20-16-37-09.png)

2. ERDCloud๋ฅผ ์ฌ์ฉํ์ฌ ERD ์์ฑ

   ![image-20220527033913289](C:\Users\jo\Desktop\ssafy7\pjt\final-pjt\README.assets\erd.png)

#### ์ค๋์ ์๊ธฐ

1. `์งํ๊ณผ์ 1` ํผ๊ทธ๋ง ์ฌ์ฉ๋ฒ ๋ฏธ์
   - ํด๊ฒฐ๋ฐฉ๋ฒ : ๋ชธ์ผ๋ก ๋ถ๋ชํ๋ค... (with. ๊ตฌ์ ์๋)
2. `์งํ๊ณผ์ 1` ๋ฉ์ธ ์์ ํ๋ ํธ ๊ฒฐ์  ๋์ 
   - ํด๊ฒฐ๋ฐฉ๋ฒ : ์ฌ๋ฌ์์์ ์ ์ฉํ์ฌ ์ ์ผ ๋์ ์ ์กฐํฉ์ ์ ํํจ -> ํ๋ง๋ ํ๊ต ์น ํ

---

### 0519 

#### ์ค๋์ ์งํ๊ณผ์ 

1. django pjt ์์ฑ
2. model ์์ฑ

#### ์ค๋์ ์๊ธฐ

1. `์งํ๊ณผ์ 2` movie ๋ฐ์ดํฐ๋ฅผ db์ ์ ์ฅํ์ง ์์ fk ์ค์ ์ ์ด๋ ค์ ๋ฐ์ 
   - ํด๊ฒฐ๋ฐฉ๋ฒ : review model์์ movie_id ํ๋๋ฅผ fk๋ก ์ํ๊ณ  int๋ก ์ค์  ํ ์ฐ๋ฆฌ๊ฐ fk์ฒ๋ผ ์ฌ์ฉํ๊ธฐ๋ก ์ ํจ

---

### 0520

#### ์ค๋์ ์งํ๊ณผ์ 

1. db์ ๋ฐ์ดํฐ ์ ์ฅ ์ฌ๋ถ ๊ฒฐ์ 

   - ๊ฒฐ์  ์ฌํญ : ์ ์ฅํ์ง ์๊ณ  ํ์ํ ๊ฒฝ์ฐ์๋ง, ํ์ ๋ฐ์ดํฐ ํธ์ถํ์ฌ ์ฌ์ฉํจ

     | ํ์ด์ง    | component      | api                                      | ๋น๊ณ                                            |
     | --------- | -------------- | ---------------------------------------- | ---------------------------------------------- |
     | ๋ฉ์ธ      | ์ ์ผ ์๋จ ์ฌ์ง | **GET**/movie/now_playing                |                                                |
     | ๋ฉ์ธ      | ์ฅ๋ฅด ๊ฐ์ ์ํ | **GET**/movie/popular                    | ๋ ๋ค์ผ๋ก ํ์ด์ง ์ ํด์ ๊ฐ์ ์ฅ๋ฅด ์ํ ๊ฐ์ ธ์ค๊ธฐ |
     | ๋ฉ์ธ      | ๋ฐฐ์ฐ ์ํ      | **GET**/person/{person_id}/movie_credits |                                                |
     | ๋ํ์ผ    | ์๊ณ ํธ         | **GET**/movie/{movie_id}/videos          |                                                |
     | ์ฐํ ๋ชฉ๋ก | ๋ํ์ผ         | GET movie/{movie_id}                     |                                                |

2. Components ์ฌํ์ธ ๋ฐ model & ERD ์์ 

   - ๋ฉ์ธ ํ์ด์ง : ๋ฒ ๋๋ ๋ทํ๋ฆญ์ค์ฒ๋ผ ํ๊ฐ์ง๋ง ๋ณด์ (์ํ ์ ๋ชฉ + ํฌ์คํฐ)

3. front(์กฐํญ์ฃผ,๊ถ๋ค์) ์ back(๊ฐ์ฅํธ)์ผ๋ก ์ญํ  ๋ถ๋ด

   - front(vue) : login / logout / signup
   - back(django) : login / logout / signup / profile(without articles)

---

**[ ์ผ๊ทผ ]**

4. front(์กฐํญ์ฃผ,๊ถ๋ค์) & back(๊ฐ์ฅํธ)
   - front : ๋ก๊ทธ์ธ ํ์ ๋ ๋ณด์ด๋ ๋ฉ์ธ ํ์ด์ง ์์ฑ [ navbar๋ง ์์ฑํ์,,, search bar ์ด์ผํ๋๊ฑฐ๋๊ณ ,,,, ]
   - back : ์ํ ๋ฆฌ๋ทฐ ์์ฑ [ ํ์ฌ ์งํ์ํฉ : ์คํจ,,,:bomb: ]

#### ์ค๋์ ์๊ธฐ

1. `์งํ๊ณผ์ 2` django์ accounts/model.py์์ genre_id๊ฐ user๋ฅผ ์์ฑํ  ๋ ์๋ฌ๊ฐ ๋ฐ์ํจ
   - ํด๊ฒฐ๋ฐฉ๋ฒ : default=0 ์์ฑ์ ์ค๋ค.
   
2. `์งํ๊ณผ์ 3` vue : login ํ๋ ๊ณผ์ ์์ ์ดํด๊ฐ ๋ถ์กฑํจ
   - ํด๊ฒฐ๋ฐฉ๋ฒ : ์ ํ๋ธ ๋ผ์ด๋ธ ๊ต์๋ ์ฝ๋๋ฅผ ์ฒ์ฒํ ์ดํด๋ด.
   
3. `์งํ๊ณผ์ 4` front : views์ `Ariticles.vue`๋ก ํ์ผ๋ช์ ์ ํ์๋, **Component name "Articles" should always be multi-word  vue/multi-word(์ปดํฌ๋ํธ ์ด๋ฆ์ ํญ์ ์ฌ๋ฌ ๋จ์ด๋ก ๋์ด์ผ ํ๋ค.)**
   - ํด๊ฒฐ๋ฐฉ๋ฒ : ArticlesView๋ก ์ด๋ฆ์ ๋ณ๊ฒฝํด์ค.
   
4. `์งํ๊ณผ์ 4` back : review ์์ฑ์ด ์๋จ,,,,,,, ์ ์๋ผ? ,,,,, ์ข ์ ๋๋ฉด ์ผ๋ง๋ ์ข๊ฒ ๋!!!!!!!

   - ํด๊ฒฐ๋ฐฉ๋ฒ : 

     ```python
     reviews = get_list_or_404(Review)
     serializer.save(user=user)
     ```

     ๋ฆฌ๋ทฐ๋ชจ๋ธ์ด ๋น์ด์์ ๋ get_list_or_404๋ฅผ ํธ์ถํ๋ ๊ฒฝ์ฐ๋ฅผ ๊ณ ๋ คํ์

     serializer ๋ฐ์ดํฐ๋ฅผ ์ ์ฅํ  ๋ movie_id๋ฅผ ๋ฐ๋ก ์ธ์๋ก ๋ฐ์ง ์๊ฒ ์์ 

---

### 0521

#### ์ค๋์ ์งํ๊ณผ์ 

##### django

- review CRUD ๊ตฌํ ๋ฐ ํ์คํธ

  ```python
      def seleted_movie(reviews, movie_pk):
          reviews_seleted_movie = []
          for review in reviews:
              if review.movie_id == movie_pk:
                  reviews_seleted_movie.append(review)
          return reviews_seleted_movie
  ```

  - movie๋ฅผ ์ฅ๊ณ ์ ์ ์ฅํ์ง ์๊ธฐ๋๋ฌธ์ ormํจ์๋ฅผ ์ฌ์ฉํ  ์ ์์
  - ๋ฐ๋ผ์ list์ ์ฒด๋ฅผ ๋ฐ๊ณ  ๊ฑฐ๊ธฐ์ movie_pk๊ฐ์ ๋ง๋ review๋ค์ Responseํด์ฃผ์ด์ผ ํจ
  - ๊ทธ์ ๋ฐ๋ฅธ ํจ์๋ฅผ ๊ตฌํ => movie_id์ movie_pk์ด ๊ฐ์ ๊ฐ๋ค์ ๋ฆฌ์คํธ์ ๋ชจ์ json์ผ๋ก ๋ณด๋ด์ค๋ค

- review_ like ๊ตฌํ

##### vue

- ArticlesView ์ MainMovieCard ์ปดํฌ๋ํธ ๊ตฌํ
  - dfs์ tmdb url ์ถ๊ฐ
  - axios ์์ฒญ์ผ๋ก nowPlaying ๋ฐ์ดํฐ๋ฅผ ๊ฐ์ ธ์์ lodash ๋๋ค์ผ๋ก ์ํ์ backdrop_path์ title๋ฅผ ๊ฐ์ ธ์์ ํ์ด์ง์ ๋ณด์ฌ์ค

#### 



### 0522

#### ์ค๋์ ์งํ๊ณผ์ 

##### django

- wish list show and save ๊ตฌํ ๋ฐ ํ์คํธ

  ```python
  user = request.user
  movie_id = request.data['movie_id']
  wish_list = WishList.objects.all().filter(user_id=user)
  
  # ์์๋ฌด๋น id ๊ฐ๋ง ๋ถ๋ฌ์ค๊ธฐ
  wish_movie_id = []
  for wish in wish_list:
  	wish_movie_id.append(wish.movie_id)
  
  # wish_movie_id๊ฐ์์ ๊ฐ์ด ์์ผ๋ฉด ==> ์ญ์ 
  if movie_id in wish_movie_id:
  	wish_object = get_object_or_404(WishList,user_id=user,movie_id=movie_id)
  	wish_object.delete()
  	serializers = WishListSerializer(wish_object)
  	return Response(serializers.data)
  
  else:
      ์์ผ๋ฉด ์ ์ฅ
  
  ```

- ์ค๋์ ์๊ธฐ

  - movie_id๊ฐ์ request๋ก ๋ฐ์์ค๊ธฐ ๋๋ฌธ์ ๋ฐ์ดํฐ์์ dictionary๋ก ๋ฐ์์์ผ ํจ
  - wish_list๋ฅผ ๋ฐ์์ฌ๋ get_list_or_404๋ก ๋ฐ์์ค์ง ๋ชปํจ
    - ์๋ํ๋ฉด ์๋ก์ด ์ ์ ๊ฐ ์ฐ์ ๋๋ ์๋ ์๋ฌด๊ฒ๋ ์์์์ 404์๋ฌ๊ฐ ๋จ๊ฒ ๋๋ค
    - ์ด๋ ๊ฒ ๋๋ฉด ์๋๊ธฐ ๋๋ฌธ์ ๋น๋ฆฌ์คํธ๋ก ๋ง๋ฌด๋ฆฌ๋ฅผ ์์ผ์ค๋ค
  - for๋ฌธ์ ์ด์ฉํ์ฌ movie id ๊ฐ๋ง ๋ฐ์์์ ๋น๊ตํ๋ค.
  - if ๋ฌธ์ ์ฌ์ฉํด์ ๋ฆฌ์คํธ์ ์๋ id๊ฐ์ ์กด์ฌ ์ฌ๋ถ๋ฅผ ๋น๊ตํ๋ค.
    - ๋ฆฌ์คํธ๋ฅผ ์จ๋ ๋๋ ์ด์  : ํ์ ์ ๊ฐ ์๋ฌด๋ฆฌ ๋ง์ ์ํ๋ฅผ ๋๋ฌ๋ ์ผ๋ง ์๋  ๊ฒ์ด๊ธฐ ๋๋ฌธ์

##### vue

- ๋ฐ์ดํฐ ํ๋ฆ ๋ณ๊ฒฝ
  MainMovieCard ์ปดํฌ๋ํธ์์ axios ์์ฒญ์ ํตํด ๋ฐ์ดํฐ๋ฅผ ๊ฐ์ ธ์ค๋๊ฑธ ๋ถ๋ชจ ์ปดํฌ๋ํธ์ธ ArticleView ์ปดํฌ๋ํธ์์ ๊ฐ์ ธ์์ props๋ก ์ ๋ฌํด์ฃผ๋ ๋ฐฉ์์ผ๋ก ๋ณ๊ฒฝ

- ArticlesVies.vue์ getNowPlayingMovie() ๋ฉ์๋ ๋ถ๋ฆฌ
  ๊ธฐ์กด์ api์์ฒญ์ ๋ณด๋ด์ ํ์ฌ ์์์ค์ธ ์ํ๋ฅผ ๊ฐ์ ธ์ค๊ณ  ๊ทธ ์์์ ๋ ๋ค์ผ๋ก ๋ฐ์ดํฐ ํ๋๋ฅผ ์ ์ฅํ๋ getNowPlayingMovie() ๋ฅผ 
  ํ์ฌ ์์์ค์ธ ์ํ ๋ฐ์ดํฐ๋ฅผ ์ ์ฅํ๋ getNowPlayingMovieList()์ ๊ทธ ์์์ ๋ ๋ค ์ํ๋ฅผ ์ ์ฅํ๋ getRandMovieData()๋ก ๋ถ๋ฆฌํจ

- ์ค๋์ ์๊ธฐ
  created ๋ผ์ดํ ์ธ์ดํด ํ์ด ๋๊ธฐ์ ์ผ๋ก ์ฝ๋๊ฐ ์คํ๋์ง ์๋๊ฑฐ ๊ฐ๋ค,,, ํ์ฌ ์์์ค์ธ ์ํ ์ ๋ณด๋ฅผ ๋จผ์  ๊ฐ์ ธ์ค๊ณ  ๋๋ค ๋ฌด๋น๋ฅผ ๊ฐ์ ธ์์ผ ๋๋๋ฐ ๊ทธ๊ฒ ์๋ผ

  ```js
  created(){
      this.getNowPlayingMovieList()
      this.getRandMovieData()
    },
  mounted() {
      this.getRandMovieData()
    },
  ```

  ์ด๋ฐ์์ผ๋ก ์ง๋ฉด ์๋ผ ๊ทธ๋์ 

  ```vue
  <template>
    <div>
      {{getRandMovieData()}}
      <MainMovieCard :backdrop-path="mainMovieBackdropPath" :title="mainMovietitle"></MainMovieCard>
    </div>
  </template>
  ```

  ์ผ๋จ ์์๋ก ์ด๋ ๊ฒ ์คํ์์ผ๋จ์ต๋๋ค,,



### 0523

#### ์ค๋์ ์งํ๊ณผ์ 

##### django

- wish list saveํ ๋ ๋ฐํ ๊ฐ์ด object์์ list๊ฐ์ผ๋ก ๋ณ๊ฒฝ
- review๋ฅผ ๋ฌ๋ ํ์ํ์ ํ๋์ review๋ง ์ธ์ ์๋๋ก ๋ณ๊ฒฝ
- review list์ ํ์  ์ถ๊ฐ
- ํ๋กํ ์ฐฝ์ ์ข์ํ๋ ๋ฆฌ๋ทฐ, ์ข์ํ๋ ๋ฆฌ๋ทฐ์ ๊ฐ์, ๋ด๊ฐ ์์ฑํ ๋ฆฌ๋ทฐ์ ๊ฐ์ ์ถ๊ฐ

**review list**

```python
# movie_id ๋ชจ์
review_movie_list = []
for review_ojt in review_list:
    review_movie_list.append(review_ojt.movie_id)
        
# ์์ฑ๋์ด ์์์ data๋ณด๋
if movie_pk in review_movie_list:
    data = {
        'exist':f'์ด๋ฏธ ์์ฑํ์จ์ต๋๋ค'
    }
	return Response(data, status=status.HTTP_201_CREATED)

# ์์ฑ ์๋์ด ์์์ ์ ์ฅ
else:
	serializer = ReviewSerializer(data=request.data)
	if serializer.is_valid(raise_exception=True):
		serializer.save(user=user)
		reviews = get_list_or_404(Review)
		reviews_selected_movie = seleted_movie(reviews, movie_pk)
		serializer = ReviewSerializer(reviews, many=True)
		return Response(serializer.data, status=status.HTTP_201_CREATED)
```

- movie id ๊ฐ์ ๋ชจ์๋๊ณ  for๋ฌธ์ ํตํด์ movie_pk๊ฐ ์๋์ง ํ์ธ
  - ์์ ==> ์ด๋ฏธ ์์ฑ ํ๋ค๋ data๋ฅผ ๋ณด๋ด์ค๋ค
  - ์์ ==> review list๋ก ๋ฐ์์ ๋ณด๋ด์ค๋ค

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

- ์ ํ๋ movie๋ค์ list์ ๋ด์ ํ๊ท ์ ๊ตฌํด์ค๋ค.



**like_review, review_count in profile**

```python
like_review = ReviewSerializer(many=True, read_only=True)
review_count = serializers.IntegerField(source='review_set.count',read_only=True)
```

- ReviewSerializer๋ ์๋ก calss๋ฅผ ๋ง๋ค์ด์ ์ปค์คํ ํด์ค

- ProfileSerializer์ ์ด ๋ ๊ฐ๋ค์ ์ถ๊ฐ ํด์ค๋ค



**genre_save**

```python
serializers = UserSerializer(instance=user, data=request.data)
```

- ์๋ฐ์ดํธ ๊ตฌํํ ๋์ ๋ง์ฐฌ๊ฐ๋ก instance=user๋ฅผ ๋ฃ์์ผ๋ก์ ๊ธฐ์กด๊ฒ๋ค์ ๊ฐ์ ธ์ค๊ณ  ์๋ฐ์ดํธ๋ง ์ํจ๋ค.



##### vue

- ๋ก๊ทธ์ธ ์์๋ 8080/ ๋ก ์ ์ํ์ ๋ ๋ก๊ทธ์ธ ํ์ด์ง๊ฐ ๋ ๋๋ง ๋๋ ๋ฌธ์  ํด๊ฒฐ
  MainUnlogin.vue ์ created ๋ผ์ดํ์ฌ์ดํด ํ์ ๋ก๊ทธ์ธ์ articles๋ก ๋ผ์ฐํ ๋๋ ๋ฉ์๋๋ฅผ ๊ฑธ์ด๋ 
  
- ๋น๋ก๊ทธ์ธ ์ /articles๋ก ์ ์๋๋ ๋ฌธ์  ํด๊ฒฐ

- ๋ฉ์ธ ํ์ด์ง

  - ์ฅ๋ฅด ์ํ ์ถ์ฒ ๋ชฉ๋ก ์์ฑ
  - ๋ฐฐ์ฐ ์ํ ์ถ์ฒ ๋ชฉ๋ก ์์ฑ
  - ํ์ฌ ์์์ค ์ํ ์ถ์ฒ ๋ชฉ๋ก ์์ฑ

- ๋ฌด๋น ๋ํ์ผ ํ์ด์ง ์ถ๊ฐ

  - get Detail api๋ก ์ํ ์ ๋ณด ๊ฐ์ ธ์์ ๋๋๋ง

  - ๋ฆฌ๋ทฐ ๋ฆฌ์คํธ django์์ ๊ฐ์ ธ์์ ๋๋๋ง
  - ๋ฆฌ๋ทฐ ์ข์์ ๋ฒํผ ์ถ๊ฐ 

- ์ฅ๋ฅด์๋์ปต ํฌ์คํฐ ์ถ๊ฐ(๋ฉ๋ฐ์)

### 0524

#### ์ค๋์ ์งํ๊ณผ์ 

##### django

- db์ ์ฅ
  - ์๊ธฐ : settings.py ์ ์๋ก ๋ง๋  movie์ฑ ๋ฑ๋ก์ ์ํ์.

##### vue

- ๊ธฐ๋ฅ ๊ตฌํ

  - ์ํ ์์ธ ํ์ด์ง์ ๋ฆฌ๋ทฐ
    - ๋ฆฌ๋ทฐ ํผ ์์ฑ
    - ๋ฆฌ๋ทฐ ์์ 
    - ๋ฆฌ๋ทฐ ์ญ์ 

  - ์ํ ์ฐ

  - ์์๋ฆฌ์คํธ ํ์ด์ง ์์ฑ

  - ์ฐ ๊ตฌํ 

  - ํ๋กํํ์ด์ง 

  - ๋ฆฌ๋ทฐ ์์ธํ์ด์ง 

  - ๋ฆฌ๋ทฐ๋ฆฌ์คํธ ๋ฐ์ดํฐ ์์ ,์ญ์ ,์์ฑ

  - ๊ฒ์

  - ๊ฒ์ ๊ฒฐ๊ณผํ์ด์ง

  - ์ธ๋ฌผ ์ปดํฌ๋ํธ

  - ์ํ ์ปดํฌ๋ํธ

- ๋ฒ๊ทธ ์์ 
  - ๋นจ๊ฐ์ ์๋ฌ
  - ์ฐ ํธ๋ฃจํ์ค
  - ๋ฐ์ดํฐ ํผ ์์ 
  - ์ฌ์ง์๋ ๋ฐ์ดํฐ ํธ๋ค๋ง
  - ํ๋กํ์์ ๋๊ธ ์์ฑ์ ๋ณด๊ธฐ 
  - ๋ฆฌ๋ทฐ์ ์ํ ์ ๋ชฉ ๋ณด์ด๊ธฐ

### 0525

##### vue

- ๊ธฐ๋ฅ ๊ตฌํ
  - ์ธ๋ฌผ์์ธ ํ์ด์ง
  - ๊ฒ์์์ ํฌ์คํฐ ์๋ ๋ฐ์ดํฐ ๋๋๋ง์ํจ
  - ํํธ ์ฐํ๊ฑฐ๋ก ํ์๋๋ ์๋ผ:?
  - ์ฌ๋ ๋ํ์ผ ๊ฐ์ ธ์ค๊ธฐ
  - ์ฅ๋ฅด์๋์ปต
  - ํ๋กํํ์ด์ง์ ์ฅ๋ฅด ์ ํ๊ธฐ๋ฅ ์ถ๊ฐ
  - ์ฐํ ๋ชฉ๋ก์์ ๋ฐฐ์ฐ ์ ๋ณด ๊ฐ์ ธ์ค๊ธฐ
  - ๋ํ์ผ ํ์ด์ง์ ์ ์  ํ์ ๋ ๋ฃ์ด์ฃผ๊ธฐ
  - ์ธ๋ฌผ ๋ฏธ๋ฆฌ๋ณด๊ธฐ์ ์ํ 3๊ฐ ์ถ๊ฐ
  - ์ธ๋ฌผ ๋ํ์ผ api์์ ์ธ๋ฌผ ์ ๋ณด ๊ฐ์ ธ์ค๊ธฐ
  - ํ๋กํํ์ด์ง ์ฅ๋ฅด ์ ํ์ ๋ด ์ฅ๋ฅด ๋ณด์ฌ์ฃผ๊ธฐ
  - ๋๊ธ ์์  ๋ฒํผ 
  - ๋ฐฐ์ฐ ์ ๋ณด ๊ฐ์ ธ์ฌ๋ ๋๋ค์ผ๋ก ๊ฐ์ ธ์ค๊ธฐ
  - ์ฅ๋ฅด์๋์ปต ๊ฒฐ๊ณผํ์ด์ง์ ๊ฐ์ ์ฅ๋ฅด ์ํ ๊ฐ์ ธ์ค๊ธฐ
- ๋ฒ๊ทธ ์์ 
  - ๋ค๋ฅธ ์ฌ๋์ด ์ด ๋๊ธ ๋ด๊ฐ ์์ 

### 0526

##### vue

- ๊ธฐ๋ฅ ๊ตฌํ
  - ์ฅ๋ฅด ์๋์ปต ์ ํ์ ํ๋ค๋ฆฌ๋ css
  - ์์ํ์ด์ง๋ก ๊ฐ์ผ๋๋๋ฐ ๋ก๊ทธ์ธํ์ด์ง๋ก๊ฐ
  - ๋ฆฌ๋ทฐ์นด๋ ์ฌ์ง ๋๋ฅด๋ฉด ์ํ ๋ํ์ผ๋ก ์ด๋
  - ์ฐํ ๋ชฉ๋ก ํธ๋ฒ์ ๋ฐ์ดํฐ 
  - ์ธ๋ฌผ์์ธํ์ด์ง,์ฅ๋ฅด์๋์ปต ๊ฐ๋ก์คํฌ๋กคํ๊ณ  ์คํฌ๋กค ์์ ๋ณ๊ฒฝ
  - ๋ก๊ทธ์์ํ์ ๋ ๋ฉ์ธ์ผ๋ก๊ฐ๊ธฐ
- ๋ฆฌํฉํ ๋ง
  - ์ธ๋ฌผ ์ ๋ณด data->vuex
- ๋ฒ๊ทธ ์์ 
  - ๋ก๊ทธ์ธ ํ๊ณ  ๋ค์ ๋ก๊ทธ์ธ ํ์ด์ง ์ ์
  - ๋ก๊ทธ์ธ ์คํจ์ ํธ๋ค๋ง
  - ํ์๊ฐ์ ์คํจ์ ํธ๋ค๋ง
  - ๋ฉ์ธํ์ด์ง ์๋ก๊ณ ์นจ์ ์ฅ๋ฅด ๋ฐ์ดํฐ ๋ชป๋ถ๋ฌ์ด vuex-persistedstate
  - ์ฌ๋ ๋ํ์ผ ํ์ด์ง ์ ๋ณด ์๋ชป๊ฐ์ ธ์ด
  - ๋ชจ๋ฌ ๋๊ฐ ๋ ๋ฉ์ถค
  - ์ฅ๋ฅด์๋์ปต ๊ฒฐ๊ณผ์์ '๊ฐ'์ด ๋ธ




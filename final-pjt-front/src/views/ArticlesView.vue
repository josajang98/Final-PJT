<template>
  <div>
    <MainMovieCard 
      :backdrop-path="mainMovieBackdropPath" 
      :title="mainMovietitle" 
      :movie-id="mainMovieId"
      >
    </MainMovieCard>

    <!-- 장르 영화 추천 목록 -->
    <p>{{username}}님이 좋아하는 영화</p>
    <div class="container">
      <div class="row bg-white bg-opacity-10 justify-content-center">
        <MovieCard
          v-for="movie in userLikeGenreMovieList"
          :movie-id="movie.id"
          :movie-poster-path="movie.poster_path"
          :key="movie.id"
          class="col-lg-2 col-md-3 col-sm-4"
        ></MovieCard>
      </div>
    </div>
    <!-- 배우 영화 추천 목록 -->
    <p>{{userLikeActor}} 배우님의 영화</p>
    <div class="container">
      <div class="row bg-white bg-opacity-10 justify-content-center">
        <MovieCard
          v-for="movie in userLikeActorMovieList"
          :movie-id="movie.id"
          :movie-poster-path="movie.poster_path"
          :key="movie.id"
          class="col-lg-2 col-md-3 col-sm-4"
        ></MovieCard>
      </div>
    </div>
    <!-- 현재 상영중 영화 추천 목록 -->
    <p>현재 상영중인 영화</p>
    <div class="container">
      <div class="row bg-white bg-opacity-10 justify-content-center">
        <MovieCard
          v-for="movie in nowPlayingMovieList"
          :movie-id="movie.id"
          :movie-poster-path="movie.poster_path"
          :key="movie.id"
          class="col-lg-2 col-md-3 col-sm-4"
        ></MovieCard>
      </div>
    </div>

  </div>
</template>

<script>
import MainMovieCard from '@/components/MainMovieCard.vue'
import MovieCard from '@/components/MovieCard.vue'
import axios from 'axios'
import drf from '@/api/drf'
import _ from 'lodash'
import { mapGetters } from 'vuex';
import router from '@/router'

const imgUrl='https://image.tmdb.org/t/p/w500/'
const count = 4

export default {
  
  name: 'ArticlesView',

  data() {
    return {
      nowPlayingMovieList:'',
      mainMovieBackdropPath:'',
      mainMovietitle:'',
      mainMovieId:0,

      // 사용자의 장르 영화
      userLikeGenreId:'18',
      // 사용자가 찜한 목록 배우
      userLikeActor:'',
      userLikeActorId:91225,
      

      // 추천 영화 리스트
      userLikeGenreMovieList:[],
      userLikeActorMovieList:[],
    };
  },
  created(){
    this.routingArticles(),
    this.getNowPlayingMovieList(),
    this.getUserLikeGenreMovieList()
    this.getUserLikeActorMovieList()
  },
  components:{
    MainMovieCard,
    MovieCard
},
  computed: {
    ...mapGetters(['isLoggedIn','currentUser']),
    username() {
      return this.currentUser.username ? this.currentUser.username : 'guest'
    },
  },
  mounted() {

  },
  methods: {
    
    /**
     * 현재 상영중인 데이터 20개를 가져와서 랜덤 데이터 하나 뽑아서 MainMovieCard에 넘겨주고 
     * 카운트 개수만 큼 잘라서 this.nowPlayingMovieList에 저장
     */
    async getNowPlayingMovieList(){
      const response=await axios.get(drf.tmdb.nowPlaying())
      
      
      this.nowPlayingMovieList=response.data.results
      this.getRandMovieData()
      const indexList = _.sampleSize(_.range(0,19),count)
      const movieListSlice=[]

      indexList.forEach(el=>{
        movieListSlice.push(response.data.results[el])
      })
      this.nowPlayingMovieList=movieListSlice
      // console.log(this.nowPlayingMovieList)
        
    },

    /**
     * 상영중인 영화 데이터 중 하나를 렌덤으로 골라서 데이터 저장
     */
    getRandMovieData(){
      const randNum=_.random(0,19)

      const randMovie=this.nowPlayingMovieList[randNum]
      // console.log(randMovie)
      const backdropPath=imgUrl+randMovie.backdrop_path
      const title=randMovie.title
      this.mainMovieBackdropPath=backdropPath
      this.mainMovietitle=title
      this.mainMovieId=randMovie.id
    },


  
    routingArticles(){
      if (this.isLoggedIn === false)
        router.push({name:'home'})
    },

    /**
     * 유저 장르id가 있다면 랜덤 페이지로 popular요청을 보내서 같은 장르의 영화데이터를 count만큼 저장 
     */
    async getUserLikeGenreMovieList(){
      if (this.userLikeGenreId===''){
        return
      }
      
      const indexList = _.sampleSize(_.range(1,500),500)
      let idx = 0
      let cnt = 0
      while (cnt < count){
        const response = await axios.get(drf.tmdb.popular(indexList[idx++]))
        
        response.data.results.forEach(element => {
          if (cnt >= count) return false

          // 포스터 패스 없을 시 continue
          if(!element.poster_path) return true

          element.genre_ids.forEach(id => {
            if (id == this.userLikeGenreId){
              this.userLikeGenreMovieList.push(element)
              cnt++
              return false
            }
          })
        })
      }
    },

    /**
     * 배우id가 있다면 person요청으로 데이터를 가져온 후 count만큼 랜덤으로 저장
     */
    async getUserLikeActorMovieList(){
      if (this.userLikeActorId===''){
        return
      }
      const response=await axios.get(drf.tmdb.person(this.userLikeActorId))
      const indexList = _.sampleSize(_.range(0,response.data.cast.length),count)
      indexList.forEach(el=>{
        // 포스터패스가 있을 시에만 추가
        if(response.data.cast[el].poster_path)
          this.userLikeActorMovieList.push(response.data.cast[el])
      })
    }
  },

};
</script>

<style lang="scss" scoped>

</style>
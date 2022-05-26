<template>
  <div class="font">
    <div class="video-background">
      <div class="video-foreground">
        <VideoDetail
            :selected-video="selectedVideo"
          >
        </VideoDetail>
      </div>
    </div>
    <!-- <MainMovieCard 
      :backdrop-path="mainMovieBackdropPath" 
      :title="mainMovietitle" 
      :movie-id="mainMovieId"
      >
    </MainMovieCard> -->

    <div class="con">
      <!-- 장르 영화 추천 목록 -->
      <p v-if="userLikeGenreId">{{username}}님이 좋아하는 영화</p>
      <div class="container">
        <div class="row justify-content-center ">
          <div class="slider">
            <div class="slides">
              <MovieCard
                v-for="movie in userLikeGenreMovieList"
                :movie="movie"
                :key="movie.id"
                class="col-lg-2 col-md-3 col-sm-4"
              ></MovieCard>
            </div>
          </div>          
          
        </div>
      </div>
      <!-- 배우 영화 추천 목록 -->
      <p v-if="userLikeActorId">{{userLikeActor}} 배우님의 영화</p>
      <div class="container gallerylist">
        <div class="row justify-content-center ">
          <div class="slider">
            <div class="slides">
              <MovieCard
                v-for="movie in userLikeActorMovieList"
                :movie="movie"
                :key="movie.id"
                class="col-lg-2 col-md-3 col-sm-4"
              ></MovieCard>
            </div>
          </div>   
          
        </div>
      </div>
      <!-- 현재 상영중 영화 추천 목록 -->
      <p>현재 상영중인 영화</p>
      <div class="container">
        <div class="row justify-content-center">
          <div class="slider">
            <div class="slides">
              <MovieCard
                v-for="movie in nowPlayingMovieList"
                :movie="movie"
                :key="movie.id"
                class="col-lg-2 col-md-3 col-sm-4"
              ></MovieCard>
            </div>
          </div>  
        </div>
      </div>
    </div>
    

  </div>
</template>

<script>
// import MainMovieCard from '@/components/MainMovieCard.vue'
import MovieCard from '@/components/MovieCard.vue'
import axios from 'axios'
import drf from '@/api/drf'
import _ from 'lodash'
import { mapGetters } from 'vuex';
import router from '@/router'

const imgUrl='https://image.tmdb.org/t/p/w500/'
const count = 20

// youtube
const API_URL = 'https://www.googleapis.com/youtube/v3/search'
const API_KEY = 'AIzaSyCAfBdFTiGwvu7XJdMJTFZzfczyvErmKgg'
import VideoDetail from '@/components/VideoDetail.vue'

export default {
  
  name: 'ArticlesView',

  data() {
    return {
      nowPlayingMovieList:'',
      mainMovieBackdropPath:'',
      mainMovietitle:'',
      mainMovieId:0,

      // 사용자의 장르 영화
      userLikeGenreId:'',
      // 사용자가 찜한 목록 배우
      userLikeActor:'',
      userLikeActorId:'',
      
      // 추천 영화 리스트
      userLikeGenreMovieList:[],
      userLikeActorMovieList:[],

      // youtube
      inputValue:null,
      videos:[],
      selectedVideo: null,
    };
  },
  created(){
    this.getUserProfile()
    this.getLikeActor()
    
    this.routingArticles()
    this.getNowPlayingMovieList()

  },
  components:{
    // MainMovieCard,
    MovieCard,
    VideoDetail
  },
  computed: {
    ...mapGetters(['isLoggedIn','currentUser','authHeader']),
    username() {
      return this.currentUser.username ? this.currentUser.username : 'guest'
    },
    
  },

  methods: {
    slide(idx){
      return `slide-${idx+1}`
    },
    shopSlide(idx){
      return `#slide-${idx+1}`
    },
    async getLikeActor(){
      const response1=await axios({
        url: drf.accounts.wishList(),
        method: 'get',
        headers: this.authHeader,
      })
      const wishList=response1.data
      const randNum=_.random(0,wishList.length-1)
      const randMovieData=wishList[randNum]

      const response2=await axios({
        url: drf.tmdb.credits(randMovieData.movie_id),
        method: 'get',
      })

      const casts=response2.data.cast
      const randCastsIndex=_.random(0,3)
      this.userLikeActor=casts[randCastsIndex].name
      this.userLikeActorId=casts[randCastsIndex].id
      this.getUserLikeActorMovieList()
    },

    async getUserProfile(){

      const response=await axios({
        url: drf.accounts.getProfile(this.currentUser.username),
        method: 'get',
        headers: this.authHeader,
      })
      this.userLikeGenreId=response.data.genre_id
      
      this.getUserLikeGenreMovieList()
    },
    /**
     * 현재 상영중인 데이터 20개를 가져와서 랜덤 데이터 하나 뽑아서 MainMovieCard에 넘겨주고 
     * 카운트 개수만 큼 잘라서 this.nowPlayingMovieList에 저장
     */
    async getNowPlayingMovieList(){

      const response=await axios.get(drf.tmdb.nowPlaying())
      
      
      this.nowPlayingMovieList=response.data.results
      this.getRandMovieData()
      this.getTearVideo(this.mainMovietitle)
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
      let cnt=0
      const response=await axios.get(drf.tmdb.person(this.userLikeActorId))
      const indexList = _.sampleSize(_.range(0,response.data.cast.length),response.data.cast.length-1)
      indexList.forEach(el=>{
        if(count==cnt) return true
        // 포스터패스가 있을 시에만 추가
        if(response.data.cast[el].poster_path){
          this.userLikeActorMovieList.push(response.data.cast[el])
          cnt++
        }   
      })
    },
    // youtube
    getTearVideo(mainMovietitle){
      this.inputValue = mainMovietitle+'예고편'
      const params = {
        key:API_KEY,
        part:'snippet',
        type:'video',
        q:this.inputValue,
      }

      axios({
        method: 'get',
        url: API_URL,
        params,
      })
        .then(res =>{
          this.videos = res.data.items
          this.selectedVideo = this.videos[0]
        })
        .catch(err=>{
          console.log(err)
        })
    },
    onSelectVideo(video){
      this.selectedVideo = video
    }
  },

};
</script>

<style lang="scss" scoped>
.con{
  width: 100%;
  position:relative;
  top:90vh;
}
.font {
  font-size: 4vw;
}
.video-background {
  background: #000;
  position: fixed;
  top: 0; right: 0; bottom: 0; left: 0;
  z-index: -99;
}
.video-foreground,
.video-background iframe {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  pointer-events: none;
}
#vidtop-content {
    top: 0;
    color: #fff;
}
.vid-info { position: absolute; top: 0; right: 0; width: 33%; background: rgba(0,0,0,0.3); color: #fff; padding: 1rem; font-family: Avenir, Helvetica, sans-serif; }
.vid-info h1 { font-size: 2rem; font-weight: 700; margin-top: 0; line-height: 1.2; }
.vid-info a { display: block; color: #fff; text-decoration: none; background: rgba(0,0,0,0.5); transition: .6s background; border-bottom: none; margin: 1rem auto; text-align: center; }
@media (min-aspect-ratio: 16/9) {
  .video-foreground { height: 300%; top: -100%; }
}
@media (max-aspect-ratio: 16/9) {
  .video-foreground { width: 300%; left: -100%; }
}
@media all and (max-width: 600px) {
.vid-info { width: 50%; padding: .5rem; }
.vid-info h1 { margin-bottom: .2rem; }
}
@media all and (max-width: 500px) {
.vid-info .acronym { display: none; }
}


* {
    box-sizing: border-box;
  }
  // 슬라이더
  .slider {
    width: 100vw;
    text-align: center;
    border-radius: 10px;
    overflow: hidden;
  }
  
  .slides {
    display: flex;
    overflow-x: auto;
    /* overflow: hidden; */
    scroll-snap-type: x mandatory;
    scroll-behavior: smooth;
    -webkit-overflow-scrolling: touch;
  }
  .slides::-webkit-scrollbar {
    width: 10px;
    height: 10px;
  }
  .slides::-webkit-scrollbar-thumb {
    background: #ffffff50;
    border-radius: 10px;
  }
  .slides::-webkit-scrollbar-track {
    background: transparent;
  }
  .slides > div {
    scroll-snap-align: start;
    flex-shrink: 0;
    margin-right: 50px;
    border-radius: 10px;
    overflow: hidden;

    transform-origin: center center;
    transform: scale(1);
    transition: transform 0.5s;
    position: relative;
    
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 100px;
  }
  
  .author-info {
    background: rgba(0, 0, 0, 0.75);
    color: white;
    padding: 0.75rem;
    text-align: center;
    position: absolute;
    bottom: 0;
    left: 0;
    width: 100%;
    margin: 0;
  }
  .author-info a {
    color: white;
  }

  
</style>
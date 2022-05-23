<template>
  <div>
    <MainMovieCard :backdrop-path="mainMovieBackdropPath" :title="mainMovietitle"></MainMovieCard>
    <MovieCard
      v-for="movie in userLikeGenreMovieList"
      :movie="movie"
      :key="movie.id"
    ></MovieCard>
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
export default {
  
  name: 'ArticlesView',

  data() {
    return {
      nowPlayingMovieList:'',
      mainMovieBackdropPath:'',
      mainMovietitle:'',

      // 사용자의 장르 영화
      userLikeGenreId:'',
      // 사용자가 찜한 목록 배우
      userLikeActor:'',
      userLikeActorId:572225,
      
      userLikeGenreMovieList:[],
      userLikeActorMovieList:[],
    };
  },
  created(){
    this.routingArticles(),
    this.getNowPlayingMovieList(),
    this.getPopularMovieList(),
    this.getUserLikeGenreMovieList(),
    this.getUserLikeActorMovieList()
  },
  components:{
    MainMovieCard,
    MovieCard
},
  computed: {
    ...mapGetters(['isLoggedIn'])
  },
  mounted() {
    // this.getRandMovieData()
  },
  methods: {
    getNowPlayingMovieList(){
      axios({
        url: drf.tmdb.nowPlaying(),
        method: 'get',
      })
        .then(res=> {
          this.nowPlayingMovieList=res.data.results
          this.getRandMovieData()
        })
        .catch(err => {
          console.error(err.response.data)
        })
    },
    getGenreMovie(){
      axios({
        url: drf.tmdb.nowPlaying(),
        method: 'get',
      })
        .then(res=> {
          res
        })
        .catch(err => {
          console.error(err.response.data)
        })
    },
    getRandMovieData(){
      const randNum=_.random(0,19)

      const randMovie=this.nowPlayingMovieList[randNum]
      // console.log(randMovie)
      const backdropPath=imgUrl+randMovie.backdrop_path
      const title=randMovie.title
      this.mainMovieBackdropPath=backdropPath
      this.mainMovietitle=title
    },
    getPopularMovieList(){
      axios({
        url: drf.tmdb.popular(),
        method: 'get',
      })
        .then(res=> {
          this.popularMovieList=res.data.results
          // console.log(this.popularMovieList)
        })
        .catch(err => {
          console.error(err.response.data)
        })
    },
    routingArticles(){
      if (this.isLoggedIn === false)
        router.push({name:'home'})
    },
    // 좋아하는 장르 영화
    async getUserLikeGenreMovieList(){
      if (this.userLikeGenreId===''){
        return
      }
      const count = 4
      const indexList = _.sampleSize(_.range(1,500),500)
      let idx = 0
      let cnt = 0
      while (cnt < count){
        const response = await axios.get(drf.tmdb.popular(indexList[idx++]))
        console.log(response.data)
        response.data.results.forEach(element => {
          if (cnt >= count){
            return false
          }
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
    // 장르 id 없을때,
    // 배우
    getUserLikeActorMovieList(){
      axios({
        url: drf.tmdb.person('63436'),
        method: 'get',
      })
        .then(res=>{
          console.log(res)
        })
      
    }
  },

};
</script>

<style lang="scss" scoped>

</style>
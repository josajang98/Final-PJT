<template>
  <div>
    <MainMovieCard :backdrop-path="mainMovieBackdropPath" :title="mainMovietitle"></MainMovieCard>
  </div>
</template>

<script>
import MainMovieCard from '@/components/MainMovieCard.vue'
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
      userLikeGenreId:'',
      userLikeActor:'',
      popularMovieList:'',
    };
  },
  created(){
    this.routingArticles(),
    this.getNowPlayingMovieList(),
    this.getPopularMovieList()
  },
  components:{
    MainMovieCard,
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
          console.log(this.popularMovieList)
        })
        .catch(err => {
          console.error(err.response.data)
        })
    },
    routingArticles(){
      if (this.isLoggedIn === false)
        router.push({name:'home'})
    }
  },

};
</script>

<style lang="scss" scoped>

</style>
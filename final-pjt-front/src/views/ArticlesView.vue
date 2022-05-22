<template>
  <div>
    {{getRandMovieData()}}
    <MainMovieCard :backdrop-path="mainMovieBackdropPath" :title="mainMovietitle"></MainMovieCard>
  </div>
</template>

<script>
import MainMovieCard from '@/components/MainMovieCard.vue'
import axios from 'axios'
import drf from '@/api/drf'
import _ from 'lodash'

const imgUrl='https://image.tmdb.org/t/p/w500/'
export default {
  
  name: 'ArticlesView',

  data() {
    return {
      nowPlayingMovieList:'',
      mainMovieBackdropPath:'',
      mainMovietitle:'',

    };
  },
  created(){
    this.getNowPlayingMovieList()
    
  },
  components:{
    MainMovieCard,
  },
  mounted() {
    this.getRandMovieData()
  },

  methods: {
    getNowPlayingMovieList(){
      axios({
        url: drf.tmdb.nowPlaying(),
        method: 'get',
      })
        .then(res=> {
          this.nowPlayingMovieList=res.data.results

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
      console.log(randMovie)
      const backdropPath=imgUrl+randMovie.backdrop_path
      const title=randMovie.title
      this.mainMovieBackdropPath=backdropPath
      this.mainMovietitle=title
    }
  },

};
</script>

<style lang="scss" scoped>

</style>
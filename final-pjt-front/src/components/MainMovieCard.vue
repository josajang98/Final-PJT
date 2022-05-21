<template>
  <div>
    <img :src="backdropPath" alt="">
    {{title}}
  </div>
</template>

<script>
import axios from 'axios'
import drf from '@/api/drf'
import _ from 'lodash'
export default {
  name: 'MainMovieCard',

  data() {
    return {
      backdropPath:'',
      title:'',
    };
  },
  created(){
    this.getMainMovie()
  },
  mounted() {
    
  },

  methods: {
    getMainMovie(){
      axios({
        url: drf.tmdb.nowPlaying(),
        method: 'get',
      })
        .then(res=> {
          
          const randIdx=_.random(0,19)
          
          this.backdropPath='https://image.tmdb.org/t/p/w500/'+res.data.results[randIdx].backdrop_path
          this.title=res.data.results[randIdx].title
          console.log(this)
        })
        // .catch(err => {
        //   console.error(err.response.data)
        //   commit('SET_AUTH_ERROR', err.response.data)
        // })
    }
  },
};
</script>

<style lang="scss" scoped>

</style>
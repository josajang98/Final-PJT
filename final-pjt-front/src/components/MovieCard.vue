<template>
  <div>
    <img @click="routingDetail(movieId)" :src="posterPath" alt="">
  </div>
</template>

<script>
import router from '@/router'
const imgUrl='https://image.tmdb.org/t/p/w500/'
export default {
  name: 'MovieCard',
  props:{
    movieId : String,
    moviePosterPath:String
  },
  computed:{
    posterPath(){
      return imgUrl+this.moviePosterPath
    }
  },
  methods:{
    routingDetail(movieId){
      router.push({
        name:'detail',
        params:{movie_id:movieId}
        })
    },
  }

}
</script>

<style>

</style>
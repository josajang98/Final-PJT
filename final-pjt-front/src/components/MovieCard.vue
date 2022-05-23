<template>
  <div>
    <img @click="routingDetail(movie.id)" :src="posterPath" alt="">
  </div>
</template>

<script>
import router from '@/router'
const imgUrl='https://image.tmdb.org/t/p/w500/'
export default {
  name: 'MovieCard',
  props:{
    movie : Object,
  },
  computed:{
    posterPath(){
      return imgUrl+this.movie.poster_path
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
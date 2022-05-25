<template>
  <div v-if="moviePosterPath">
    <img @click="routingDetail(movieId)" :src="posterPath" alt="">
  </div>
</template>

<script>
import router from '@/router'
const imgUrl='https://image.tmdb.org/t/p/w500/'
export default {
  name: 'MovieCard',
  props:{
    movieId:Number,
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

<style  lang="scss" scoped>
img {
    max-width: 100%;
    height: auto;
}

</style>
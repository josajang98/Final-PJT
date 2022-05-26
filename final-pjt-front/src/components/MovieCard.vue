<template>
  <div v-if="movie.poster_path">
    <img @click="routingDetail()" :src="posterPath" alt="">
  </div>
</template>

<script>
import router from '@/router'
const imgUrl='https://image.tmdb.org/t/p/w500/'
export default {
  name: 'MovieCard',
  props:{
    movie:Object,
  },
  computed:{
    posterPath(){
      return imgUrl+this.movie.poster_path
    }
  },
  methods:{
    routingDetail(){
      router.push({
        name:'detail',
        params:{movie_id:this.movie.id}
        })
    },
  }

}
</script>

<style  lang="scss" scoped>
img {
    max-width: 100%;
    height: 100%;
    cursor: pointer;
}

</style>
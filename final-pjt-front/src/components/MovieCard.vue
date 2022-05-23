<template>
  <div>
    <img :src="posterPath" alt="">
  </div>
</template>

<script>
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
  }
}
</script>

<style>

</style>
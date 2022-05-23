<template>
  <div>
    <p>{{title}}</p>
    <p>{{overview}}</p>
    <p>{{releaseDate}}</p>
    <p>{{voteAverage}}</p>
    <img :src="posterPath" alt="">

    <a v-if="mainTrailerUrl" :href="mainTrailerUrl">미리보기</a>
  </div>
</template>

<script>
import axios from 'axios';
import drf from '@/api/drf'

const imgUrl='https://image.tmdb.org/t/p/w500/'

export default {
  name: 'ArticleDetail',

  data() {
    return {
      movie_id:this.$route.params.movie_id,
      posterPath:'',
      title:'',
      overview:'',
      releaseDate:'',
      voteAverage:'',
      mainTrailerUrl:'',
    };
  },

  created() {
    this.getMovieData(),
    this.getMovieVideo()
  },

  methods: {
    async getMovieData(){
      const response=await axios.get(drf.tmdb.detail(this.movie_id))

      this.posterPath=imgUrl+response.data.poster_path
      this.title=response.data.title
      this.overview=response.data.overview
      this.releaseDate=response.data.release_date
      this.voteAverage=response.data.vote_average
    },
    async getMovieVideo(){
      const response=await axios.get(drf.tmdb.videos(this.movie_id))
      const youtubeUrl="https://www.youtube.com/watch?v="
      
      this.mainTrailerUrl=youtubeUrl+response.data.results[0].key
      
    }
  },
};
</script>

<style lang="scss" scoped>

</style>
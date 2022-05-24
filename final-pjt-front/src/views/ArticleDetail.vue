<template>
  <div>
    <p>{{title}}</p>
    <p>{{overview}}</p>
    <p>{{releaseDate}}</p>
    <p>{{voteAverage}}</p>
    <img :src="posterPath" alt="">
    <!-- <img src="../assets/18.png" alt="" style="width: 600px;height: 900px;"> -->
    <a v-if="mainTrailerUrl" :href="mainTrailerUrl">미리보기</a>

    <review-card 
    v-for="review in reviewList" 
    :review="review"
    :key="review.id"></review-card>

    <review-create-form :movie-id="movieId" @getReview="getReviewList"></review-create-form>
  </div>
</template>

<script>
import axios from 'axios';
import drf from '@/api/drf'
import {mapGetters} from 'vuex'

import ReviewCard from '../components/ReviewCard.vue'
import ReviewCreateForm from '../components/ReviewCreateForm.vue';

const imgUrl='https://image.tmdb.org/t/p/w500/'

export default {
  components: { ReviewCard, ReviewCreateForm },
  name: 'ArticleDetail',

  data() {
    return {
      // 영화 데이터
      movieId:this.$route.params.movie_id,
      posterPath:'',
      title:'',
      overview:'',
      releaseDate:'',
      voteAverage:'',
      mainTrailerUrl:'',


      // 리뷰 데이터
      reviewList:'',
    };
  },

  created() {
    this.getMovieData(),
    this.getMovieVideo(),
    this.getReviewList()
  },
  computed:{
    ...mapGetters(['authHeader'])
  },
  methods: {
    async getMovieData(){
      const response=await axios.get(drf.tmdb.detail(this.movieId))

      this.posterPath=imgUrl+response.data.poster_path
      this.title=response.data.title
      this.overview=response.data.overview
      this.releaseDate=response.data.release_date
      this.voteAverage=response.data.vote_average
    },
    async getMovieVideo(){
      const response=await axios.get(drf.tmdb.videos(this.movieId))
      const youtubeUrl="https://www.youtube.com/watch?v="
      
      this.mainTrailerUrl=youtubeUrl+response.data.results[0].key
    },

    async getReviewList(){

      const response=await axios({
        url: drf.articles.reviewList(this.movieId),
        method: 'get',
        headers: this.authHeader,
      })
      this.reviewList=response.data.serializer_data
  
    }
  },
};
</script>

<style lang="scss" scoped>

</style>
<template>
  <div>

    <p>제목 : {{title}}</p>
    <p>줄거리 : {{overview}}</p>
    <p>개봉 날짜 : {{releaseDate}}</p>
    <p>평점 : {{voteAverage}}</p>
    <img :src="posterPath" alt="">
    <p>찜 여부 : {{isWishMovie}} <button @click.prevent="addWishList">찜</button></p>
    <a v-if="mainTrailerUrl" :href="mainTrailerUrl">미리보기</a>
    <p>리뷰 리스트</p>
    <review-card 
    v-for="review in reviewList" 
    :review="review"
    :key="review.id"
    @getReview="getReviewList"
    ></review-card>

    <review-create-form :movie-id="movieId" :movie-title="title" @getReview="getReviewList"></review-create-form>
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
      // 유저 데이터
      userId:'',
      isWishMovie:false,

      // 영화 데이터
      movieId:parseInt(this.$route.params.movie_id),
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
    ...mapGetters(['authHeader','currentUser']),
  },
  methods: {
    addWishList(){
      axios({
        url: drf.accounts.wishList(),
        method: 'post',
        data:{
          user_id:this.userId,
          movie_id:this.movieId,
          poster_path:this.posterPath
        },
        headers: this.authHeader,
      }).then(()=>{
        this.isWishMovie=!this.isWishMovie
      })

    },
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
      
      try{
        this.mainTrailerUrl=youtubeUrl+response.data.results[0].key
      }
      catch(err){
        // console.error(err)
      }
      
    },

    async getReviewList(){
      try{
        const response=await axios({
          url: drf.articles.reviewList(this.movieId),
          method: 'get',
          headers: this.authHeader,
        })
        this.reviewList=response.data.serializer_data
        this.isWishMovie=response.data.wish_state

      }catch(err){
        // console.error(err)
        this.reviewList=[]
      }
    }
  },
};
</script>

<style lang="scss" scoped>

</style>
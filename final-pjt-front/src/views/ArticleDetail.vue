<template>
  <div class="container mt-5">
    <div class="movie-detail">
      <p class="d-flex p-2 title">{{movie.title}}</p>
      <div class="d-flex justify-content-around" >
        <div class="container">
          <div>
            <div class="d-flex align-items-start ">
              <p class="btn btn-outline-secondary ">개봉 날짜 : {{movie.release_date}}</p>
              <p class="btn btn-outline-secondary">평점 : {{movie.vote_average}}</p>
              <p class="btn btn-outline-secondary">유저 평점 : {{userRate}}</p>
               
              <div class="d-flex align-items-center mx-3">
                <div id="heart" @click.prevent="addWishList"><ToggleFavorite :isWishMovie="isWishMovie" class="haert-box"/></div>
              </div>  
            </div>
            <div class="container">
              <p class="overview">{{movie.overview}}</p>
            </div>
            <div class="d-flex align-items-start">
              <button @click="onClickRedirect" v-if="mainTrailerUrl" :href="mainTrailerUrl" 
              type="button" class="btn btn-outline-light btn-lg " id="box">미리보기</button>
            </div>
          </div>
        </div>
        <div class="container inline" id="image">
          <img :src="posterPath" alt="">
        </div>
      </div>
    </div>
    <div class="review-list mt-5">
      <div class="container slider">
        <p class="sub-title">리뷰 리스트</p>
        <div class="slides">
          <MovieDetailReviewCard
          v-for="review in reviewList" 
          :review="review"
          :key="review.id"
          @getReview="getReviewList"
          ></MovieDetailReviewCard>  
        </div>
      </div>
    </div>

    <review-create-form :movie="movie" @getReview="getReviewList"></review-create-form>
  </div>
</template>

<script>
import axios from 'axios';
import drf from '@/api/drf'
import {mapGetters} from 'vuex'

import MovieDetailReviewCard from '../components/MovieDetailReviewCard.vue'
import ReviewCreateForm from '../components/ReviewCreateForm.vue';

import ToggleFavorite from "../components/ToggleFavorite.vue";


const imgUrl='https://image.tmdb.org/t/p/w500/'

export default {
  components: { MovieDetailReviewCard, ReviewCreateForm, ToggleFavorite },
  name: 'ArticleDetail',

  data() {
    return {
      liked: false,

      // 유저 데이터
      userId:'',
      isWishMovie:false,
      userRate:'',
      

      // 영화 데이터
      movieId:parseInt(this.$route.params.movie_id),
      movie:{},
      mainTrailerUrl:'',
      moviePosterPath:'',

      // 리뷰 데이터
      reviewList:'',
    };
  },

  created() {
    this.getMovieData()
    this.getMovieVideo()
    this.getReviewList()
  },

  computed:{
    ...mapGetters(['authHeader','currentUser']),
    posterPath(){
      return imgUrl+this.movie.poster_path
    }
  },
  methods: {
    addWishList(){
      axios({
        url: drf.accounts.wishList(),
        method: 'post',
        data:{
          user_id:this.userId,
          movie_id:this.movieId,
          poster_path:this.posterPath,
          release_date:this.movie.release_date,
          title:this.movie.title
        },
        headers: this.authHeader,
      }).then(()=>{
        this.isWishMovie=!this.isWishMovie
      })

    },
    async getMovieData(){
      const response=await axios.get(drf.tmdb.detail(this.movieId))
      this.movie=response.data
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
        
        this.userRate=response.data.average_rate
        this.reviewList=response.data.serializer_data
        this.isWishMovie=response.data.wish_state

      }catch(err){
        // console.error(err)
        this.reviewList=[]
      }
    },
    onClickRedirect(){   
        window.open(this.mainTrailerUrl, "_blank")
      },   
  },
};
</script>

<style lang="scss" scoped>
  #box {
    width: 300px;
    height: 70px;
  }
  a {
    text-decoration: none;
    color: black;
  }
  img {
    width: 50%;
    // height: 1000px;
  }
  #heart {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 0px;
  }
  .haert-box {
    background: none;
    border: none;
    padding: 0;
    outline: inherit;
    cursor: pointer;
  }
  .overview {
    font-size: 20px;
  }
  .title{
    font-size: 45px;
  }
  .movie-detail{
    margin-left: 90px;
  }
  .sub-title{
    font-size: 30px;
  }

  // 슬라이더
  .slider {
    width: 100vw;
    text-align: center;
    border-radius: 10px;
    overflow: hidden;
 
  }
  
  .slides {
    display: flex;
    overflow-x: auto;
    /* overflow: hidden; */
    scroll-snap-type: x mandatory;
    scroll-behavior: smooth;
    -webkit-overflow-scrolling: touch;
  }
  .slides::-webkit-scrollbar {
    width: 10px;
    height: 10px;
  }
  .slides::-webkit-scrollbar-thumb {
    background: #ffffff50;
    border-radius: 10px;
  }
  .slides::-webkit-scrollbar-track {
    background: transparent;
  }
  .slides > div {
    scroll-snap-align: start;
    flex-shrink: 0;
    margin-right: 50px;
    border-radius: 10px;
    overflow: hidden;

    // transform-origin: center center;
    // transform: scale(1);
    // transition: transform 0.5s;
    // position: relative;
    
    display: flex;
    justify-content: center;
    align-items: center;

  }
  
  .author-info {
    background: rgba(0, 0, 0, 0.75);
    color: white;
    padding: 0.75rem;
    text-align: center;
    position: absolute;
    bottom: 0;
    left: 0;
    width: 100%;
    margin: 0;
  }
  .author-info a {
    color: white;
  }
</style>
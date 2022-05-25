<template>
  <div class="container mt-5">
    <div class="movie-detail">
      <p class="d-flex p-2 title">{{title}}</p>
      <div class="d-flex justify-content-around" >
        <div class="container">
          <div>
            <div class="d-flex align-items-start ">
              <p class="btn btn-outline-secondary ">개봉 날짜 : {{releaseDate}}</p>
              <p class="btn btn-outline-secondary">평점 : {{voteAverage}}</p>
               
              <div class="d-flex align-items-center mx-3">
                <div id="heart" @click.prevent="addWishList"><ToggleFavorite :isWishMovie="isWishMovie" class="haert-box"/></div>>
              </div>  
            </div>
            <div class="container">
              <p class="overview">{{overview}}</p>
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
      <div>
        <p>리뷰 리스트</p>
        <div class="container">
          <review-card 
          v-for="review in reviewList" 
          :review="review"
          :key="review.id"
          @getReview="getReviewList"
          ></review-card>  
        </div>
      </div>
    </div>

    <review-create-form :movie-id="movieId" :movie-title="title" @getReview="getReviewList"></review-create-form>
  </div>
</template>

<script>
import axios from 'axios';
import drf from '@/api/drf'
import {mapGetters} from 'vuex'

import ReviewCard from '../components/ReviewCard.vue'
import ReviewCreateForm from '../components/ReviewCreateForm.vue';

import ToggleFavorite from "../components/ToggleFavorite.vue";
const imgUrl='https://image.tmdb.org/t/p/w500/'

export default {
  components: { ReviewCard, ReviewCreateForm, ToggleFavorite },
  name: 'ArticleDetail',

  data() {
    return {
      liked: false,

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
    this.getMovieData()
    this.getMovieVideo()
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
  .for-center{
    margin-left: 90px;
  }
  // .background{
  //   background-image: url("paper.gif");
  //   background-color: #cccccc;
  // }
</style>
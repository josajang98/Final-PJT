<template>
  <div class="container pb-5">
    <div >
      <p class="profile-title">내가 쓴 리뷰</p>
      <div class="container slider">
        <div class="slides">
          <review-card 
          v-for="review in userWriteReviewList" 
          :review="review"
          :key="review.id"
          :id="review.id"
          :u-name="userName"
          @getReview="getProfileData"
          ></review-card>
        </div>
      </div>
    </div>
    <br>
    <div clsss="pb-5 mt-5">
      <p class="profile-title">내가 좋아요 단 리뷰</p>
      <div class="container slider">
        <div class="slides">
          <review-card 
          v-for="review in userLikeReviewList" 
          :review="review"
          :key="review.created_at"
          :id="'i'+review.id"
          :u-name="userName"
          @getReview="getProfileData"
          ></review-card>
        </div>
      </div>
    </div>


    <div class="input-group pt-5 pb-5">
      <select class="form-select" id="inputGroupSelect04" aria-label="Example select with button addon" v-model="genreValue">
        <option 
        v-for="genre in genreList"
        :value="genre.id"
        :key="genre.id">
        {{genre.name}}
        </option>
      </select>
      <button class="btn btn-outline-secondary" type="button" @click="onSubmit">Button</button>
    </div>
  </div>
</template>

<script>
import {mapGetters} from 'vuex'
import axios from 'axios'
import drf from '@/api/drf'
import ReviewCard from '../components/ReviewCard.vue'
export default {
  name: 'ProfileView',

  data() {
    return {
      userName:this.$route.params.username,
      userWriteReviewList:'',
      userLikeReviewList:'',
      genreValue:'',
      genreList:[
        {id:12,name:'모험'},
        {id:14,name:'판타지'},
        {id:16,name:'애니메이션'},
        {id:18,name:'드라마'},
        {id:27,name:'공포'},
        {id:28,name:'액션'},
        {id:35,name:'코미디'},
        {id:36,name:'역사'},
        {id:37,name:'서부'},
        {id:53,name:'스릴러'},
        {id:80,name:'범죄'},
        {id:99,name:'다큐멘터리'},
        {id:878,name:'SF'},
        {id:9648,name:'미스터리'},
        {id:10402,name:'음악'},
        {id:10749,name:'로맨스'},
        {id:10751,name:'가족'},
        {id:10752,name:'전쟁'},
        {id:10770,name:'TV영화'},
      ]
    };
  },
  components:{
    ReviewCard
  },

  computed: {
    ...mapGetters(['authHeader','currentUser'])
  },
  created(){
    this.getProfileData()
  },

  methods: {
    inputChange(){
      console.log(this.genreValue)
    },
    async getProfileData(){
      const response=await axios({
        url: drf.accounts.getProfile(this.userName),
        method: 'get',
        headers: this.authHeader,
      })
      this.userWriteReviewList=response.data.review_set
      this.userLikeReviewList=response.data.like_review
      this.genreValue=response.data.genre_id
      console.log(response.data)
    },
    onSubmit(){
      axios({
        url: drf.accounts.genre(this.currentUser.username,this.genreValue),
        method: 'put',
        data: {
          username:this.currentUser.username
        },
        headers: this.authHeader,
      })
      .then(res=>{
        alert('장르 변경 완료')
        console.log(res.data)
      })
    }
  },
  
};
</script>

<style lang="scss" scoped>
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
  .profile-title{
    font-size:32px;
  }
</style>
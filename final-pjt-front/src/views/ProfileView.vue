<template>
  <div>
    <p>내가 쓴 리뷰</p>
    <review-card 
    v-for="review in userWriteReviewList" 
    :review="review"
    :key="review.id"
    :u-name="userName"
    @getReview="getProfileData"
    ></review-card>
    <br>
    <p>내가 좋아요 단 리뷰</p>
    <review-card 
    v-for="review in userLikeReviewList" 
    :review="review"
    :key="review.created_at"
    :u-name="userName"
    @getReview="getProfileData"
    ></review-card>


    <div class="input-group">
      <select class="form-select" id="inputGroupSelect04" aria-label="Example select with button addon" @change="inputChange(this.value)" >
        <option selected>Choose...</option>
        <option 
        v-for="genre in genreList"
        :value="genre.value"
        :key="genre.value">
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
    ...mapGetters(['authHeader'])
  },
  created(){
    this.getProfileData()
  },

  methods: {
    inputChange(value){
      this.genreValue=value
      console.log( this.genreValue)
    },
    async getProfileData(){
      const response=await axios({
        url: drf.accounts.getProfile(this.userName),
        method: 'get',
        headers: this.authHeader,
      })
      this.userWriteReviewList=response.data.review_set
      this.userLikeReviewList=response.data.like_review
      console.log(response.data)
    },
    onSubmit(event){
      console.log(event)
    }
  },
  
};
</script>

<style lang="scss" scoped>

</style>
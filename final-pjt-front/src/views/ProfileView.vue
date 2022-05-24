<template>
  <div>
    <p>내가 쓴 리뷰</p>
    <review-card 
    v-for="review in userWriteReviewList" 
    :review="review"
    :key="review.id"
    @getReview="getProfileData"
    ></review-card>
    <br>
    <p>내가 좋아요 단 리뷰</p>
    <review-card 
    v-for="review in userLikeReviewList" 
    :review="review"
    :key="review.created_at"
    @getReview="getProfileData"
    ></review-card>
    
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
    async getProfileData(){
      const response=await axios({
        url: drf.accounts.getProfile(this.userName),
        method: 'get',
        headers: this.authHeader,
      })
      this.userWriteReviewList=response.data.review_set
      this.userLikeReviewList=response.data.like_review
      console.log(this.userWriteReviewList)
    },
    
  },
  
};
</script>

<style lang="scss" scoped>

</style>
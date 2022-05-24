<template>
  <form @submit.prevent="onSubmit" >
    <label for="title">제목: </label>
    <input type="text" id="title" v-model="title" required>
    <label for="content">내용: </label>
    <input type="text" id="content" v-model="content" required>
    <label for="rate">평점: </label>
    <input type="number" step="0.1" max="10" id="rate" v-model="rate" required>
    <button>쓰기</button>
  </form>
</template>

<script>
import {mapGetters} from 'vuex'
import axios from 'axios';
import drf from '@/api/drf'
export default {
  name: 'ReviewCreateForm',

  data() {
    return {
      title:'',
      content:'',
      rate:'',
    };
  },
  props:{
    movieId:Number,
    movieTitle:String
  },
  mounted() {
    
  },
  computed:{
    ...mapGetters(['authHeader'])
  },
  methods: {
    onSubmit() {
      axios({
        url: drf.articles.reviews(this.movieId),
        method: 'post',
        data: {
          title:this.title,
          content:this.content,
          rate:this.rate,
          movie_id:this.movieId,
          movie_title:this.movieTitle
        },
        headers: this.authHeader,
      })
      .then(()=>{
        this.$emit('getReview')
      })
    },
  },
};
</script>

<style lang="scss" scoped>

</style>
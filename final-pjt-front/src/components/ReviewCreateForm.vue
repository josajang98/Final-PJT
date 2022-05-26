<template>
  <div class="container my-5 review-create">
    <!-- <form @submit.prevent="onSubmit" >
      <label for="title">제목: </label>
      <input type="text" id="title" v-model="title" required>
      <label for="content">내용: </label>
      <input type="text" id="content" v-model="content" required>
      <label for="rate">평점: </label>
      <input type="number" step="0.1" max="10" id="rate" v-model="rate" required>
      <button>쓰기</button>
    </form> -->
    <form @submit.prevent="onSubmit" class="row g-3 needs-validation d-flex justify-content-start" novalidate>
      <div class="col-md-8">
        <label for="title" class="form-label sub-title">Title</label>
        <input type="text" class="form-control sub-content" id="title" placeholder="Write Title" v-model="title" required>
        <div class="valid-feedback">
          Looks good!
        </div>
      </div>
      <div class="col-md-4">
        <label for="rate" class="form-label sub-title" >Rate</label>
        <input type="number" class="form-control sub-content" id="rate" step="0.1" max="10" v-model="rate" required>
        <div class="valid-feedback">
          Looks good!
        </div>
      </div>
      <div class="col-md-12 text-area">
        <label for="content" class="form-label sub-title">Content</label>
        <textarea class="form-control sub-content" id="content" rows="8" placeholder="Write Content" v-model="content" required></textarea>
        <div class="valid-feedback">
          Looks good!
        </div>
      </div>
      <div class="col-12">
        <button class="btn btn-secondary write" type="submit">Write Reivew</button>
      </div>
    </form>

  </div>



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
  .review-create{
    width: 80%;
  }
  .sub-title{
    font-size: 27px;
  }
  .write{
    font-size: 20px;
  }

  .user-name{
    font-size: 30px;
  }

  .sub-content{
    font-size: 23px;
  }
</style>
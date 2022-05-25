<template>
  <div>

    <div class="container col-10">
      <div class="d-flex justify-content-start mt-3">
        {{review.user.username}}
      </div>
      <a href="#exampleModal" data-bs-toggle="modal" class="list-group-item list-group-item-secondary" aria-hidden="true">
        <div class="d-flex w-100 justify-content-between">
          title : {{review.title}}
          <small>rate : {{review.rate}}</small>
        </div>
      </a>
    </div>

    <!-- Modal -->
    <div class="modal fade modal-dialog-scrollable" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content bg-dark p-2" style="--bs-bg-opacity: .75;">
          <div class="modal-header ">
            <h5 class="modal-title" id="exampleModalLabel">{{ review.title }}</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            {{review.content}}
          </div>
          <div class="modal-footer">
            <button @click.prevent="likeArticle"> 좋아요</button>
            {{likeUserCount}}
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
            <button type="button"  @click.prevent="edit" class="btn btn-primary">Save</button>
            <button type="button"  @click.prevent="onDelete" class="btn btn-primary">Delete</button>
          </div>
        </div>
      </div>
    </div>





    <!-- 영화 제목 : {{review.movie_title}}
    작성자 : {{review.user.username}}
    제목 : {{review.title}}
    내용 : {{review.content}}
    좋아요 수 : {{likeUserCount}}
    유저 평점 : {{review.rate}}
    <button @click.prevent="likeArticle"> 좋아요</button>
    <button @click.prevent="edit">수정</button>
    <button @click.prevent="onDelete">삭제</button> -->

      <form @submit.prevent="onSubmit" v-show="isEdit" >
        <label for="title">제목: </label>
        <input type="text" id="title" v-model="title" required >
        <label for="content">내용: </label>
        <input type="text" id="content" v-model="content" required >
        <label for="rate">평점: </label>
        <input type="number" step="0.1" max="10" id="rate" v-model="rate" required >
        <button>수정</button>
      </form>


  </div>





</template>

<script>
import {mapGetters} from 'vuex'
import axios from 'axios'
import drf from '@/api/drf'
export default {
  name: 'ReviewCard',

  data() {
    return {
      likeUserCount:this.review.like_users_count,
      isEdit:false,
      title:this.review.title,
      content:this.review.content,
      rate:this.review.rate,
      movieId:this.review.movie_id,
    };
  },
  props:{
    review:Object,
    uName:String
  },
  mounted() {
    
  },
  computed:{
    ...mapGetters(['authHeader'])
  },
  methods: {
    async likeArticle() {
      console.log(this.review)
      /* 좋아요
      POST: likeArticle URL(token)
        성공하면
          state.article 갱신
        실패하면
          에러 메시지 표시
      */
      const response=await axios({
        url: drf.articles.likeArticle(this.review.movie_id,this.review.id),
        method: 'post',
        headers: this.authHeader,
      })
      this.$emit('getReview')
      this.likeUserCount=response.data.like_users_count
    },
    edit(){
      this.isEdit=!this.isEdit
    },

    onSubmit() {
      axios({
        url: drf.articles.review(this.review.movie_id,this.review.id),
        method: 'put',
        data: {
          title:this.title,
          content:this.content,
          rate:this.rate,
          movie_id:this.movieId,
          movie_title:this.review.movie_title
        },
        headers: this.authHeader,
      })
      .then(()=>{
        this.$emit('getReview')
        this.isEdit=!this.isEdit
      })
    },
    onDelete() {
      axios({
        url: drf.articles.review(this.review.movie_id,this.review.id),
        method: 'delete',
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

  // .review-card{
  //   height:50px;
  // }

</style>
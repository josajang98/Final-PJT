<template>
  <div>

    <div class="container col-10">
      <div class="d-flex justify-content-start mt-3 sub-title">
        {{review.user.username}}
      </div>
      <a href="#exampleModal1" data-bs-toggle="modal" class="list-group-item list-group-item-secondary" aria-hidden="true">
        <div class="d-flex w-100 justify-content-between sub-title">
          title : {{review.title}}
          <small>rate : {{review.rate}}</small>
        </div>
      </a>
    </div>

    <!-- Modal -->
    <div class="modal fade modal-dialog-scrollable" id="exampleModal1" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content bg-dark p-2" style="--bs-bg-opacity: .75;">
          <div class="modal-header ">
            <h5 class="modal-title" id="exampleModalLabel" v-show="!isEdit">{{ review.title }}</h5>
            <h5 class="modal-title" id="exampleModalLabel" v-show="isEdit">  <input type="text" id="title" v-model="title" style="height:50px; width:300px;"></h5>
            <h6 aria-label="Close" v-show="!isEdit">점수 : {{review.rate}} / 10</h6>
            <h6 aria-label="Close" v-show="isEdit">점수 :<input type="number" step="0.1" max="10" id="rate" v-model="rate" required style="height:50px; width:50px;"></h6>
            <!-- <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button> -->
          </div>
          <div class="modal-body" v-show="!isEdit">{{review.content}}</div>
          <div class="modal-body" v-show="isEdit"><textarea name="content" id="content" cols="30" rows="10" v-model="content" class="madal-text" style="height:250px; width:430px; text-align=justify;"></textarea></div>
          <div class="modal-footer d-flex justify-content-between">

            <div class="d-flex justify-content-between">
              <vue-star animate="animated bounceIn" color="#2a6eeb">
                <a slot="icon" class="fa fa-heart" @click.prevent="likeArticle">
                  <svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" fill="currentColor" class="bi bi-hand-thumbs-up-fill" viewBox="0 0 16 16">
                    <path d="M6.956 1.745C7.021.81 7.908.087 8.864.325l.261.066c.463.116.874.456 1.012.965.22.816.533 2.511.062 4.51a9.84 9.84 0 0 1 .443-.051c.713-.065 1.669-.072 2.516.21.518.173.994.681 1.2 1.273.184.532.16 1.162-.234 1.733.058.119.103.242.138.363.077.27.113.567.113.856 0 .289-.036.586-.113.856-.039.135-.09.273-.16.404.169.387.107.819-.003 1.148a3.163 3.163 0 0 1-.488.901c.054.152.076.312.076.465 0 .305-.089.625-.253.912C13.1 15.522 12.437 16 11.5 16H8c-.605 0-1.07-.081-1.466-.218a4.82 4.82 0 0 1-.97-.484l-.048-.03c-.504-.307-.999-.609-2.068-.722C2.682 14.464 2 13.846 2 13V9c0-.85.685-1.432 1.357-1.615.849-.232 1.574-.787 2.132-1.41.56-.627.914-1.28 1.039-1.639.199-.575.356-1.539.428-2.59z"/>
                  </svg>
                </a>
              </vue-star>
              <div id="like-number">
                {{likeUserCount}}
              </div>
            </div>
            <!-- <vue-star animate="animated bounceIn" color="#F05654">
              <i slot="icon" class="fa fa-heart">dddddddddddddddddddddddddddddddddd</i>
            </vue-star> -->
            <!-- <button @click.prevent="likeArticle"> 좋아요</button> -->
            <div>
              <button type="button"  @click.prevent="edit" class="btn btn-primary" v-show="!isEdit">Edit</button>
              <button type="button"  @click.prevent="onSubmit" class="btn btn-primary" v-show="isEdit">Edit</button>
              <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
              <button type="button"  @click.prevent="onDelete" class="btn btn-secondary">Delete</button>
            </div>
            
            <!-- <form @submit.prevent="onSubmit" v-show="isEdit" >
              <label for="title">제목: </label>
              <input type="text" id="title" v-model="title" required >
              <label for="content">내용: </label>
              <input type="text" id="content" v-model="content" required >
              <label for="rate">평점: </label>
              <input type="number" step="0.1" max="10" id="rate" v-model="rate" required >
              <button>수정</button>
            </form> -->
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



  </div>





</template>

<script>
import {mapGetters} from 'vuex'
import axios from 'axios'
import drf from '@/api/drf'
import VueStar from 'vue-star'
export default {
  name: 'ReviewCard',
  components: {
    VueStar
  },
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
  .VueStar {
    position: relative;
    // margin-left: 100px;
  }
  .VueStar__decoration{
    font-size: 50px;
  }
  #like-number{
    font-size: 30px;
    margin-top: 27px;
  }
  h5{
    font-size: 40px;
  }
  h6{
    font-size: 30px;
  }
  .modal-body{
    font-size: 30px;
    text-align: left;
  }
  .sub-title{
    font-size: 23px;
  }
  .sub-content{
    font-size: 20px;
  }
  .scroll{
    overflow-y: hidden;
    overflow-y: scroll;
  }

</style>
<template>
  <div>
    {{review.user.username}}
    {{review.title}}
    {{review.content}}
    {{likeUserCount}}
    {{review.rate}}
    <button @click.prevent="likeArticle"> 버튼</button>
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
      likeUserCount:this.review.like_users_count
    };
  },
  props:{
    review:Object
  },
  mounted() {
    
  },
  computed:{
    ...mapGetters(['authHeader'])
  },
  methods: {
    async likeArticle() {
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
      this.likeUserCount=response.data.like_users_count
    },
  },
};
</script>

<style lang="scss" scoped>

</style>
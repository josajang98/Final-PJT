<template>
  <div>
    <div b-container cotainer-fluid>
      <!-- 커버 화면 -->
      <div class="login-cover"></div>
      <!-- 로그인 폼 -->
      <div class="login box01">
        <!-- <div class="box01"></div> -->
        <div class="login-card pb-1 user-pwd">
          <span style="color: #f1f1f1; opacity: 0.7;">"드루와 드루와"</span><br><br>
          <span style="color: #f1f1f1; opacity: 0.7;">-영화 '신세계' 中</span><br>
          <form class="login-form mt-3" :model="credentials" ref="form" @submit.prevent="signup(credentials)">
            <div>
              <label for="username ">username :</label>
              <input type="text" v-model="credentials.username" id="username" prefix-icon="fas fa-user" placeholder="아이디">
            </div>
            <div>
              <label for="password1">password : </label>
              <input type="password" v-model="credentials.password1" placeholder="비밀번호" id="password1" prefix-icon="fas fa-lock">
            </div>
            <div>
              <label for="password2">Password Confirmation:</label>
              <input type="password" v-model="credentials.password2" placeholder="비밀번호" id="password2" prefix-icon="fas fa-lock">
            </div>
            <button id="login-button" block><span style="color: rgba(255, 255, 255, 0.82);">회원가입</span></button>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import router from '@/router';
  import { mapActions,mapGetters } from 'vuex'
  export default {
    name: 'SignupView',

    data() {
      return {
        credentials: {
          username: '',
          password1: '',
          password2: '',
        }
      }
    },
    methods: {
      ...mapActions(['signup']),
      routingArticles(){
      if (this.isLoggedIn === true)
        router.push({name:'articles'})
      }
    },
    computed: {
    ...mapGetters(['isLoggedIn'])
    },
    created(){
    this.routingArticles()
  },
  }
</script>

<style></style>

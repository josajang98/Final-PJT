<template>

  <div b-container cotainer-fluid>
    <!-- 커버 화면 -->
    <div class="login-cover"></div>
    <!-- 로그인 폼 -->
    <div class="login box01">
      <!-- <div class="box01"></div> -->
      <div class="login-card pb-1 user-pwd">
        <span style="color: #f1f1f1; opacity: 0.7;">"드루와 드루와"</span><br><br>
        <span style="color: #f1f1f1; opacity: 0.7;">-영화 '신세계' 中</span><br>
        <form class="login-form mt-3" :model="credentials" ref="form" @submit.prevent="login(credentials)">
          <div>
            <label for="username ">username :</label>
            <input type="text" v-model="credentials.username" id="username" prefix-icon="fas fa-user" placeholder="아이디">
          </div>
          <div>
            <label for="password">password : </label>
            <input type="password" v-model="credentials.password" placeholder="비밀번호" id="password" prefix-icon="fas fa-lock">
          </div> 
          <button id="login-button" block><span style="color: rgba(255, 255, 255, 0.82);">로그인</span></button>  
          <h6 class="signup-router text-secondary p-0 signup-font" @click="signup">회원가입</h6>
        </form>
      </div>
    </div>
  </div>
</template>

<script src="sweetalert2.all.min.js"></script>
<script>
import router from '@/router'
import { mapActions,mapGetters } from 'vuex'


// import Swal from 'sweetalert2/dist/sweetalert2.js'
// import 'sweetalert2/src/sweetalert2.scss'
export default {
  name: 'LoginView',

  data(){
    return {
      credentials:{
        username : '',
        password : '',
      }
    }
  },
  computed: {
    ...mapGetters(['isLoggedIn'])
  },
  methods:{
    ...mapActions(['login']),
    signup(){
      router.push({name:'signup'})
    },
    routingArticles(){
      if (this.isLoggedIn === true)
        router.push({name:'articles'})
    }
  },
  created(){
    this.routingArticles()
  },
}
</script>

<style>
.user-pwd{
  font-size: 25px;
}

#bg {
  position: fixed; 
  z-index: -1;
  top: 0; 
  left: 0; 
  margin: auto;
}
.login{
  margin-top:25px;
}
.login-cover {
  position: fixed;
  z-index: 3;
  width: 100vw;
  height: 100vh;
  background-color: black;
  animation: fadeout 3s;
  animation-fill-mode: forwards;
  animation-delay: 1.55s;
}
@keyframes fadeout {
    from {
        z-index: 3;
        opacity: 1;
    }
    to {
        z-index: -1;
        opacity: 0;
    }
}
.text-slide {
  animation-name: slide;
  animation-delay: 1.75s;
  animation-duration: 2s;
  animation-duration: leaner;
  animation-fill-mode: forwards;
}
@keyframes slide {
  0% {
    top: 45%;
    transform: scale(1)
  }
  100% {
    top: 83%;
    transform: scale(0.8)
  } 
}
.cover-textCenter {
  position: fixed;
  width: 100%;
  top: 45%;
  left: 2%;
  z-index: 6;
  margin-left: -50px;
  margin-top: -25px;
  color: rgba(255, 255, 255, 0.82);
  font-family: 'Nanum Myeongjo', serif;
}
.cover-textCenter > h2 {
  font-family: 'Nanum Myeongjo', serif;
}
.cover-textCenter > h1  {
  padding-bottom: 1rem;
}
.login {
  flex: 1;
  display: flex;
  justify-content: center;
  align-items: center;
}
#login-button {
  width: 100%;
  margin-top: 40px;
  padding: 14px 20px;
  border: none;
  cursor: pointer;
  width: 100%;
  transition: 0.5s;
  font-size: 16px;
  color: rgba(255, 255, 255, 0.82);
}
.login-card{
  background-color: rgba(0, 0, 0, 0.9);
  border-color: rgba(0, 0, 0, 0.9);;
}
.login-form {
  width: 290px;
}
.signup-router {
  margin-top: 10px;
  font-size: 13px;
  cursor: pointer;
}
</style>

<style lang="scss">
$teal: rgba(71, 63, 113, 0.8);
#login-button {
  background: $teal;
  border-color: $teal;
  &:hover,
  &.active,
  &:focus {
    background: lighten($teal, 20);
    border-color: lighten($teal, 20);
  }
}
.login .el-input__inner:hover {
  border-color: $teal;
}
.login .el-input__prefix {
  background: rgb(238, 237, 234);
  left: 0;
  height: calc(100% - 2px);
  left: 1px;
  top: 1px;
  border-radius: 3px;
  .el-input__icon {
    width: 30px;
  }
}
.login .el-input input {
  padding-left: 35px;
}
.login .el-card {
  padding-top: 0;
  padding-bottom: 30px;
}
h2 {
  font-family: "Open Sans";
  letter-spacing: 1px;
  font-family: Roboto, sans-serif;
  padding-bottom: 20px;
  color: rgba(255, 255, 255, 0.82);
}
a {
  color: $teal;
  text-decoration: none;
  &:hover,
  &:active,
  &:focus {
    color: lighten($teal, 7);
  }
}
.login .el-card {
  width: 340px;
  display: flex;
  justify-content: center;
}
.signup-font{
  font-size:28px;
}
.box01{
  width:auto;
  height:100vh;
  position:relative;
  background:url('~@/assets/backgroundimageblack.png');
  background-size:cover;
  // opacity:0.5;

}
.box01::before{
  content:"";
  opacity:0.5;
  position:absolute;
  top:0px;
  left:0px;
  right:0px;
  bottom:0px;
  background-color: #000;
}
.box01 .login-card{
  color:#fff;
  text-align:center;
  position:relative;}
</style>
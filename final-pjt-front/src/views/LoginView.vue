<template>
  <div>
    <h1>login</h1>
    <br>
    <form @submit.prevent="login(credentials)">
      <div>
        <label for="username">username :</label>
        <input type="text" v-model="credentials.username" id="username">
      </div>
      <br>
      <div>
        <label for="password">password : </label>
        <input type="password" v-model="credentials.password" id="password">
      </div>
      
      <button>로그인</button>
    </form>
    <br>
    <p>아직 잘골라줘유 사용 전이신가요?</p>
    <button @click="signup">회원가입</button>
  </div>
</template>

<script>
import router from '@/router'
import { mapActions,mapGetters } from 'vuex'
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

</style>
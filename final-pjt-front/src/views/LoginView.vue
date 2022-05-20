<template>
  <div>
    <h1>login</h1>
    <form @submit.prevent="login(credentials)">
      <div>
        <label for="username">username</label>
        <input type="text" v-model="credentials.username" id="username">
      </div>
      <div>
        <label for="password">password</label>
        <input type="password" v-model="credentials.password" id="password">
      </div>
      
      <button>로그인</button>
    </form>
    <button @click="signup">회원가입</button>
  </div>
</template>

<script>
import router from '@/router'
import { mapActions } from 'vuex'
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
  methods:{
    ...mapActions(['login']),
    signup(){
      router.push({name:'signup'})
    }
  }
}
</script>

<style>

</style>
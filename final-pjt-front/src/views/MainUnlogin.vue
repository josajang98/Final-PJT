<template>
  <div>
    <p>심심하신가요?</p>
    <p>장르 월드컵을 통해 당신에게 맞는</p>
    <p>영화를 추천 받으세요!</p>
    <button @click="login">잘골라줘유 START</button>
  </div>
</template>

<script>
import router from '@/router';
export default {
  name: 'MainUnlogin',
  methods: {
    login(){
      router.push({name:'login'})
    }
  },
};
</script>

<style lang="scss" scoped>

</style>
<template>
  <div class="py-5 box01 d-flex align-items-center">
    <div class="container">
      <p>심심하신가요?</p>
      <p>장르 월드컵을 통해 당신에게 맞는</p>
      <p>영화를 추천 받으세요!</p>
      <button @click="login" class="custom-btn btn-14">잘골라줘유 START</button>
    </div>
  </div>
</template>

<script>
import router from '@/router';
import { mapGetters } from 'vuex';

export default {
  name: 'MainUnlogin',
  methods: {
    login(){
      router.push({name:'login'})
    },
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
};
</script>

<style lang="scss" scoped>
.box01{
  width:auto;
  height:100vh;
  position:relative;
  background:url('~@/assets/backgroundimageblack.png');
  background-size:cover;
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
.box01 p{
  color:#fff;
  text-align:center;
  position:relative;}
p {
  font-size: 50px;
  // text-shadow: 2px 2px 2px gray;
}
.custom-btn {
  font-size: 53px;
    text-shadow: 2px 2px 2px black;
  width: 500px;
  height: 100px;
  color: #fff;
  border-radius: 25px;
  padding: 10px 25px;
  background: transparent;
  cursor: pointer;
  transition: all 0.3s ease;
  position: relative;
  display: inline-block;
   box-shadow:inset 2px 2px 2px 0px rgba(255,255,255,.5),
   7px 7px 20px 0px rgba(0,0,0,.1),
   4px 4px 5px 0px rgba(0,0,0,.1);
  outline: none;
}

.btn-14 {
  background: #FF8307;
  border: none;
  z-index: 1;
}
.btn-14:after {
  position: absolute;
  content: "";
  width: 100%;
  height: 0;
  top: 0;
  left: 0;
  z-index: -1;
  border-radius: 25px;
  background-color: #eaf818;
  background-image: linear-gradient(315deg, #eaf818 0%, #f6fc9c 74%);
   box-shadow:inset 2px 2px 2px 0px rgba(255,255,255,.5),
   7px 7px 20px 0px rgba(0,0,0,.1),
   4px 4px 5px 0px rgba(0,0,0,.1);
  transition: all 0.3s ease;
}
.btn-14:hover {
  color: #000;
}
.btn-14:hover:after {
  top: auto;
  bottom: 0;
  height: 100%;
}
.btn-14:active {
  top: 2px;
}
</style>
<template>
  <div id="app" class = 'container'>
    <nav v-if="!isLoggedIn" class="navbar navbar-expand-lg">
      <router-link to="/" exact-active-class="active"><img src="./assets/logo.png" alt="asd"></router-link> 
    </nav>
    <nav v-if="isLoggedIn" class="navbar navbar-expand-lg navbar-light">
      <div class="container-fluid">
        <div exact-active-class="active" @click="routingHome">
          <img src="./assets/logo.png" alt="asd">
        </div>
        <button class="navbar-toggler toggle-color" type="button" data-bs-toggle="collapse" data-bs-target="#navbarTogglerDemo03" aria-controls="navbarTogglerDemo03" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarTogglerDemo03">
          <ul class="navbar-nav me-auto mb-2 mb-lg-0">
            <li class="nav-item p-3" @click="routingGenrewc" :class="back(selectGenrewc)">
              <router-link class="text" :to="{ name: 'genrewc'}">장르 월드컵</router-link> 
            </li>
            <li class="nav-item p-3" @click="routingWishList" :class="back(selectWishList)">
              <router-link class="text" :to="{ name: 'wishList'}">내가 찜한 목록</router-link>
            </li>
          </ul>
          <form @submit="onSubmit" class="d-flex">
            <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search" v-model="input">
            <button class="btn btn-outline-success">Search</button>
          </form>
          <li class="p-3 active" @click="routingProfile" :class="back(selectProfile)">{{username}}</li>
          <router-link class="p-3" :to="{ name: 'logout'}"><button>로그아웃</button></router-link>
        </div>
      </div>
    </nav>
  <router-view/>
  </div>
</template>
<script>
  import { mapGetters,mapActions } from 'vuex'
  import router from '@/router'
  export default {
    name: 'App',
    data(){
      return {
        input:'',
        selectGenrewc:false,
        selectWishList:false,
        selectProfile:false,

      }
    },
    methods: {
      ...mapActions(['fetchCurrentUser']),
      onSubmit(){
        router.push({
        name:'search',
        params:{query:this.input}
        })
      },
      routingHome(){
        router.push({ name: 'articles'})
        this.selectGenrewc=false
        this.selectWishList=false
        this.selectProfile=false
      },
      routingGenrewc(){
        router.push({ name: 'genrewc'})
        this.selectGenrewc=true
        this.selectWishList=false
        this.selectProfile=false
      },
      routingWishList(){
        router.push({ name: 'wishList'})
        this.selectGenrewc=false
        this.selectWishList=true
        this.selectProfile=false
      },
      routingProfile(){
        router.push({ 
          name: 'profile',
          params:{username:this.username}
        })
        this.selectGenrewc=false
        this.selectWishList=false
        this.selectProfile=true
      },
      back(data) {
        return {
          "back": data,
        };
      }
    },
    created() {
      this.fetchCurrentUser()
    },
    computed: {
      ...mapGetters(['isLoggedIn','currentUser']),
      username() {
        return this.currentUser.username ? this.currentUser.username : 'guest'
      }
      
    
    },
  }
</script>
<style>
#app {
  /* -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale; */
  text-align: center;
  /* 폰트 */
  font-family: 'East Sea Dokdo', cursive;
  /* font-family: 'Jalnan'; */
  /* font-family: 'Noto Sans KR', sans-serif; */
  font-size: 4vw;
  /* font-weight : 0; */
}

nav a {
  color: white;
  text-decoration:none;
}

nav a.active:hover {
  color: white;
  text-decoration:none;
  background-color: #DBFF4560;
}
nav a.text:hover {
  color: white;
  text-decoration:none;
}
nav li:hover {
  color: white;
  text-decoration:none;
  background-color: #DBFF4560;
}
nav .back{
  background-color: #DBFF4560;
}
nav a.router-link-exact-active:not(.active) {
  background-color: none;
}
nav a.router-link-exact-active {
  color: white;
  text-decoration:none;
}
nav {
  font-size: 1.35vw;
}
li {
  list-style:none;
}

.toggle-color {
  background-color: #FFF775;
}

.animated-icon2 span:nth-child(1) {
  top: 0px;
}

.animated-icon2 span:nth-child(2), .animated-icon2 span:nth-child(3) {
  top: 10px;
}

.animated-icon2 span:nth-child(4) {
  top: 20px;
}

.animated-icon2.open span:nth-child(1) {
  top: 11px;
  width: 0%;
  left: 50%;
}

.animated-icon2.open span:nth-child(2) {
  -webkit-transform: rotate(45deg);
  -moz-transform: rotate(45deg);
  -o-transform: rotate(45deg);
  transform: rotate(45deg);
}

.animated-icon2.open span:nth-child(3) {
  -webkit-transform: rotate(-45deg);
  -moz-transform: rotate(-45deg);
  -o-transform: rotate(-45deg);
  transform: rotate(-45deg);
}

.animated-icon2.open span:nth-child(4) {
  top: 11px;
  width: 0%;
  left: 50%;
}

</style>

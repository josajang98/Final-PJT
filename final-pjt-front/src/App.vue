<template>
  <div id="app" class = 'container'>

    <nav v-if="!isLoggedIn" class="navbar navbar-expand-lg">
      <router-link to="/" exact-active-class="active"><img src="./assets/logo.png" alt="asd"></router-link> 
    </nav>
    <nav v-if="isLoggedIn" class="navbar navbar-expand-lg navbar-light">
      <div class="container-fluid">
        <router-link exact-active-class="active" :to="{ name: 'articles'}" >
          <img src="./assets/logo.png" alt="asd">
        </router-link>
        <button class="navbar-toggler toggle-color" type="button" data-bs-toggle="collapse" data-bs-target="#navbarTogglerDemo03" aria-controls="navbarTogglerDemo03" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarTogglerDemo03">
          <ul class="navbar-nav me-auto mb-2 mb-lg-0">
            <li class="nav-item m-3">
              <router-link :to="{ name: 'genrewc'}">장르 월드컵</router-link> 
            </li>
            <li class="nav-item m-3">
              <router-link :to="{ name: 'wishList'}">내가 찜한 목록</router-link>
            </li>
            <li class="nav-item m-3">
              <router-link :to="{ name: 'profile', params: {username} }">{{username}}</router-link>
            </li>
          </ul>
          <form @submit.prevent="onSubmit" class="d-flex">
            <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search" v-model="input">
            <button class="btn btn-outline-success">Search</button>
          </form>
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
      }
    },
    methods: {
      ...mapActions(['fetchCurrentUser']),
      onSubmit(){
        router.push({
        name:'search',
        params:{query:this.input}
        })
      }
    },
    created() {
      this.fetchCurrentUser()
    },
    computed: {
      ...mapGetters(['isLoggedIn','currentUser']),
      username() {
        return this.currentUser.username ? this.currentUser.username : 'guest'
      },
    },
  }
</script>
<style>
#app {
  /* -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale; */
  text-align: center;
  /* 폰트 */
  /* font-family: 'East Sea Dokdo', cursive; */
  /* font-family: 'Jalnan'; */
  font-family: 'Noto Sans KR', sans-serif;
  font-size: 25px;
  /* font-weight : 0; */
}

/* nav {
  padding: 30px;
} */

nav a {
  color: white;
  text-decoration:none;
}

nav a:hover {
  color: white;
  text-decoration:none;
  background-color: #DBFF4560;
}

nav a:hover:not(.hoverno) {
  background-color: none;
}

nav a.router-link-exact-active:not(.active) {
  background-color: none;
}
nav a.router-link-exact-active {
  color: white;
  text-decoration:none;
  background-color: #DBFF4560;
  
}
.toggle-color {
  background-color: #FF8307;
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

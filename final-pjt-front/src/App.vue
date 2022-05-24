<template>
  <div id="app" class = 'container'>

    <nav v-if="!isLoggedIn" class="navbar navbar-expand-lg">
      <router-link to="/" exact-active-class="active"><img src="./assets/logo.png" alt="asd"></router-link> 
    </nav>
    <nav  v-if="isLoggedIn" class="navbar navbar-expand-lg">
      <router-link exact-active-class="active" :to="{ name: 'articles'}" >
        <img src="./assets/logo.png" alt="asd">
      </router-link> 
      <div class="container-fluid">
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav me-auto mb-2 mb-lg-0">
            <li class="nav-item">
              <router-link :to="{ name: 'genrewc'}">장르 월드컵</router-link> 
            </li>
          </ul>
          <ul class="navbar-nav me-auto mb-2 mb-lg-0">
            <form class="d-flex" role="search">
              <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
              <button class="btn btn-outline-success" type="submit">Search</button>
            </form>
            <li class="nav-item">
              <router-link :to="{ name: 'wishList'}">내가 찜한 목록</router-link> 
            </li>
            <li class="nav-item">
              <router-link :to="{ name: 'profile', params: {username} }">profile</router-link> | 
            </li>
            <li class="nav-item">
              <router-link :to="{ name: 'logout' }">Logout</router-link>
            </li>
          </ul>
        </div>
      </div>
    </nav>
    <router-view/>
  </div>
</template>

<script>

  import { mapGetters,mapActions } from 'vuex'

  export default {
    name: 'App',

    methods: {
      ...mapActions(['fetchCurrentUser'])
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
  font-family: 'East Sea Dokdo', cursive;
  font-size: 25px;
}

nav {
  padding: 30px;
}

nav a {
  color: white;
  text-decoration:none;
}

nav a.router-link-exact-active:not(.active) {
  background-color: none;
}
nav a.router-link-exact-active {
  color: white;
  text-decoration:none;
  background-color: #DBFF4560;
}

</style>

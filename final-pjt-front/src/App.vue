<template>
  <div id="app">
    <nav v-if="this.$store.accounts.state.user">
      <router-link to="/"><img src="./assets/logo.png" alt="asd"></router-link> 
    </nav>
    <nav v-if="!this.$store.state.user">
      <router-link :to="{ name: 'articles'}">
        <img src="./assets/logo.png" alt="asd">
      </router-link> 
      <div class="collapse navbar-collapse">
        <router-link :to="{ name: 'genrewc'}"><p>장르 월드컵</p></router-link> 
        <router-link :to="{ name: 'pickmovie'}"><p>내가 찜한 목록</p></router-link> 
        <!-- <div>
          <b-navbar type="light" variant="light">
            <b-nav-form>
              <b-form-input class="mr-sm-2" placeholder="Search"></b-form-input>
              <b-button variant="outline-success" class="my-2 my-sm-0" type="submit">Search</b-button>
            </b-nav-form>
          </b-navbar>
        </div> -->
        <router-link :to="{ name: 'articles'}"><p>profile</p></router-link> 
      </div>
    </nav>
    <router-view/>
  </div>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>

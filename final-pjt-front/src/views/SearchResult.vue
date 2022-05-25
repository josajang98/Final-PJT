<template>
  <div class="font">
    <p>인물</p>
    <div class="section" style="max-height:200px">
      <person-card
      v-for="person in personData"
      :person="person"
      :key="person.id"
      ></person-card>
    </div>
    <p>영화</p>
    <div class="section" style=" max-height: 400px;">
      <div class="row justify-content-center">
        <MovieCard
          v-for="movie in movieData"
          :movie-id="movie.id"
          :movie-poster-path="movie.poster_path"
          :key="movie.id"
          class="col-lg-2 col-md-3 col-sm-4 p-3"
          style="margin-bottom: 120px;"
        ></MovieCard>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import drf from '@/api/drf'
import MovieCard from '../components/MovieCard.vue';
import PersonCard from '../components/PersonCard.vue';
import { mapActions, mapGetters } from 'vuex'

export default {
  name: 'SearchResult',

  data() {
    return {
      query:this.$route.params.query,
      movieData:[]
    };
  },
  
  components:{
    MovieCard,
    PersonCard,
  },
  
  computed:{
    ...mapGetters(['personData'])
  },
  methods: {
    ...mapActions(['getPersonData']),

    async getMovieData(){
      const response=await axios.get(drf.tmdb.searchMovie(this.query))
      
      this.movieData=response.data.results
      console.log(this.movieData) 
    },
  },
  created(){
    this.getPersonData(this.query)
    this.getMovieData()
  },
};
</script>

<style lang="scss" scoped>
.font {
  font-size: 4vw;
}
.section {
  // max-height: 400px;
  // padding: 1rem;
  overflow-y: auto;
  overflow-x: hidden;
  direction: ltr;
  scrollbar-color: #d4aa70 #e4e4e4;
  scrollbar-width: thin;

  h2 {
    font-size: 1.5rem;
    font-weight: 700;
    margin-bottom: 1rem;
  }

  p + p {
    margin-top: 1rem;
  }
}

.section::-webkit-scrollbar {
  width: 20px;
}

.section::-webkit-scrollbar-track {
  background-color: #e4e4e4;
  border-radius: 100px;
}

.section::-webkit-scrollbar-thumb {
  border-radius: 100px;
  border: 6px solid rgba(0, 0, 0, 0.18);
  border-left: 0;
  border-right: 0;
  background-color: #8070d4;
}

body {
  font-family: "system-ui";
  line-height: 1.4;
  padding: 1rem;
  background-color: #f7f7f7;
  min-height: 1200px;
}

* {
  box-sizing: border-box;
}
</style>
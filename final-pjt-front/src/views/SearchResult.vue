<template>
  <div>
    
    <div class="container">
      <p>영화</p>
      <div class="row bg-white bg-opacity-10 justify-content-center">
        <MovieCard
          v-for="movie in movieData"
          :movie-id="movie.id"
          :movie-poster-path="movie.poster_path"
          :key="movie.id"
          class="col-lg-2 col-md-3 col-sm-4"
        ></MovieCard>
      </div>
      <p>인물</p>
      <div class="row bg-white bg-opacity-10 justify-content-center">
        <person-card
        v-for="person in personData"
        :person="person"
        :key="person.id"
        class="col-lg-2 col-md-3 col-sm-4"
        ></person-card>
      </div>   
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import drf from '@/api/drf'
import MovieCard from '../components/MovieCard.vue';
import PersonCard from '../components/PersonCard.vue';
export default {
  name: 'SearchResult',

  data() {
    return {
      query:this.$route.params.query,
      personData:[],
      movieData:[]
    };
  },
  components:{
    MovieCard,
    PersonCard,
  },
  created(){
    this.getPersonData()
    this.getMovieData()
  },
  methods: {
    async getPersonData(){
      const response=await axios.get(drf.tmdb.searchPerson(this.query))
      
      this.personData=response.data.results
      console.log(this.personData) 
    },

    async getMovieData(){
      const response=await axios.get(drf.tmdb.searchMovie(this.query))
      
      this.movieData=response.data.results
      console.log(this.movieData) 
    },
  },
};
</script>

<style lang="scss" scoped>

</style>
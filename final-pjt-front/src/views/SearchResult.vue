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

</style>
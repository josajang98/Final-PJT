<template>
  <div>
    <movie-card
    v-for="movie in wishList"
      :movie-id="movie.movie_id"
      :movie-poster-path="movie.poster_path"
      :key="movie.id"
      ></movie-card>
  </div>
</template>

<script>
import axios from 'axios';
import drf from '@/api/drf'
import {mapGetters} from 'vuex'
import MovieCard from '../components/MovieCard.vue';
export default {
  name: 'WishList',

  data() {
    return {
      wishList:'',
    };
  },
  components: { MovieCard },
  computed:{
    ...mapGetters(['authHeader'])
  },
  created(){
    this.getWishList()
  },
  methods: {
    getWishList(){
      axios({
        url: drf.accounts.wishList(),
        method: 'get',
        headers: this.authHeader,
      }).then((res)=>{
        this.wishList=res.data
        
      })
    }
  },
};
</script>

<style lang="scss" scoped>

</style>
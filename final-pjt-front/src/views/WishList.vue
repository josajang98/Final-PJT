<template>
  <div class="container">
    <div class="row bg-white bg-opacity-10 justify-content-center">
      <movie-card
      v-for="movie in wishList"
        :movie="movie"
        :key="movie.id"
        class="col-lg-2 col-md-3 col-sm-4"
        ></movie-card>
    </div>
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
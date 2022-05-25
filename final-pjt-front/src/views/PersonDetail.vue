<template>
  <div class="d-flex align-items-center">
    <div class="flex-shrink-0">
      <img :src="profilePath" alt="">
    </div>
    <div class="flex-grow-1 ms-3">
      <p>이름 : {{personData[index].name}}</p>
      <p>성별 : {{personData[index].gender}}</p>
      <div class="my-custom-scrollbar my-custom-scrollbar-primary">
        <div class="row bg-white bg-opacity-10 justify-content-center">
          <MovieCard
            v-for="movie in personMovie"
            :movie-id="movie.id"
            :movie-poster-path="movie.poster_path"
            :key="movie.id"
            class="col-lg-2 col-md-3 col-sm-4"
          ></MovieCard>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import drf from '@/api/drf'
import { mapGetters } from 'vuex'
import MovieCard from '../components/MovieCard.vue';
const imgUrl='https://image.tmdb.org/t/p/w500/'

export default {
  components: { MovieCard },
  name: 'ArticleDetail',

  data() {
    return {
      // 유저 데이터    

      // 영화 데이터
      index:0,
      personId:parseInt(this.$route.params.person_id),
      personMovie:[],
      
      // 리뷰 데이터
      reviewList:'',
    };
  },

  created() {
    this.getPersonMovie()

  },
  computed:{
    ...mapGetters(['authHeader','currentUser','personData']),
    profilePath(){
      return imgUrl+this.personData[this.index].profile_path
    }
  },
  methods: {
    async getPersonMovie(){
      const response=await axios.get(drf.tmdb.getMovieCreadit(this.personId))
      this.personMovie=response.data.cast
    },
  },
};
</script>

<style lang="scss" scoped>
img{
  width:75%;
  height: auto;
}
.my-custom-scrollbar {
  position: relative;
  width: 800px;
  height: 400px;
  overflow: auto;
}
</style>
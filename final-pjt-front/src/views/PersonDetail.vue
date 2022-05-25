<template>
  <div>
    <div class="d-flex align-items-center py-5">
      <img :src="profilePath" alt="" class="pe-4">
      <div class="px-4">
        <p>이름 : {{personData[index].name}}</p>
        <p>성별 : {{personData[index].gender}}</p>
        <p>생일 : {{personDetail.birthday}}</p>
        <p>출생지 : {{personDetail.place_of_birth}}</p>
        <a v-if="personDetail.homepage" :href="personDetail.homepage">홈페이지</a>
      </div>
    </div>
    <div class="section">
      <div class="row justify-content-center">
        <MovieCard
          v-for="movie in personMovie"
          :movie-id="movie.id"
          :movie-poster-path="movie.poster_path"
          :key="movie.id"
          class="col-lg-2 col-md-3 col-sm-4 p-3"
        ></MovieCard>
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
      personDetail:{},
      
      // 리뷰 데이터
      reviewList:'',
    };
  },

  created() {
    this.getPersonMovie()
    this.getPersonDetail()

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
    async getPersonDetail(){
      const response=await axios.get(drf.tmdb.personDetail(this.personId))
      this.personDetail=response.data
      console.log(this.personDetail)
    },
  },
};
</script>

<style lang="scss" scoped>
img{
  width:200px;
  height: auto;
  border-radius: 10%;
}

p {
  font-size: 35px;
  text-align: left;
}
.section {
  max-height: 300px;
  // padding: 1rem;
  overflow-y: auto;
  overflow-x: hidden;
  direction: ltr;
  scrollbar-color: #d4aa70 #e4e4e4;
  scrollbar-width: thin;
  margin-bottom: 120px;

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
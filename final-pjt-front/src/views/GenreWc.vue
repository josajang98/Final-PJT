<template>
  <div class="text-box">
    <br>

    <!-- 장르월드컵 선택 -->
    <h1 class="p-3">장르 한번 골라보자!!</h1>
    <h3 v-if="!result" class="p-3" style="font-size:4.5vw"> {{getRound()}}강 </h3>
    <h3 v-if="result" class="p-3" style="font-size:4.5vw"> 결과 </h3>
    <div class="d-flex justify-content-between align-items-center" v-if="!result">
      <div class="background mx-3" @click="selected(randGenreIdList[index])">
        <genre-wc-card :genre-id="randGenreIdList[index]" ></genre-wc-card>
      </div>
      <span class="mx-2" style="font-size:4vw;">VS</span>
      <div class="background" @click="selected(randGenreIdList[index+1])">
        <genre-wc-card :genre-id="randGenreIdList[index+1]"></genre-wc-card>
      </div>
    </div>

    <!-- 결과페이지 -->
    <div v-if="result">
      <genre-wc-card :genre-id="randGenreIdList[30]"></genre-wc-card>
      <div class="container">
        <div class="row bg-white bg-opacity-10 justify-content-center">
          <div class="slider">
            <div class="slides">
              <MovieCard
                v-for="movie in userLikeGenreMovieList"
                :movie="movie"
                :key="movie.id"
                class="col-lg-2 col-md-3 col-sm-4"
              ></MovieCard>
            </div>
          </div> 
        </div>
      </div>
    </div>
    <br>  
  </div>
</template>

<script>
import _ from 'lodash'
import GenreWcCard from '@/components/GenreWcCard.vue';
import axios from 'axios';
import {mapGetters} from 'vuex'
import drf from '@/api/drf'
import MovieCard from '@/components/MovieCard.vue'
const count = 20
export default {
  components: { GenreWcCard,MovieCard },
  name: 'GenreWc',

  data() {
    return {
      index:0,
      randGenreIdList:this.getRandGenreIdList(),
      result:'',
      userLikeGenreMovieList:[],
    };
  },

  created() {

  },
  computed:{
    ...mapGetters(['authHeader','currentUser'])
  },
  methods: {
    getRandGenreIdList(){
      const genreIdList=[12,14,16,18,27,28,35,36,37,53,80,99,878,9648,10402,10749,10751,10752,10770,]
      const randGenreIdList = _.sampleSize(genreIdList,16)
      return randGenreIdList
    },
    selected(id){
      this.randGenreIdList.push(id)
      this.index+=2
      if (this.index==30){
        this.result=id
        this.getUserLikeGenreMovieList()
        axios({
          url: drf.accounts.genre(this.currentUser.username,this.result),
          method: 'put',
          data: {
            username:this.currentUser.username
          },
          headers: this.authHeader,
        })

      }

    },
    getRound(){
      if(this.index<16) return 16
      else if(this.index<24) return 8
      else if (this.index<28) return 4
      else if (this.index<30) return 2
    },
    async getUserLikeGenreMovieList(){

      if (this.result===''){
        return
      }
      
      const indexList = _.sampleSize(_.range(1,500),500)
      let idx = 0
      let cnt = 0
      while (cnt < count){
        const response = await axios.get(drf.tmdb.popular(indexList[idx++]))
        
        response.data.results.forEach(element => {
          if (cnt >= count) return false

          // 포스터 패스 없을 시 continue
          if(!element.poster_path) return true

          element.genre_ids.forEach(id => {
            if (id == this.result){
              this.userLikeGenreMovieList.push(element)
              cnt++
              return false
            }
          })
        })
      }
    },
  },
};
</script>

<style lang="scss" scoped>
.text-box h1 {
  letter-spacing: 3vw;
  width:100%;
  font-size:5vw;
  text-align: center;
  color: #FF8307;
  text-shadow: 1.5px 1.5px black;
  margin: 0;
  // text-decoration: overline underline;
  // text-underline-position: under;
  // text-decoration-style: wavy;
}

// 슬라이더

* {
    box-sizing: border-box;
  }
  .slider {
    width: 100vw;
    text-align: center;
    border-radius: 10px;
    overflow: hidden;
  }
  
  .slides {
    display: flex;
    overflow-x: auto;
    /* overflow: hidden; */
    scroll-snap-type: x mandatory;
    scroll-behavior: smooth;
    -webkit-overflow-scrolling: touch;
  }
  .slides::-webkit-scrollbar {
    width: 10px;
    height: 10px;
  }
  .slides::-webkit-scrollbar-thumb {
    background: #ffffff50;
    border-radius: 10px;
  }
  .slides::-webkit-scrollbar-track {
    background: transparent;
  }
  .slides > div {
    scroll-snap-align: start;
    flex-shrink: 0;
    margin-right: 50px;
    border-radius: 10px;
    overflow: hidden;

    transform-origin: center center;
    transform: scale(1);
    transition: transform 0.5s;
    position: relative;
    
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 100px;
  }
  
  .author-info {
    background: rgba(0, 0, 0, 0.75);
    color: white;
    padding: 0.75rem;
    text-align: center;
    position: absolute;
    bottom: 0;
    left: 0;
    width: 100%;
    margin: 0;
  }
  .author-info a {
    color: white;
  }
</style>
<template>
  <div class="text-box">
    <br>
    <h1 class="p-3">장르 한번 골라보자!!</h1>
    <h3 class="p-3" style="font-size:4.5vw"> {{getRound()}}강 </h3>
    <div class="d-flex justify-content-between align-items-center" v-if="!result">
      <div class="background mx-3" @click="selected(randGenreIdList[index])">
        <genre-wc-card :genre-id="randGenreIdList[index]" ></genre-wc-card>
      </div>
      <span class="mx-2" style="font-size:4vw;">VS</span>
      <div class="background" @click="selected(randGenreIdList[index+1])">
        <genre-wc-card :genre-id="randGenreIdList[index+1]"></genre-wc-card>
      </div>
    </div>
    <div v-if="result">
      <p>결과</p>
      <genre-wc-card :genre-id="randGenreIdList[30]"></genre-wc-card>
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
export default {
  components: { GenreWcCard },
  name: 'GenreWc',

  data() {
    return {
      index:0,
      randGenreIdList:this.getRandGenreIdList(),
      result:'',
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
        axios({
        url: drf.accounts.genre(this.currentUser.username,this.result),
        method: 'put',
        data: {
          username:this.currentUser.username
        },
        headers: this.authHeader,
      })
      .then(res=>{
        console.log(res.data)
      })
      }
      console.log(this.randGenreIdList)
    },
    getRound(){
      if(this.index<16) return 16
      else if(this.index<24) return 8
      else if (this.index<28) return 4
      else if (this.index<30) return 2
    }
  },
};
</script>

<style lang="scss" scoped>
.text-box h1 {
  letter-spacing: 3vw;
  width:100%;
  font-size:5vw;
  text-align: center;
  // color: #FFF775;
  color: #d4ff2a;
  text-shadow: 4px 4px black;
  margin: 0;
  // text-decoration: overline underline;
  // text-underline-position: under;
  // text-decoration-style: wavy;
}
</style>
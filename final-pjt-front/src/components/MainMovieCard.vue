<template>
  <!-- <div> -->
    <img @click="routingDetail(movieId)" :src="backdropPath" alt="">
    <!-- <p>
      {{title}}
    </p> -->
  <!-- </div> -->
</template>

<script>
import router from '@/router'
export default {
  name: 'MainMovieCard',

  data() {
    return {
    
    }
  },
  props:{
    backdropPath:String,
    title:String,
    movieId:Number,
  },
  created(){
    
  },
  mounted() {
    
  },

  methods:{
    routingDetail(movieId){

      router.push({
        name:'detail',
        params:{movie_id:movieId}
        })
    },
  }
};
</script>

<style lang="scss" scoped>
img{
  cursor: pointer;
  width: 100%;
}
</style>
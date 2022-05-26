<template>
 
  <img class="py-5 animate__animated animate__bounce" :src="genreWcImgPath">


</template>

<script>
import 'animate.css'
export default {
  name: 'GenreWcCard',
  props:{
    genreId:Number
  },
  computed: {
    genreWcImgPath(){
      return require(`../assets/genre/${this.genreId}.png`)
    },
  },
  methods:{

  }
};
</script>

<style lang="scss" scoped>
img{
  width: 95%;
  height: auto;
  
}
// img:active{
//   position:relative; animation:ani .1s infinite;
// }
.animate__animated {
    --animate-duration  : 500ms;
    --animate-delay     : 0;
    }
#my-element {
    --animate-duration: 0.5s;
  }  

@keyframes ani {
  from{
    left:-10px
  }
  to{left:10px}
}
</style>
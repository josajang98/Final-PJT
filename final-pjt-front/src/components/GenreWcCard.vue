<template>
 <div class="container">
  <img class="py-5 mx-5 image" :src="genreWcImgPath">
 </div>


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
  width: auto;
  height: 80vh;
  
}
// img:active{
//   position:relative; animation:ani .1s infinite;
// }

.image:hover {
  animation: shake 0.82s cubic-bezier(.36,.07,.19,.97) both;
  transform: translate3d(0, 0, 0);
  backface-visibility: hidden;
  perspective: 150px;
}
@keyframes shake {
  10%, 90% {
    transform: translate3d(-1px, 0, 0);
  }
  
  20%, 80% {
    transform: translate3d(2px, 0, 0);
  }

  30%, 50%, 70% {
    transform: translate3d(-4px, 0, 0);
  }

  40%, 60% {
    transform: translate3d(4px, 0, 0);
  }
}


@keyframes ani {
  from{
    left:-10px
  }
  to{left:10px}
}
</style>
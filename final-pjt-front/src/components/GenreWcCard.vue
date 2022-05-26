<template>
  <img class="py-5" :src="genreWcImgPath">
</template>

<script>
export default {
  name: 'GenreWcCard',
  props:{
    genreId:Number
  },
  computed: {
    genreWcImgPath(){
      return require(`../assets/genre/${this.genreId}.png`)
    }
  },
};
</script>

<style lang="scss" scoped>
img{
  width: 400px;
  height: auto;
  
}
img:active{
  position:relative; animation:ani .1s infinite;
}
  
@keyframes ani {
  from{
    left:-10px
  }
  to{left:10px}
}

  
</style>
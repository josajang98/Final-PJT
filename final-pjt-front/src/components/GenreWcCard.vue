<template>
  <img :src="genreWcImgPath">
</template>

<script>

export default {
  name: 'GenreWcCard',

  data() {
    return {
      
    };
  },
  props:{
    genreId:Number
  },
  mounted() {
    
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
  width: 200px;
  height: 300px;
}
</style>
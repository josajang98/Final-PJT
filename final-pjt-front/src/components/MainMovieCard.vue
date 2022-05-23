<template>
  <div>
    <img :src="backdropPath" alt="">
    <p>
      {{title}}
    </p>
  </div>
</template>

<script>

export default {
  name: 'MainMovieCard',

  data() {
    return {
    
    }
  },
  props:{
    backdropPath:String,
    title:String,
  },
  created(){
    
  },
  mounted() {
    
  },

  methods: {
    
  },
};
</script>

<style lang="scss" scoped>

</style>
<template>
  <div>
    {{review.title}}
    {{review.content}}

  </div>
</template>

<script>
export default {
  name: 'ReviewCard',

  data() {
    return {
      
    };
  },
  props:{
    review:Object
  },
  mounted() {
    
  },

  methods: {
    
  },
};
</script>

<style lang="scss" scoped>

</style>
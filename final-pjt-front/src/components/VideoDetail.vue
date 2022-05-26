<template>
  <iframe 
  v-if="selectedVideo" 
  :src="videoUrl" 
  frameborder="0"
  width="640"
  height="380"
  ></iframe>
</template>

<script>
export default {
  name: 'VideoDetail',
  props:{
    selectedVideo: Object,
  },
  computed:{
    videoUrl(){
      const baseUrl = "https://www.youtube.com/embed/"
      const videoId = this.selectedVideo.id.videoId
      return baseUrl + videoId + '?autoplay=1&loop=1&playlist='+videoId
    }
  }
}
</script>

<style lang="scss" scoped>
div {
    position: relative;
}

/* iframe */
div > iframe {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
}
</style>
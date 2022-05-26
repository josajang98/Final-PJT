<template>
  <div>
    <iframe 
    v-if="selectedVideo" 
    :src="videoUrl" 
    frameborder="0"
    width="640"
    height="380"
    ></iframe>
  </div>
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
      return baseUrl + videoId + '?autoplay=1'
    }
  }
}
</script>

<style lang="scss" scoped>
div {
    position: relative;
    // padding-top: 56.25%;
    // height:0px;
    // overflow:hidden;
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
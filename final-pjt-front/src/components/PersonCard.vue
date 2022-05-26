<template>
  <div v-if="person.profile_path" class="d-flex align-items-center radius">
    <div  class="flex-shrink-0 img-wrapper">
      <img @click="routingDetail(person.id)" :src="profilePath" alt="">
    </div>
    <div class="flex-grow-1 ms-3">
      <p class=" font">{{person.name}}</p>
      <li style="font-size:15px">
        [ {{person.known_for_department}} ] 
        <span
        v-for="movie in person.known_for"
        :key="movie.id"
        style="font-size:15px"
        class="px-2"
        >
        {{movie.name?movie.name:movie.title}}
        </span>
      </li>
      
    </div>

  </div>
</template>

<script>
import router from '@/router'
const imgUrl='https://image.tmdb.org/t/p/w500/'
export default {
  name: 'PersonCard',
  props:{
    person:Object,
    index:Number
  },
  computed:{
    profilePath(){
      return imgUrl+this.person.profile_path
    }
  },
  methods:{
    routingDetail(personId){
      router.push({
        name:'personDetail',
        params:{
          person_id:personId,
          index:this.index
          }
      })
    },
  }

}
</script>

<style  lang="scss" scoped>
.font {
  font-size: 20px;
}
div {
  margin: 20px;
}
p{
  text-align: left;
}
.img-wrapper {
    position: relative;
    // width: 13vw;
    // height: 13vw;
    width: 100px;
    height: 100px;
}
.img-wrapper img {
  position: absolute;
  top: 0;
  left: 0;
  transform: translate(50, 50);
  width: 100%;
  height: 100%;
  object-fit: cover;
  margin: auto;
  border-radius: 20%;
}
li{
  list-style: circle;
  text-align: left;
}

</style>
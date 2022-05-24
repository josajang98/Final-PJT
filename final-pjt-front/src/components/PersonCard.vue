<template>
  <div>
    <img @click="routingDetail(person.id)" :src="profilePath" alt="">
    <p>{{person.name}}</p>
    <p>{{person.known_for_department}}</p>
    
    <!-- <p>{{person.known_for[0]}}</p> -->
  </div>
</template>

<script>
import router from '@/router'
const imgUrl='https://image.tmdb.org/t/p/w500/'
export default {
  name: 'PersonCard',
  props:{
    person:Object,
    // personProfilePath:String,
    // personName:String,
    // department:String,
    // movies:Array,
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
        params:{person_id:personId}
        })
    },
  }

}
</script>

<style  lang="scss" scoped>
div {
  margin: 20px;
}
img {
  width:200px;
  height:300px;
}
</style>
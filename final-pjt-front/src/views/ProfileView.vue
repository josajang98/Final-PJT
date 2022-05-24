<template>
  <div>
    <p></p>
  </div>
</template>

<script>
import {mapGetters} from 'vuex'
import axios from 'axios'
import drf from '@/api/drf'
export default {
  name: 'ProfileView',

  data() {
    return {
      userName:this.$route.params.username
    };
  },

  computed: {
    ...mapGetters(['authHeader'])
  },

  methods: {
    async getProfileData(){
      const response=await axios({
        url: drf.accounts.getProfile(this.userName),
        method: 'get',
        headers: this.authHeader,
      })
      console.log(response)
    }
  },
  created(){
    this.getProfileData()
  }
};
</script>

<style lang="scss" scoped>

</style>
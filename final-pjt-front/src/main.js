import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import swal from 'sweetalert'
import 'bootstrap-vue/dist/bootstrap-vue.css'

Vue.config.productionTip = false

new Vue({
  router,
  store,
  swal,
  render: h => h(App)
}).$mount('#app')

import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from 'vuex-persistedstate';


import accounts from './modules/accounts'
import articles from './modules/articles'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: { accounts, articles },


  //vuex-persistedstate
  plugins: [createPersistedState({
    paths: ["accounts"]
  })]

})

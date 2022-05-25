import axios from 'axios'
import drf from '@/api/drf'

// import accounts from './accounts'

export default {
  // namespaced: true,
  state: {
    personData: {},
  },

  getters: {
    personData: state => state.personData,

  },

  mutations: {
    SET_PERSON: (state, person) => state.personData = person,

  },

  actions: {
    async getPersonData({ commit }, query) {
      const response = await axios.get(drf.tmdb.searchPerson(query))
      commit('SET_PERSON', response.data.results)
      console.log(response.data.results)
    },

  },
}

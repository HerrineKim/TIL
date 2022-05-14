import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

const API_KEY = 'b62f75c838cebf4e82c9634fae139c52'
const API_URL = 'https://api.themoviedb.org/3/movie/now_playing'

export default new Vuex.Store({
  state: {
    MovieCards: [],
    MovieList: [],
  },
  getters: {
  },
  mutations: {
    MOVIE_CARD_GET: function (state, results) {
      state.MovieCards = results
    },
    CREATE_MOVIE_LIST: function (state, movieItem) {
      state.MovieList.push(movieItem)
    },
    DELETE_MOVIE_LIST: function (state, movieItem) {
      const idx = state.MovieList.indexOf(movieItem)
      state.MovieList.splice(idx, 1)
    }
  },
  actions: {
    movieCardGet({commit}) {
      axios({
        method: 'get',
        url: API_URL,
        params: {
          api_key: API_KEY,
          language: 'ko-KR'
        }
      }).then(response => {
        commit('MOVIE_CARD_GET', response.data.results)
      })

    },

    createMovieList: function (context, movieItem) {
      context.commit('CREATE_MOVIE_LIST', movieItem)
    },
    deleteMovieList: function (context, movieItem) {
      context.commit('DELETE_MOVIE_LIST', movieItem)
    },
  },
  modules: {
  }
})

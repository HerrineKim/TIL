<template>
  <div class="home">
      <h1>HomeView</h1>
      <movie-card
      v-for="MovieCard in MovieCards"
      :key="MovieCard.id"
      :movieCard="MovieCard"
      ></movie-card>
  </div>
</template>

<script>
import { mapState } from 'vuex'
// @ is an alias to /src

import MovieCard from '../components/MovieCard.vue'

export default {
  name: 'HomeView',
  components: {
    MovieCard,
  },
  computed: {
    ...mapState([
      'MovieCards',
    ])
  }
}
</script>

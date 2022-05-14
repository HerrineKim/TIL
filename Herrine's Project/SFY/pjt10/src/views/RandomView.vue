<template>
  <div>
    <h1>Random</h1>
    <button @click="pickRandom">Push me!</button>
    <img v-if="is_check === true" :src="`https://image.tmdb.org/t/p/w500${pickPosterPath}`" alt="">
    <br>
    
    <h2>{{ pickTitle }}</h2>
  </div>
</template>

<script>
import _ from 'lodash'
import {mapState} from 'vuex'

export default {
  name: 'RandomView',
  data: function (){
    return {
      pick: '',
      pickTitle: '',
      pickPosterPath: '',
      is_check: false,
    }
  },
  computed: {
    ...mapState([
      'MovieCards',
    ])
  },
  methods: {
    pickRandom: function () {
      const pick = _.sample(this.MovieCards)
      this.pickTitle = pick.title
      this.pickPosterPath = pick.poster_path
      console.log(this.pickPosterPath)
      this.is_check = true

    }
  },
}
</script>

<style>

</style>
<template>
  <div>
    <input type="text"
      v-model.trim="watchedMovie"
      @keyup.enter="createWatchedMovie"
      placeholder="내가 오늘 본 영화는"
    >
    <button
      @click="createWatchedMovie"
    >
    클릭!
    </button>
  </div>
</template>

<script>
export default {
  name: 'WatchListForm',
  data: function () {
    return {
      watchedMovie: '',
    }
  },
  methods: {
    createWatchedMovie: function () {
      const myMovie = this.watchedMovie
      if (myMovie) {
        this.$store.dispatch('createMovieList', myMovie)
      }
      this.watchedMovie = null
    }
  }

}
</script>

<style>

</style>
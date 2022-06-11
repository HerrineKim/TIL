<template>
  <div>
    <h1>My Movie List</h1>
    <watch-list-form></watch-list-form>
    <watch-list-item
    v-for="Movie in MovieList"
    :key="Movie"
    :Movie="Movie"
    >      
    </watch-list-item>
  </div>
</template>

<script>
import WatchListForm from '../components/WatchListForm.vue'
import WatchListItem from '../components/WatchListItem.vue'
import { mapState } from 'vuex'

export default {
  name: 'WatchList',
  components: {
    WatchListForm,
    WatchListItem
  },

  computed:{
    ...mapState([
      'MovieList',
    ])
  }
}
</script>

<style>

</style>
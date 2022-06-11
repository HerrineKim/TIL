<template>
<div>
  <img :src="`https://image.tmdb.org/t/p/w500${movieCard.poster_path}`" alt="이미지">
  <h1>{{ movieCard.title }}</h1>
  <p>{{ movieCard.overview }}</p>
  <br>
</div>

</template>

<script>
export default {
  name: 'MovieCard',
  props: {
    movieCard : Object,
  }

}
</script>

<style>

</style>
<template>
    <div class="container">
    <div id="movie_logo" class="m-5"> Like movies </div>
    <div class="d-flex row">
      <profile-movie-item v-for="movie in likeMovies"
      :movie="movie"
      :key="movie.id"></profile-movie-item>
    </div>
  </div>

</template>

<script>
import ProfileMovieItem from './ProfileMovieItem.vue'

export default {
  name: 'profile_movie_item',
  components: {
    ProfileMovieItem,
  },
  props: {
    likeMovies: Array,
  }
}
</script>

<style>

</style>
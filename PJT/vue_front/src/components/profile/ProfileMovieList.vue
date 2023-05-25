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
import ProfileMovieItem from '@/components/profile/ProfileMovieItem.vue'

export default {
  name: 'ProfileMovieList',
  components: {
    ProfileMovieItem,
  },
  props: {
    likeMovies: Array,
  }
}
</script>

<style>

#movie_logo {
    font-family: 'Noto Sans KR',  sans-serif;
    font-weight: 700;
    font-size: 2.0rem
  }

  #movie_logo:after {
  content: "";
  display: block;
  width: 85px;
  border-bottom: 2px solid #bcbcbc;
  margin: 3px auto;
  position: absolute;
  margin-left: 3px;
  }
</style>
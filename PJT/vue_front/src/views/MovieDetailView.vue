<template>
    <div class="login_logo display-4">
        MovieDetailView
        </div>
  </template>
  
<script>
import axios from "axios"

const URL = "https://api.themoviedb.org/3/movie/"
const API_KEY = process.env.VUE_APP_TMDB_API_KEY


export default {
  name: 'MovieDetailView',
  data: function() {
    return {      
      movie: this.$route.params.movie_id,
      moviePk: this.$route.params.movie_id,
      title: '',
    }
  },
  components: {},
  computed: {},
  methods: {},
  created() {
    axios.get(URL + this.movie, {
      params: {
        api_key: API_KEY, 
        language: 'ko-KR',
      }
    })
    .then(res => {
      alert(res.data)
      this.title = res.data.title
    })
    .catch(err => {
      alert(err)
    })
  },
}
</script>

<style>

</style>
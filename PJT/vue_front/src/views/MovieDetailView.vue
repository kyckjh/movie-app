<template>
    <div class="login_logo display-4">
        Movie Detail
        <div>
          <a :href="`http://localhost:8080/moviedetail/${ movie.id }`" >{{poster_path}}
            <div class="img">
              <img :src="poster_img" alt="poster">
            </div>
            </a>

          <h3>title: {{title}}</h3>
          <h3>overview: {{overview}}</h3>
          <h3>release_date : {{release_date }}</h3>
          <h3>popularity: {{popularity }}</h3>
          <h3>like_users: {{like_users}}</h3>
        </div>

        <hr>
        <movie-comment-list :movie_id="movie"></movie-comment-list>
    </div>
  </template>
  
<script>
import MovieCommentList from '@/components/movie/MovieCommentList.vue'

import axios from "axios"
import { mapActions, mapGetters } from "vuex"
const URL = "https://api.themoviedb.org/3/movie/"
const API_KEY = process.env.VUE_APP_TMDB_API_KEY


export default {
  name: 'MovieDetailView',
  data: function() {
    return {      
      movie: this.$route.params.movie_id,
      moviePk: this.$route.params.movie_id,
      poster_path : '',
      title: '',
      overview: '',
      release_date : '',
      popularity : '',
      like_users : '',
    }
  },
  components: {
    MovieCommentList,
  },
  computed: {
      ...mapGetters(['get_movie', 'isLiking', 'currentUser', 'get_movie_data']),
  },
  poster_img(){
            return "https://image.tmdb.org/t/p/original/" + this.poster_path
  },

  methods: {
    ...mapActions(['likeMovie', 'fetchCurrentUser', 'search']),
  },
  created() {
    axios.get(URL + this.movie, {
      params: {
        api_key: API_KEY, 
        language: 'ko-KR',
      }
    })
    .then(res => {
      //alert(res.data)
      this.title = res.data.title
      this.overview = res.data.overview
      this.release_date = res.data.release_date
      this.popularity  = res.data.popularity 
      this.poster_path  = res.data.poster_path 
      this.like_users = res.data.like_users
    })
    .catch(err => {
      alert(err)
    })
    this.fetchCurrentUser()
    this.search(this.movie)
  },
}
</script>

<style>

</style>
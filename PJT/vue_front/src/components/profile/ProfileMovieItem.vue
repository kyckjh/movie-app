<template>
    <div class="col-3 movie">
    <a :href="`http://localhost:8080/moviedetail/${ movie_id }`">
      <div class="containers" :style="`background: url('https://image.tmdb.org/t/p/original${poster_path}')`">
        <div class="overlay">
          <div class = "items"></div>
          <div class = "items head">
            <p>{{ title }}</p>
            <hr>
          </div>
        </div>
      </div>
    </a>
  </div>

</template>

<script>
import axios from "axios"
const URL = "https://api.themoviedb.org/3/movie/"
const API_KEY = process.env.VUE_APP_TMDB_API_KEY

export default {
    name: "profile_movie_item",
    props: {
        movie: Object,
    },
    data: function() {
        return {
            title: '',
            poster_path: '',
            movie_id: '',
        }
    },
    created() {
        axios.get(URL + this.movie.movie_id, {
            params: {
                api_key: API_KEY,
                language: 'ko-KR',
            }
        })
        .then(res => {
            this.title = res.data.title
            this.poster_path = res.data.poster_path
            this.movie_id = res.data.id
        })
        .catch(err => console.log(err))
    }
}
</script>

<style>

</style>
<template>
    <div class="col-3 movie">
    <a class="containers" :href="`http://localhost:8080/moviedetail/${ movie_id }`">
      <img :src="like_poster" alt="like_poster">
          <div class = "items"></div>
          <div class = "items head">
            <p>{{ title }}</p>
            <hr>

      </div>
      </a>
  </div>

</template>

<script>
import axios from "axios"
const URL = "https://api.themoviedb.org/3/movie/"
const API_KEY = process.env.VUE_APP_TMDB_API_KEY

export default {
    name: "ProfileMovieItem",
    props: {
        movie: Object,
    },
    data: function(){
        return {
            title: '',
            poster_path: '',
            movie_id: '',
        }
    },
    created(){
        axios.get(URL + this.movie.id, {
            params: {
                api_key: API_KEY,
                language: 'ko-KR',
            }
        })
        .then(res => {
            this.title = res.data.title
            this.poster_path = res.data.poster_path
            this.movie_id = res.data.id
            console.log(res)
        })
        .catch(err => console.log(err))
    },
    computed: {
      like_poster() {
        const test = "https://image.tmdb.org/t/p/original/" + this.poster_path
        console.log(test)
        return  "https://image.tmdb.org/t/p/original" + this.poster_path
        
      }
    }
}
</script>

<style scoped>
img {
  width: 100%;
  height: 200px;
  overflow: hidden;
}
</style>
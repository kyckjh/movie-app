<template>
    <div>
      <div class="trand">for You</div>
      
      <div>
          <carousel v-if="movies.length > 0">            
              <recommand-item v-for="movie in movies" :key="movie.id" :movie="movie"></recommand-item>
          </carousel>
      </div>
    </div>
  </template>
  
  <script>
  import RecommandItem from './RecommandItem.vue'
  import carousel from "vue-owl-carousel2";
  
  import axios from "axios"
  const URL = "https://api.themoviedb.org/3/movie/now_playing"
  const API_KEY = process.env.VUE_APP_TMDB_API_KEY
  
  export default {
      name: 'MainCardList',
      components: {
        RecommandItem,
          carousel
      },
      data: function() {
          return {
              movies: {},
          }
      },
      created() {
          axios.get(URL, {
              params: {
                  api_key: API_KEY,
                  language: "ko-KR",
                  region: "KR"
              }
          })
          .then(res => {
              this.movies = res.data.results.slice(0, 10)
          })
          .catch(err => {
              console.log(err)
          })
      }
  }
  </script>
  
  <style>
  .trand {
      margin: 15px;
  }
  </style>
<template>
  <div>
    <div v-if="num == 1">Trending</div>
    <div v-else>Animation</div>
    
    <div>
        <carousel v-if="movies.length > 0">            
            <main-card-item v-for="movie in movies" :key="movie.id" :movie="movie"></main-card-item>
        </carousel>
    </div>
  </div>
</template>

<script>
import MainCardItem from './MainCardItem.vue'
import carousel from "vue-owl-carousel2";

import axios from "axios"
const URL = "https://api.themoviedb.org/3/movie/now_playing"
const API_KEY = process.env.VUE_APP_TMDB_API_KEY
const URL2 = "http://localhost:8000/api/v1/recommend/"

export default {
    name: 'MainCardList',
    components: {
        MainCardItem,
        carousel
    },
    props: {
        num: Number,
    },
    data: function() {
        return {
            movies: {},
            animations: {},
        }
    },
    created() {
        if (this.num == 1){
            axios.get(URL, {
                params: {
                    api_key: API_KEY,
                    language: "ko-KR",
                    region: "KR"
                }
            })
            .then(res => {
                this.movies = res.data.results.slice(0, 100)
            })
            .catch(err => {
                console.log(err)
            })
        }
        else {            
            axios({                
                url: URL2,
                method: 'get',            
            })
            .then(res => {
                //console.log(res.data)
                this.movies = res.data.slice(0, 100)
            })
            .catch(err => {
                console.log(err)
            })
        }
    }
}
</script>

<style>
.trand {
    margin: 15px;
}
</style>
<template>
    <div>
        <div id="owl">
        <h1>asdf</h1>

        <span v-for="actor in actor_ids" :key="actor">actor: {{ actor }}</span>

        <carousel v-if="actor_ids.length > 0">
        <actors-item v-for="actor in actor_ids" 
        :key="actor"
        :actor="actor">{{ actor }}</actors-item>
      </carousel>
    </div>
  </div>

</template>

<script>
import ActorsItem from '@/components/movie/ActorsItem.vue'
import carousel from "vue-owl-carousel2"
import axios from "axios"
import { mapGetters, mapActions } from 'vuex'

// const URL = "https://api.themoviedb.org/3/movie"
// const API_KEY = process.env.VUE_APP_TMDB_API_KEY

export default {
    name: 'actors_list',
    components: {
        ActorsItem,
        carousel,
    },
    props: {
        movie_Number: Number,
    },
    data: function() {
        return {
        actorform: {
            movie_id: this.$route.params.movie_id,
            name: "",
        },
        movies: {},
        actor_ids: [],
        num: 0,
        }
    },
    methods: {
    ...mapActions(['fetchCurrentUser']),
    add(){
        this.num++
    },
    },
    computed: {
    ...mapGetters(['isLoggedIn', "get_comments", 'get_movie', 'currentUser', ]),
    },
    created() {
        // axios.get(URL + this.movie + "/credits", {
        //     params: {
        //         api_key: API_KEY,
        //     }
        // })
        // .then(res => {
        //     this.actors = res.data.cast.slice(0, 10)
        // })
        // .catch(err => {
        //     console.log(err)
        // })        
        axios.get("http://localhost:8000/api/v1/" + this.$route.params.movie_id + "/", {})
        .then(res => {
            console.log('movies:             ')
            console.log(res.data)
            this.movies = res.data
            console.log(this.movies.actor_ids)
            this.actor_ids = this.movies.actor_ids
            console.log(this.actor_ids.length)
        }),
        this.fetchCurrentUser()
    }
}
</script>

<style>

</style>
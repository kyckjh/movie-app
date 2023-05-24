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

const URL = "https://api.themoviedb.org/3/movie"
const API_KEY = process.env.VUE_APP_TMDB_API_KEY

export default {
    name: 'actors_list',
    components: {
        ActorsItem,
        carousel,
    },
    props: {
        movie: String,
        actor_ids: Array,
    },
    data: function() {
        return {
            actors: {},
        }
    },
    created() {
        axios.get(URL + this.movie + "/credits", {
            params: {
                api_key: API_KEY,
            }
        })
        .then(res => {
            this.actors = res.data.cast.slice(0, 10)
        })
        .catch(err => {
            console.log(err)
        })
    }
}
</script>

<style>

</style>
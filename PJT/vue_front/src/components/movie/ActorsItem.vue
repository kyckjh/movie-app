<template>
    <div class="m-3 carousel card">
        <div class="carousel-bg"></div>
        <img v-if="image_path == null" 
        src="@/assets/annonymous.jpg" alt="actor">
        <img v-else :src="actorImg" alt="actor">
        <p class="carousel-text">name: {{name}}  character: {{ character }}</p>
  </div>

</template>

<script>
import axios from "axios"
import { mapActions, mapGetters } from 'vuex'

export default {
    name: 'actors_item',
    data() {
        return {
            name: "",
            character: "",
            image_path: "",
        }
    },
    methods: {
        ...mapActions(['create_movie_Comment', 'fetchCurrentUser']),
        add(){
        this.num++
    },
  },
    props: {
        actor: Number
    },
    computed: {
        ...mapGetters(['isLoggedIn', "get_comments", 'get_movie', 'currentUser', ]),
        actorImg() {
            return "https://image.tmdb.org/t/p/w500" + this.image_path
        },
    },
    created() {
        axios.get("http://localhost:8000/api/v1/actors/" + this.actor + "/", {})
        .then(res => {
            this.actors = res.data
            this.name = this.actors.name
            this.character = this.actors.character
            this.image_path = this.actors.image_path
            //console.log('name: ', this.actors)
            //console.log('image: ', this.actors.image_path)
        }),
        this.fetchCurrentUser()
    }
}
</script>

<style>

</style>
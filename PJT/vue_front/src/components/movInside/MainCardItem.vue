<template>
  <div>
    <div>
        <a :href="`http://localhost:8080/moviedetail/${ movie.id }`" ></a>
        <div class="img">
            <img :src="poster_img" alt="poster">
        </div>
    </div>
  </div>
</template>

<script>
export default {
    name: "MovieCardItem",
    props: {
        movie: Object,
    },
    computed: {
        poster_img(){
            return "https://image.tmdb.org/t/p/original/" + this.movie.poster_path
        }
    }
}
</script>

<style>

</style>
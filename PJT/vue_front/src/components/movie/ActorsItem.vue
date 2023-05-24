<template>
    <div class="m-3 carousel card">
      <p class="carousel-text">{{actor}}</p>
      <div class="carousel-bg"></div>
      <img v-if="actor.profile_path == null" 
      src="@/assets/annonymous.jpg" alt="actor">
      <img v-else :src="actorImg" alt="actor">
  </div>

</template>

<script>
export default {
    name: 'actors_item',
    props: {
        actor: Number
    },
    computed: {
        actorImg() {
            return "https://imge.tmdb.org/t/p/w500/" +this.actor.profile_path
        },
    }

}
</script>

<style>

</style>
<template>
    <div>
        <profile-item></profile-item>
        <profile-movie-list :likeMovies="profile.like_movies">
        </profile-movie-list>
    </div>
</template>

<script>
import ProfileItem from '../components/profile/ProfileItem.vue'
import ProfileMovieList from '../components/profile/ProfileMovieList.vue'
import { mapGetters, mapActions } from 'vuex'

export default {
    name: 'ProfilePageView',
    components: {
        ProfileItem,
        ProfileMovieList,
    },
    computed: {
        ...mapGetters(['profile'])
    },
    methods: {
        ...mapActions(['fetchProfile'])
    },
    created() {
        const payload = { username: this.$route.params.username }
        this.fetchProfile(payload)
    }

}
</script>

<style>

</style>
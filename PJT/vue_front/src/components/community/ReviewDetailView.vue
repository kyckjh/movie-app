<template>
    <div class="login_logo display-4">
        ReviewDetailView
        <p>username: {{review.user}}</p>
        <p>title: {{ review.title }}</p> 
        <p>content: {{ review.content }}</p> 
    </div>
  </template>
  
  <script>

  //import axios from "axios"
  import { mapActions, mapGetters } from "vuex"
  //const URL = "https://api.themoviedb.org/3/movie/"
  //const API_KEY = process.env.VUE_APP_TMDB_API_KEY

  export default {
    name: 'ReviewDetailView',
    data: function() {
    return {      
      reviewPk: this.$route.params.review_id,
      title: '',
      content: '',
      username: '',
    }
  },
    components: {},
    computed: {
      ...mapGetters(['review'])
    },
    methods: {
      ...mapActions(['fetchReview'])
    },
    created() {
      this.fetchReview(this.reviewPk)
    },
  }
  </script>
  
  <style>
  
  </style>
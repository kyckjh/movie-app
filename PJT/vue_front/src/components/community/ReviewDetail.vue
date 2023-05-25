<template>
    <div class="login_logo display-4 text-start">
    <div class="container">
      <div class="row mt-5">
        <div class="row back-op ms-0">
          <div class="col-md-2 col-sm-3">
            <a :href="poster_img" >
                <div class="img">
                  <img class="w-100" :src="poster_img" alt="poster">
                </div>
            </a>
          </div>
          <div class="col-md-10 col-sm-10">
            <p class="fs-3">{{ movie_title }}</p>
            <p>{{ review.title }}</p> 
            <p class="fs-5">{{ review.updated_at.slice(0, 4) }}년 {{ review.updated_at.slice(5, 7) }}월 {{ review.updated_at.slice(8, 10) }}일에 작성됨</p>
          </div>
        </div>
        <p class="back mt-4 fs-5">{{ review.content }}</p> 
      </div>
    </div>
    </div>
  </template>
  
  <script>

  import axios from "axios"
  import { mapActions, mapGetters } from "vuex"
  const URL = "https://api.themoviedb.org/3/movie/"
  const API_KEY = process.env.VUE_APP_TMDB_API_KEY

  export default {
    name: 'ReviewDetail',
    data: function() {
    return {      
      reviewPk: this.$route.params.review_id,
      title: '',
      content: '',
      username: '',

      poster_path : '',
      movie_title: '',
      overview: '',
      release_date : '',
      popularity: '',
      like_users: [],
      vote_average: '',
      genre_ids: [],
      backdrop_path: '',
      is_liking: false,
    }
  },
    components: {},
    computed: {
      ...mapGetters(['review']),
      poster_img(){
        return "https://image.tmdb.org/t/p/original/" + this.poster_path
    },
    },
    methods: {
      ...mapActions(['fetchReview'])
    },
    created() {
    this.fetchReview(this.reviewPk)
    
    setTimeout(() => {
      axios.get(URL + this.review.movie, {
      params: {
        api_key: API_KEY, 
        language: 'ko-KR',
      }
    })
    .then(res => {
      console.log('>>>>>>>>>>>>>>>>>>>>>>')
      console.log(res.data)
      this.movie_title = res.data.title
      this.overview = res.data.overview
      this.release_date = res.data.release_date
      this.popularity  = res.data.popularity 
      this.poster_path  = res.data.poster_path 
      this.like_users = res.data.like_users
      this.vote_average = res.data.vote_average
      this.genre_ids = res.data.genres
      this.backdrop_path = res.data.backdrop_path
    })
    .catch(err => {
      alert(err)
    })
    }, 500);
    
  },
  }
  </script>
  
  <style>
  .back-op {
    background-color: rgba(179, 179, 179, 0.1);
    padding: 25px;
  }
  .back {
    padding: 25px;
    background-color: rgba(0, 0, 0, 0.3);
    font-size: 30px;
  }
  </style>
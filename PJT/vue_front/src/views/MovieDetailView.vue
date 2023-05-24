<template>
    <div class="login_logo display-4">
        Movie Detail
        <div>
            <button id="follow" @click="likeMovie(moviePk)" 
            class="heart-button" 
            :class="{active : isLiking}">
              <div class="heart-flip"></div>
              <span>Like<span>d</span></span>
            </button>
          </div>
        <div>
          <a :href="`http://localhost:8080/moviedetail/${ movie.id }`" >
            <div class="img">
              <img :src="poster_img" alt="poster">
            </div>
            </a>

          <h3>제목: {{title}}</h3>
          <h5>줄거리: {{overview}}</h5>
          <h3>개봉일 : {{release_date }}</h3>
          <h3>관객 수 : {{popularity }}</h3>
          <!-- <h3>like users: {{like_users}}</h3> -->
          <h3>평점: {{ vote_average }}</h3>
        </div>
        <actors-list :movie_id="movie"></actors-list>

        <hr>
        <movie-comment-list :movie_id="movie"></movie-comment-list>
    </div>
  </template>
  
<script>
import MovieCommentList from '@/components/movie/MovieCommentList.vue'
import ActorsList from '@/components/movie/ActorsList.vue'

import axios from "axios"
import { mapActions, mapGetters } from "vuex"
const URL = "https://api.themoviedb.org/3/movie/"
const API_KEY = process.env.VUE_APP_TMDB_API_KEY


export default {
  name: 'MovieDetailView',
  data: function() {
    return {      
      movie: this.$route.params.movie_id,
      moviePk: this.$route.params.movie_id,
      poster_path : '',
      title: '',
      overview: '',
      release_date : '',
      popularity: '',
      like_users: [],
      vote_average: '',
    }
  },
  components: {
    MovieCommentList,
    ActorsList,
  },
  computed: {
      ...mapGetters(['get_movie', 'isLiking', 'currentUser', 'get_movie_data']),
    poster_img(){
        return "https://image.tmdb.org/t/p/original/" + this.poster_path
    },
  },
  methods: {
    ...mapActions(['likeMovie', 'fetchCurrentUser', 'search']),
    click_actor: function() {
      if (this.menubar === false) {
        this.menubar = true
        const actors = document.querySelector("#actors")
        const s_movie = document.querySelector("#s_movie")
        actors.classList.add('class', 'actived')
        s_movie.classList.remove('class', 'actived')
      }
    },
    click_s_movie: function() {
      if (this.menubar === true) {
        this.menubar = false
        const actors = document.querySelector("#actors")
        const s_movie = document.querySelector("#s_movie")
        actors.classList.remove('class', 'actived')
        s_movie.classList.add('class', 'actived')
      }
    }

  },
  created() {
    axios.get(URL + this.movie, {
      params: {
        api_key: API_KEY, 
        language: 'ko-KR',
      }
    })
    .then(res => {
      //alert(res.data)
      this.title = res.data.title
      this.overview = res.data.overview
      this.release_date = res.data.release_date
      this.popularity  = res.data.popularity 
      this.poster_path  = res.data.poster_path 
      this.like_users = res.data.like_users
      this.vote_average = res.data.vote_average

    })
    .catch(err => {
      alert(err)
    })
    this.fetchCurrentUser()
    this.search(this.movie)
  },
  mounted() {
    document.querySelectorAll('.heart, .heart-button')
    .forEach(button => button.addEventListener('click', () => button.classList.toggle('active')));
  },

}
</script>

<style>
  .heart,
  .heart-button {
    cursor: pointer;
    outline: none;
    -webkit-appearance: none;
    -webkit-tap-highlight-color: transparent;
  }
  .heart .heart-flip,
  .heart-button .heart-flip {
    --base: 32px;
    --duration: .6s;
    --active: #ea4673;
    --inactive: #d1d6ee;
    width: var(--base);
    height: calc(var(--base) + var(--base) / 2);
    border-radius: calc(var(--base) / 2) calc(var(--base) / 2) 0 0;
    position: relative;
    transform-origin: 50% 66.66%;
    transform-style: preserve-3d;
    transform: rotate(var(--rotate, -45deg));
    transition: background var(--duration), transform var(--duration) ease;
    background: var(--heart-background, var(--inactive));
  }
  .heart .heart-flip:before, .heart .heart-flip:after,
  .heart-button .heart-flip:before,
  .heart-button .heart-flip:after {
    content: "";
    width: calc(var(--base) / 2);
    height: var(--base);
    border-radius: var(--pseudo-border-radius, calc(var(--base) / 2) 0 0 calc(var(--base) / 2));
    position: absolute;
    left: var(--pseudo-left, -50%);
    transform-origin: var(--pseudo-origin, 100%) 50%;
    bottom: 0;
    background: var(--heart-background, var(--inactive));
    filter: brightness(var(--pseudo-filter, 50%));
    transform: translateX(1%) rotateY(var(--pseudo-rotate, 90deg)) translateZ(0);
    transition: background var(--duration), transform var(--duration) ease, filter var(--duration);
  }
  .heart .heart-flip:after,
  .heart-button .heart-flip:after {
    --pseudo-border-radius: 0 calc(var(--base) / 2) calc(var(--base) / 2) 0;
    --pseudo-left: 100%;
    --pseudo-origin: 0;
    filter: brightness(var(--pseudo-filter-second, 100%));
    transform: translateX(-1%) rotateY(var(--pseudo-rotate-second, 0deg)) translateZ(0);
  }
  .heart.active .heart-flip,
  .heart-button.active .heart-flip {
    --rotate: 45deg;
    --pseudo-filter: 100%;
    --pseudo-filter-second: 50%;
    --pseudo-rotate: 0deg;
    --pseudo-rotate-second: 90deg;
    --heart-background: var(--active);
  }

  .heart {
    background: none;
    border: none;
    padding: 0;
    transform: scale(var(--button-scale, 1)) translateZ(0);
    transition: transform 0.2s;
  }
  .heart:active {
    --button-scale: .95;
  }

  .heart-button {
    --duration: .4s;
    --color: #404660;
    --color-hover: #2b3044;
    --color-active: #fff;
    --border: #d1d6ee;
    --border-hover: #bbc1e1;
    --border-active: #ea4673;
    --background: #fff;
    --background-active: #ea4673;
    font-family: inherit;
    font-size: 14px;
    line-height: 1.6;
    font-weight: 600;
    padding: 6px 16px;
    border-radius: 7px;
    color: var(--button-color, var(--color));
    border: 1px solid var(--button-border, var(--border));
    background: var(--button-background, var(--background));
    transform: scale(var(--button-scale, 1)) translateZ(0);
    transition: background var(--duration), border-color var(--duration), color var(--duration), transform 0.2s;
  }
  .heart-button .heart-flip {
    --base: 8px;
    --active: #fff;
    --inactive: #bbc1e1;
    display: inline-block;
    vertical-align: top;
    margin: 4px 6px 0 0;
  }
  .heart-button span {
    display: inline-block;
    vertical-align: top;
  }
  .heart-button > span {
    transform: translateX(var(--text-x, 4px));
    transition: transform var(--duration);
  }
  .heart-button > span span {
    display: inline-block;
    vertical-align: top;
    opacity: var(--span-opacity, 0);
    transform: translateX(var(--span-x, 4px));
    transition: opacity var(--duration), transform var(--duration);
  }
  .heart-button:active {
    --button-scale: .95;
  }
  .heart-button:hover {
    --button-color: var(--color-hover);
    --button-border: var(--border-hover);
  }
  .heart-button.active {
    --text-x: 0;
    --button-color: var(--color-active);
    --button-border: var(--border-active);
    --button-background: var(--background-active);
    --span-opacity: 1;
    --span-x: 0;
  }

</style>
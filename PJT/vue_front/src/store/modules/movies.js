import router from '@/router';
import axios from 'axios'
import drf from '@/api/drf'
import _ from 'lodash'

// import { _ } from 'core-js';
 const URL = "https://api.themoviedb.org/3/search/movie"
 const API_KEY = process.env.VUE_APP_TMDB_API_KEY

 export default{
    state: {
        //token: "",
        movie_data: {},
        movie: localStorage.getItem('movie') || {},
        //movie: {},
        comments: {},
        currentUser: {},
    },
    getters: {
       currentUser: state => state.currentUser,
       get_movie_data: state => state.movie_data,
       get_movie: state => state.movie,
       get_comments: state => state.comments,
       isLike: state => _.some(state.movie_data.like_user,{"pk":state.currentUser.pk}),
    },
    mutations: {
        SET_CURRENT_USER: (state, user) => state.currentUser = user,
        SET_MOVIE_DATA: (state, movie) => state.movie_data = movie,
        SET_MOVIE_ID: (state, movie) => state.movie = movie,
        SET_COMMENT: (state, comments) => state.comments = comments,
        SET_MOVIES_COMMENT: (state, comments) =>(state.movie.comment = comments),
    },
    actions:{
        search: function({ commit }, movie_id ) {
            axios({
                url: drf.movies.movie(movie_id),
                method: 'get',
            })
            .then(res => {
                console.log('movie ' + res.data.id);
                console.log(res.data)
                localStorage.setItem('movie', res.data.id)
                commit("SET_MOVIE_ID", movie_id)
                commit("SET_MOVIE_DATA", res.data)
                axios({
                    url:
                    'http://localhost:8000/api/v1/' +
                    res.data.id +
                    '/comments/',
                    method: 'get',
                })
                    .then((res) => {
                    console.log(res.data);
                    commit("SET_COMMENT", res.data)
                    })
                    .catch((err) => {
                    if (err.response.status === 404) {
                        commit("SET_MOVIES_COMMENT", {})
                        router.push({
                          name: 'MovieDetailView',
                          params: { movie_id: movie_id.toString() },
                        });
                    }
                    });
                router.push({ name: 'MovieDetailView', params: { movie_id: movie_id.toString()}}).catch(err => err)
            })
            .catch(err => {
                alert(err)
                console.log(err)
                router.push({ name: 'MainView'}).catch(err => err)
            })
        },

        search_movie_ID: function ({ commit, dispatch }, search_movie) {
            axios.get(URL, {
                params: {
                    api_key: API_KEY,
                    language: 'ko-KR',
                    query: search_movie,
                }
            })
            .then(res => {
                console.log(res.data)
                console.log('movie id: '+res.data.results[0].id)
                const movie_id = res.data.results[0].id
                dispatch("search", movie_id)
                commit("SET_MOVIE_DATA", res.data.results[0])
            })
            .catch(err => {
                console.log(err)
            })
            .catch(err => {
                console.log(err)
                router.push({ name: 'MainView' }).catch((err) => err);
            })
        },
        create_movie_Comment({ commit, getters }, { movie_id, content}) {
            console.log(movie_id)
            console.log(content)
            const comment = { content, }
            console.log(comment)
            axios({
                url: drf.movies.movie_comment(movie_id),
                method: 'post',
                data: comment,
                headers: getters.authHeader,
            })
            .then(res => {
                commit('SET_MOVIES_COMMENT', res.data)
            })
            .catch(err => console.error(err.response))
        },
        likeMovie({ commit, getters }, moviePk) {
            /* 좋아요
            POST: likeMovie URL(token)
              성공하면
                state.article 갱신
              실패하면
                에러 메시지 표시
            */
            axios({
              url: drf.movies.likeMovie(moviePk),
              method: 'post',
              headers: getters.authHeader,
            })
              .then(res => commit('SET_MOVIE_DATA', res.data))
              .catch(err => console.error(err.response))
          },
      },
    
  
 }
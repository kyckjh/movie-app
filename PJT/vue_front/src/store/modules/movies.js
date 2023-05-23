// import router from '@/router';
// import { _ } from 'core-js';
//  const URL = "https://api.themoviedb.org/3/search/movie"
//  const API_KEY = process.env.VUE_APP_TMDB_API_KEY

//  export default{
//     state: {
//         //token: "",
//         movie_data: {},
//         movie: localStorage.getItem('movie') || {},
//         //movie: {},
//         comments: {},
//         currentUser: {},
//     },
//     getters: {
//        currentUser: state => state.currentUser,
//        get_movie_data: state => state.movie_data,
//        get_movie: state => state.movie,
//        get_comments: state => state.comments,
//        isLike: statee => _.some(state.movie_data.like_user,{"pk":state.currentUser.pk}),
//     },
//     mutations: {
//         SET_CURRENT_USER: (state, user) => state.currentUser = user,
//         SET_MOVIE_DATA: (state, movie) => state.movie_data = movie,
//         SET_MOVIE_ID: (state, movie) => state.movie = movie,
//         SET_COMMENT: (state, comments) => state.comments = comments,
//         SET_MOVIES_COMMENT: (state, comments) =>(state.movie.comment = comments),
//     },
//     actions:{
//         search: function({ commit }, movie_id ) {
//             axios({
//                 url: DocumentFragment.movie.movie(movie_id),
//             })
//         }
//     }
//  }
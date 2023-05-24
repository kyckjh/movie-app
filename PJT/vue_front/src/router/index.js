import Vue from 'vue'
import VueRouter from 'vue-router'
// import store from '../store'

import MainView from '../views/MainView.vue'
import SignUpView from '@/views/SignUpView'
import LoginView from '@/views/LoginView'
import LogoutView from '@/views/LogoutView.vue'

import MovieDetailView from '@/views/MovieDetailView.vue';

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'MainView',
    component: MainView,
  },
  {
    path: '/signup',
    name: 'SignUpView',
    component: SignUpView,
  },
  {
    path: '/login',
    name: 'LoginView',
    component: LoginView,
  },
  {
    path: '/logout',
    name: 'LogoutView',
    component: LogoutView,
  },
  {
    path: '/moviedetail/:movie_id',
    name: 'MovieDetailView',
    component: MovieDetailView,
  },
  // {
  //   path: '/community',
  //   name: 'community',
  //   component: CommunityView
  // },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router

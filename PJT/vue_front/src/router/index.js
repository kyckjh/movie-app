import Vue from 'vue'
import VueRouter from 'vue-router'
// import store from '../store'

import MainView from '../views/MainView.vue'
import SignUpView from '@/views/SignUpView'
import LoginView from '@/views/LoginView'
import LogoutView from '@/views/LogoutView.vue'
import ProfileView from '@/views/ProfilePageView.vue'

import MovieDetailView from '@/views/MovieDetailView.vue';

import CommunityView from '@/views/CommunityView.vue'
import CommunityList from '@/components/community/CommunityList.vue'
import ReviewDetailView from '@/components/community/ReviewDetail.vue';
import CommunityCreateView from '@/views/CommunityCreateView.vue'

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
  {
    path: '/profile/:username',
    name: 'ProfilePageView',
    component: ProfileView,
  },
  {
    path: '/reviewdetail/:review_id',
    name: 'ReviewDetail',
    component: ReviewDetailView,
  },
  {
    path: '/community',
    name: 'CommunityView',
    component: CommunityView
  },
  {
    path: '/community/create',
    name: 'CommunityCreateView',
    component: CommunityCreateView
  },
  {
    path: '/community/reviews',
    name: 'CommunityList',
    component: CommunityList
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router

import router from '@/router'
import axios from 'axios'
import drf from '@/api/drf'
import { _ } from 'core-js'

export default {
    state: {
        token: localStorage.getItem('token') || '' ,
        currentUser: {},
        profile: {},
        authError: null,
    },
    
    // 모든 state는 getters 를 통해서 접근하겠다.
    getters: {
        isLoggedIn: state => !!state.token,
        currentUser: state => state.currentUser,
        profile: state => state.profile,
        notMyAccount: (state) => {
            return state.profile.username !== state.currentUser
        },
        isFollowing: state => _.includes(state.profile.followers, state.currentUser.pk),
        authError: state => state.authError,
        authHeader: state => ({Authorization: `Token ${state.token}`})
    },

    mutations: {
        SET_TOKEN: (state, token) => state.token = token,
        SET_CUTTENT_USER: (state, user) => state.currentUser = user,
        SET_PROFILE: (state, profile) => state.profile = profile,
        // SET_PROFILE_IMG: (state, profile_img) => state.profile.profile_img = profile_img,
        SET_AUTH_ERROR: (state, error) => state.authError = error
    },

    actions: {
        followProfile({ commit, getters}, username) {

        }
    }

}
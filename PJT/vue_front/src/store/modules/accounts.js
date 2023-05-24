import router from '@/router'
import axios from 'axios'
import drf from '@/api/drf'
import _ from 'lodash'
// import { _ } from 'core-js'

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
            return state.profile.username !== state.currentUser.username
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
            axios({
                url: drf.accounts.follow(username),
                method: 'post',
                headers: getters.authHeader,
            })
            .then(res => {
                console.log(res)
                commit('SET_PROFILE', res.data)
            })
            .catch(err => {
                console.error(err.response)
            })
        },
        saveToken({ commit }, token) {
            commit('SET_TOKEN', token)
            localStorage.setItem('token', token)
        },

        removeToken({ commit }) {
            commit('SET_TOKEN', '')
            localStorage.setItem('token', '')
        },
        login({ commit, dispatch }, credentials) {
            axios({
                url: drf.accounts.login(),
                method: 'post',
                data: credentials
            })
            .then(res => {
                //alert(res)
                const token = res.data.key
                dispatch('saveToken', token)
                dispatch('fetchCurrentUser')
                router.push({ name: 'MainView' })
            })
            .catch(err => {
                //alert(err)
                console.error(err.response.data)
                commit('SET_AUTH_ERROR', err.response.data)
            })
        },
        signup({ commit, dispatch }, credentials) {
            axios({
                url: drf.accounts.signup(),
                method: 'post',
                data: credentials
            })
            .then(res => {
                const token = res.data.key
                dispatch('saveToken', token)
                dispatch('fetchCurrentUser')
                router.push({ name: 'MainView' })
            })
            .catch(err => {
                console.error(err.response.data)
                commit('SET_AUTH_ERROR', err.response.data)
            })
        },

        logout({ getters, dispatch }) {
            axios({
                url: drf.accounts.logout(),
                method: 'post',
                headers: getters.authHeader,
            })
            .then(() => {
                dispatch('removeToken')
                alert('Log out.')
                router.push({ name: 'LoginView' })
            })
            .catch(err => {
                console.error(err.response)
            })
        },
        fetchCurrentUser({ commit, getters, dispatch }) {
            if (getters.isLoggedIn) {
                axios({
                    url: drf.accounts.currentUserInfo(),
                    method: 'get',
                    headers: getters.authHeader,
                })
                .then(res => commit('SET_CURRENT_USER', res.data),
                console.log("패치커런트유저 어카운츠스테이트")
                )
                .catch(err => {
                    if (err.response.status === 401) {
                        dispatch('removeToken')
                        console.log("패치커런트유저 어카운츠스테이트")

                        router.push({ name: 'LoginView' });
                    }
                })
            }
        },
        fetchProfile({ commit, getters }, { username }) {
            axios({
                url: drf.accounts.profile(username),
                method: 'get',
                headers: getters.authHeader,
            })
            .then(res => {
                commit('SET_PROFILE', res.data)
            })
        }
    }

}
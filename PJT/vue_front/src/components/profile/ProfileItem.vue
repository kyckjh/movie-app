<template>
<div class="app9" >
<div> Profile </div><hr>
  <div class="d-flex justify-content-center">
      <div class="d-flex flex-column mt-3">
        <div class="d-flex justify-content-between">
          <div class="d-flex flex-column">
            <div class="d-flex justify-content-between">
              <div style="font-size: 50px">
                <div v-if="currentUser.username == profile.username" style="margin:0;">
                  Welcome! {{ profile.username }}
                </div>
                <div>
                  <span v-if="currentUser.username == profile.username" 
                  style="margin:0; font-size:50px">                  .
                  </span>
                  <span v-else style="margin:0; font-size:50px">의</span>
                </div>
                <div class="d-flex align-items-center">
                  <div v-if="currentUser.username != profile.username" 
                  style="margin:0; font-size:50px; font-weight: 500">
                    프로필
                  </div>
                  <button v-if="currentUser.username != profile.username" id="follow" @click="followProfile(username)" class="heart-button" :class="{active : isFollowing}">
                  <div class="heart-flip"></div>
                  <span>follow<span>ed</span></span>
                  </button>
                </div>
              </div>
                <!-- 본인 프로필이면 팔로우 버튼 x
                팔로우 상태면 언팔로우버튼
                언팔로우 상태면 팔로우버튼 -->
            </div>
            <div>
              <span>{{ likeCount }} movie &nbsp;</span>
              <span>{{ followersCount }} followers &nbsp;</span>
              <span>{{ followingsCount }} followings</span>
            </div>
          </div>
        </div>
      </div>
    
  </div>
</div>

</template>

<script>
// import _ from "lodash"
import { mapActions, mapGetters } from "vuex"

export default {
    name: "ProfileItem",
    computed: {
        ...mapGetters(['profile', 'notMyAccount', 'isFollowing', 'currentUser']),
        likeCount() {
            return this.profile.like_movies?.length
        },
        followersCount() {
            return this.profile.followers?.length
        },
        followingsCount() {
            return this.profile.followings?.length
        },
    },

    data() {
        return {
            username: this.$route.params.username
        }
    },
    methods: {
        ...mapActions(['fetchProfile', 'followProfile'])
    },
    created() {
        const payload = { username: this.$route.params.username }
        this.fetchProfile(payload)
    },
    mounted() {
        document.querySelectorAll('.heart, .heart-button').forEach(button => button.addEventListener('click', () => button.classList.toggle('active')))
    }
}
</script>

<style>

</style>
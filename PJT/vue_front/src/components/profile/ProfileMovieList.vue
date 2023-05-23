<template>
  <div>
    <div > 계정 </div>
    <div class="d-flex justify-content-center">
        <div id="main_profile"  class="d-flex justify-content-between">
          <div class="d-flex flex-column">
            <router-link :profile_img="profile.profile_img" v-if="currentUser.username == profile.username" :to="{ name: 'profileImg', params : { username: profile.username } } ">
              <div class="changeText">프로필 사진 변경</div>
              <img v-if="profile.profile_img" :src="profile.profile_img">
              <img v-else class="profile" src="@/assets/default_profile.jpg">
            </router-link>
            <div v-else>
              <img v-if="profile.profile_img" :src="profile.profile_img">
              <img v-else class="profile" src="@/assets/default_profile.jpg">
            </div>
          </div>
          <div class="d-flex flex-column" style="margin-top: 80px">
            <div class="d-flex justify-content-between">
              <div style="font-size: 50px">
                <div v-if="currentUser.username == profile.username" style="margin:0;">어서와요!</div>
                <div>{{ profile.username }}<span v-if="currentUser.username == profile.username" style="margin:0; font-size:50px">.</span><span v-else style="margin:0; font-size:50px">의</span></div>
                <div class="d-flex align-items-center">
                  <div v-if="currentUser.username != profile.username" style="margin:0; font-size:50px; font-weight: 500">프로필</div>
                    <button v-if="currentUser.username != profile.username" id="follow" @click="followProfile(username)" class="heart-button" :class="{active : isFollowing}">
                      <div class="heart-flip"></div>
                      <span>follow<span>ed</span></span>
                    </button>
                </div>
              </div>

              <!-- 본인 프로필이면 팔로우 버튼 없음
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
</template>

<script>
import _ from "lodash"

import { mapGetters, mapActions } from 'vuex'
export default {
    name: 'profile_item',
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
    methods: {
        ...mapActions(['fetchProfile', 'followProfile']),
    },
    created() {
        const payload = { username: this.$route.params.username}
        this.fetchProfile(payload)
        this.random_num = _.random(0,5)
    },
    mounted() {
        document.querySelectorAll('.heart, .heart-button').forEach(button => button.addEventListener('click', () => button.classList.toggle('active')))
    }
}
</script>

<style>

</style>
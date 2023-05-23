<template>
    <div id="comment-list-item">
      <div class="d-flex justify-content-between">
        <div class="d-flex">
          <a :href="`http://localhost:8080/profile/${ comment.user.username }`">
            <img v-if="comment.user.profile_img" :src="comment.user.profile_img" alt="profile_img" class="profile_img">
            <img v-else class="profile_img" src="@/assets/default_profile.jpg">
          </a>
          <div id="comment_info">
            <div class="d-flex">
              <router-link :to="{ name: 'profile', params: { username: comment.user.username } }">
                <div>{{ comment.user.username }}</div>
              </router-link> 
  
              <div id="comment_edit" v-if="currentUser.username === comment.user.username && !isEditing">
                <button @click="switchIsEditing">수정</button>
                <button @click="deleteComment(payload)">삭제</button>
              </div>
            </div>
            <div class="divfont" v-if="!isEditing">{{ payload.content }} </div>
            <div id="editing" v-if="isEditing">
              <div class="d-flex">
                <input type="text" v-model="payload.content">
                <div>
                  <button @click="onUpdate">수정</button>
                  <button @click="switchIsEditing">취소</button>
                </div>
              </div>
            </div>
          </div>
  
  
        </div>
        <p>{{ comment.updated_at }}</p>
      </div>
      <hr>
    </div>
  </template>
  
  <script>
  import { mapGetters, mapActions } from 'vuex'
  
  export default {
    name: 'review_comment_item',
    props: { comment: Object },
    data() {
      return {
        isEditing: false,
        payload: {
          ReviewPk: this.comment.review,
          commentPk: this.comment.pk,
          content: this.comment.content
        },
      }
    },
    computed: {
      ...mapGetters(['currentUser']),
    },
    methods: {
      ...mapActions(['updateComment', 'deleteComment']),
      switchIsEditing() {
        this.isEditing = !this.isEditing
      },
      onUpdate() {
        this.updateComment(this.payload)
        this.isEditing = false
      }
    },
  }
  </script>
  
  <style>
 
  </style>
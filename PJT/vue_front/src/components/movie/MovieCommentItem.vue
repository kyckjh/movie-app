<template>
  <div>
  <hr>
    <h5 class="fs-6">작성자 : {{ comment.user.username }}</h5>
    <h5 class="">ㅡ {{payload.content}}</h5>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'

export default {
  name: 'MovieCommentItem',
  props:{
    comment: Object,
  },
  data: function(){
    return {
      isEditing: false,
      payload: {
        moviePk: this.comment.movie,
        commentPk: this.comment.id,
        content: this.comment.content
      },
      num: 0,
    }
  },
  computed: {
    ...mapGetters(['currentUser']),
    counting_star() {
      return `★`.repeat(this.comment.rate)
    },
    profile_img() {
      return this.comment.profile_img
    }
  },
  methods: {
    ...mapActions(['delete_movie_Comment', 'update_movie_Comment' ]),
    switchIsEditing() {
      this.isEditing = !this.isEditing
    },
    onUpdate() {
      this.update_movie_Comment(this.payload)
      this.isEditing = false
    },
    add(){
      this.num = this.num + 1
    }
  },
  watch: {
    "num" () {
      location.reload()
      
    },
  }
}
</script>

<style>

</style>
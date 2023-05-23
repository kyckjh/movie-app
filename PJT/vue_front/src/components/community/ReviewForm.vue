<template>
    <div class="container">
    <form @submit.prevent="onSubmit">
      <div class="input">
        <input class="title_input" v-model="newReview.title" type="text" id="title" placeholder="제목을 입력하세요."/>
      </div>
      <div id="content">
        <textarea class="content_input" v-model="newReview.content" type="text" placeholder="내용을 입력하세요."></textarea>
        <div class="text-end"><button class="yp-btn yp-btn-white">{{ action }}</button></div>
      </div>
    </form>
  </div>

</template>

<script>
import { mapActions } from 'vuex'

export default {
  name: 'ReviewForm',
  props: {
    review: Object,
    action: String,
  },
  data() {
    return {
      newReview: {
        title: this.review.title,
        content: this.review.content,
      }
    }
  },

  methods: {
    ...mapActions(['createReview', 'updateReview']),
    onSubmit() {
      if (this.action === '작성하기') {
        this.createReview(this.newReview)
      } else if (this.action === '수정하기') {
        const payload = {
          pk: this.review.pk,
          ...this.newReview,
        }
        this.updateReview(payload)
      }
    },
  },
}
</script>

<style>

</style>
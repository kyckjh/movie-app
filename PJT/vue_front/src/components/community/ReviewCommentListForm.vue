<template>
<div>
    
    <div id="form">
        <div class="in_form_margin">
            <div>
                {{ currentUser.username }}
            </div>
            <form @submit.prevent="onSubmit">
                <div class="d-flex">
                    <textarea name="" id="comment" v-model="content" placeholder="댓글을 달아주세요" required></textarea>
                    <!-- <input type="text" id="comment" v-model="content" placeholder="댓글을 달아주세요" required> -->
                    <button id="sub" style="margin-top: 70px">등록</button>
                </div>
            </form>
        </div>
    </div>
    
</div>

</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
    name: 'ReviewCommentListForm',
  data() {
    return {
      content: ''
    }
  },
  computed: {
    ...mapGetters(['Review', 'currentUser']),
  },
  methods: {
    ...mapActions(['createComment']),
    onSubmit() {
      this.createComment({ reviewPk: this.review.pk, content: this.content, })
      this.content = ''
    }
  }
}
</script>

<style>

</style>
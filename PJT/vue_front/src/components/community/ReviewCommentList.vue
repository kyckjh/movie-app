<template>
    <div class="article-comment-list">
    <review-comment-list-item 
      v-for="comment in comments" 
      :comment="comment" 
      :key="comment.pk">
    </review-comment-list-item>        
    <review-comment-list-form></review-comment-list-form>
  </div>

</template>

<script>
import ReviewCommentListItem from '@/components/community/ReviewCommentListItem.vue'
import ReviewCommentListForm from '@/components/community/ReviewCommentListForm.vue'

export default {
    name: 'ReviewCommentList',
  components: { ReviewCommentListForm, ReviewCommentListItem },
  props: { comments: Array },
}
</script>

<style>

</style>
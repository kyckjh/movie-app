<template>
  <div class="haha text-start">
    <hr>

    <h2>사용자 리뷰</h2><br>
    <div class="community d-flex justify-content-between">      
      <!-- <router-link :to="{ name: 'reviewNew' }">
        <button class="yp-btn yp-btn-white">게시글 작성</button>
      </router-link> -->
    </div>
    
    <div v-for="review in reviews" :key="Number(review.pk)" class="text-black" >
      <div class="card mb-3 card-bg">
        <div class="card-header fs-4">{{ review.title }}</div>
        <div class="card-body">
          <p class="card-text fs-5 m-3">{{ review.content.slice(0,300) }}...</p>
        </div>
        <div class="card-footer fs-6 text-end">
          <p> updated at {{ review.updated_at.slice(0, 10) }}</p>
          <a 
          :href="`http://localhost:8080/reviewdetail/${ review.pk }`"
          class="btn btn-outline-secondary text-black fw-bold"
          >자세히보기</a>
        </div>
      </div>
      
    </div>
    
  </div>

</template>

<script>
import { mapActions, mapGetters } from 'vuex'
// import Pagination from '@/components/community/Pagination.vue'
export default { 
  name: "review_list",
  components: {
    // Pagination
  },
  props: {
    movie_id: String,
  },
  methods: {
    ...mapActions(['fetchReviewList']),
  },
  computed: {
    ...mapGetters(['reviews'])
  },
  created() {
    this.fetchReviewList(this.movie_id)
    console.log(this.reviews)
  },
  
}
</script>

<style>
.card-bg {
  background-color:rgb(216, 216, 216);
}
</style>
<template>
    <div class="app">
        <h1>Community</h1>

      <div>
          <div class="d-flex justify-content-around">
          <review-detail></review-detail>
        </div>
          <review-list></review-list>
              
          
        
      </div>
      
    </div>
  </template>
  
  <script>
  import ReviewList from '../components/community/ReviewList.vue'
  import ReviewDetail from '../components/community/ReviewDetail.vue'
  
  export default {
    name: 'CommunityView',
    components: {
        ReviewList,
        ReviewDetail,
    }
  }
  </script>
  
  <style scoped>
  
    .app {
      margin-left: 15rem;
      margin-right: 15rem;
      margin-bottom: 100px;
    }
  
  </style>
<template>
    <div class="app">
        <h1>Community</h1>

      <div>
        <div class="d-flex justify-content-around">
        <community-list></community-list>
        
      </div>

          
        
      </div>
      
    </div>
  </template>
  
  <script>
import CommunityList from '../components/community/CommunityList.vue'
  
  export default {
    name: 'CommunityView',
    components: {
        CommunityList
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
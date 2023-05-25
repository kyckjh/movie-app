<template>
    <div class="haha">
      <div class="community d-flex justify-content-between">
        <router-link :to="{ name: 'CommunityCreateView' }">
          <button class="yp-btn yp-btn-white">게시글 작성</button>
        </router-link>
      </div>
      <div class="board">
        <table>
            <thead class="board__header">
              <tr>
                <th class="board__header__row" style="width: 4rem">번호</th>
                <th class="board__header__row">제목</th>
                <th class="board__header__row" style="width: 10rem">글쓴이</th>
                <th class="board__header__row" style="width: 8rem">작성일</th>
              </tr>
            </thead>
  
            <tbody
            v-for="review in reviews"
            :key="review.pk"
            class="board__body"
            >
              <tr>
                <td class="board__body__row">{{ review.pk }}</td>
                <router-link :to="{ name: 'review', params : { reviewPk: review.pk} }">
                  <td class="board__body__row hover">
                    {{ review.title }} 
                    <span style="color: #EE3B3B">[{{ review.comments.length }}]</span>
                    
                  </td>
                </router-link>
                <td class="board__body__row">
                  <router-link :to="{ name: 'profile', 
                  params: { username: review.user.username } }">
                    {{ review.user.username }}
                  </router-link> 
                </td>
                <td class="board__body__row">
                  {{ review.created_at }}
                </td>
              </tr>
            </tbody>
        </table>
      </div>
    </div>
  </template>
  
  <script>
  import { mapActions, mapGetters } from 'vuex'
  export default { 
    name: "CommunityList",
    components: {
      // Pagination
    },
    methods: {
      ...mapActions(['fetchReviews']),
    },
    computed: {
      ...mapGetters(['reviews'])
    },
    created() {
      this.fetchReviews()
    },
    
  }
  </script>
  
  <style>

  </style>
<template>
  <div>
    <h1>MovieCommentList</h1>
    
    <div>
      <movie-comment-item v-for="comment in get_comments" :key="comment.id" :comment="comment"></movie-comment-item>
    </div>
    <div v-if="isLoggedIn" id="comment_writer">
        <form @submit.prevent="create_movie_Comment(commentform); add();">
          <div class="d-flex row" style="margin: 10px 10px 10px 10px;">
            <div>
              <div class="d-flex justify-content-between">
                <div>
                  <label for="comment_w" id="user">{{ currentUser.username }}</label>
                </div>             
              </div>
              <textarea name="" id="comment_w" cols="30" rows="10" autocomplete="off" autocorrect="off" maxlength="200" v-model="commentform.content"></textarea>
            </div>
            <div class=" d-flex justify-content-end">
              <button>등록</button>
            </div>
          </div>
        </form>
      </div>
  </div>
</template>

<script>
import MovieCommentItem from '@/components/movie/MovieCommentItem.vue'
import axios from 'axios'
import { mapGetters, mapActions } from 'vuex'


export default {  
  name: 'MovieCommentList',
  components: {
    MovieCommentItem,
  },
  props: {
    movie_id: String,
  },
  data: function() {
    return {
      commentform: {
        movie_id: this.$route.params.movie_id,
        content: "",
      },
      //get_comments: {},
      num: 0,
    }
  },
  methods: {
    ...mapActions(['create_movie_Comment', 'fetchCurrentUser']),
    add(){
      this.num++
    },
  },
  computed: {
    ...mapGetters(['isLoggedIn', "get_comments", 'get_movie', 'currentUser', ]),
  },
  created() {
    axios.get("http://localhost:8000/api/v1/" + this.$route.params.movie_id + "/comments/", {})
      .then(res => {
        console.log(res.data)
        //this.get_comments = res.data
        this.$store.state.get_comments = res.data
      }),
    this.fetchCurrentUser()
  },
  watch: {
    "num"() {
      location.reload()
    }
  }

}
</script>

<style>

</style>
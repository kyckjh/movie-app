<template>
  <div>
    <h1>MovieCommentList</h1>
    
    <div>
      <movie-comment-item v-for="comment in get_comments" :key="comment.id" :comment="comment"></movie-comment-item>
      
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
        rate: 0,
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
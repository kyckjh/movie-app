<template>
  <div>
    <h1>Sign Up Page</h1>
    <form>
      <label for="username">username : </label>
      <input type="text" id="username"><br>

      <label for="email">email : </label>
      <input type="text" id="email"><br>

      <label for="password1"> password : </label>
      <input type="password" id="password1"><br>

      <label for="password2"> password confirmation : </label>
      <input type="password" id="password2">
      
      <input type="submit" value="SignUp">
    </form>
  </div>
</template>

<script>
import {mapActions, mapGetters } from 'vuex'


export default {
  name: 'SignUpView',
  components: {

  },
  data() {
    return {
      credentials: {
        username: '',
        email: '',
        password1: '',
        password2: '',
      }
    }
  },
  computed: {
    ...mapGetters(['authError'])
  },
  methods: {
    ...mapActions(['signup'])
  }

}
</script>

<style>

</style>
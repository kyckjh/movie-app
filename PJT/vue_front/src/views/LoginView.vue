<template>
  <div class="login_logo display-4">
        Log In
      </div>
</template>

<script>
import {mapActions, mapGetters } from 'vuex'
import AccountErrorList from '@/components/account/AccountErrorList.vue'
export default {
  name: 'LoginView',
  components: {AccountErrorList,
  },
  data() {
    return {
      credentials: {
        username: '',
        password: '',
      },
      state: false,
    }
  },
  computed: {
    ...mapGetters(['authError'])
  },
  methods: {
    ...mapActions(['login']),

    trim: function(str) {
      str = str.replace(/^\s/, "");
      for (var i = str.length - 1; i >= 0; i --) {
        if (/\s/.test(str.charAt(i))) {
          str = str.substring(0, i + 1);
          break;
        }
      }
      return str;
    },
    next() {
      let username = document.getElementById("username").value
      if (username) {
        document.getElementById("backbtn").classList.add("active");
        document.getElementById("phase-form").classList.add("next");
        setTimeout(function() {document.getElementById("password").focus()}, 250)

        try {
          document.getElementById("username").classList.remove("error");
        } catch {
          console.log("remove")
        }
        this.state = ture;
      } 
    },
  },
  created() {},
}
</script>

<style>

</style>
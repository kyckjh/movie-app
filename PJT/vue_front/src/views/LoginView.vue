<template>
  <div id="main" class="d-flex">
      <div class="login_logo display-4">
        Log in
      </div>
    <div class="container d-flex align-items-center justify-content-center">
      <div class="d-flex justify-content-center align-items-center mb-5">
          <div>
            <account-error-list v-if="authError"></account-error-list>
            <div>
              <form @submit.prevent="login(credentials)" id="userInfo" name="userInfo">
                <div class="login-form">
                  <div class="backbtn" id="backbtn" @click="back">
                    <i class="fa-solid fa-reply"></i>
                  </div>
                  <div class="phases" id="phase-form">
                    <div class="phase-1">
                      <input id="username" v-model="credentials.username" autocomplete="off" type="text" placeholder="User ID">

                    </div>
                    <div class="phase-2">
                      <input type="password" v-model="credentials.password" id="password" @keydown.esc="back" @keydown.enter="submitForm" placeholder="Enter password">
                      <button @click="submitForm"><i class="fa-solid fa-circle-arrow-right">로그인</i></button>      
                    </div>
                  </div>
                  <div class="loading"></div>
                </div>
              </form>
            </div>

            <div>
              <div class="separator" style="width:100%; max-width: 328px; margin:auto; height: 1px; background-image: url(https://appleid.cdn-apple.com/appleauth/static/bin/cb1633718600/dist/assets/HR_gradient_dark.png); background-size: cover;"></div>
              <div class="text-center sign_up">
                회원가입 하시겠습니까?
                <router-link to="/signup" class="nav-link" active-class="active">Sign Up</router-link>
              </div>
            </div>
          </div>
      </div>
    </div>
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
        this.state = true;
      } 
    },
    submitForm() {
      var password = this.trim(document.getElementById("password").value);
      if (password) {
        //Submit form ...
        document.getElementsByClassName("loading")[0].classList.add("show-it");
        //setTimeout(() => { this.login(this.credentials) }, 1300)
        // setTimeout(this.login(this.credentials), 3000)
        // this.login(this.credentials)
      } else {
        document.getElementById("password").classList.add("error");
      }
    },
    back() {
      if (this.state) {
        document.getElementById("backbtn").classList.remove("active");
        document.getElementById("phase-form").classList.remove("next");
        this.credentials.username = ""
        this.credentials.password = ""
        setTimeout(function() {document.getElementById("username").focus()}, 250)
        this.state = false;
      }
    },
  }, 
  created() {},
}
</script>

<style>

</style>
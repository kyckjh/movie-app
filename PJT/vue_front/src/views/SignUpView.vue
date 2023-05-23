<template>
  <div id="main" class="d-flex">
    <div class="login_logo display-4">
      회원가입
    </div>
    <div class="container d-flex align-items-center justify-content-center">
      <div class="d-flex justify-content-center align-items-center mb-5">
        <div>
          <account-error-list v-if="authError"></account-error-list>
          <div>
            <form @submit.prevent="signup(credentials)">
              <div class="login-form">
                <div class="phases" id="phase-form">
                  <div class="phase-1">
                    <input id="username" v-model="credentials.username" autocomplete="off" type="text" placeholder="아이디를 입력하세요." required>
                    <input id="email" v-model="credentials.email" autocomplete="off" type="text" placeholder="이메일을 입력하세요." required>
                    <input type="password" v-model="credentials.password1" id="password1" autocomplete="off"  placeholder="비밀번호를 입력하세요." required>
                    <input type="password" v-model="credentials.password2" id="password2" autocomplete="off"  @keydown.enter="submitForm" placeholder="비밀번호 확인" required>
                  </div>
                  <div>
                    <div class="separator mt-4" style="width:100%; max-width: 328px; margin:auto; height: 1px; background-image: url(https://appleid.cdn-apple.com/appleauth/static/bin/cb1633718600/dist/assets/HR_gradient_dark.png); background-size: cover;"></div>
                    <div class="text-center sign_up">
                      <div class="mt-4 mb-4">회원가입 결정</div>
                      <button class="btn btn-primary ms-4 me-4">회원가입</button>
                    </div>
                  </div>                  
                </div>
              </div>
            </form>
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
  name: 'SignUpView',
  components: {
    AccountErrorList,

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
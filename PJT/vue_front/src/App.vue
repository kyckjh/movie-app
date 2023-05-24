<template>
  <div id="MovInside">
    <nav>
      <ul class="nav align-items-center justify-content-between">
        <div class="d-flex align-items-center justify-content-between">
          <div class="">
            <router-link to="/" class="nav-link text-secondary">
              <!-- <img src="./assets/Eivom_uppercase.png" alt="" class="nav-link"> -->
          </router-link>
          </div>

          <li class="nav-item short_menu">
            <router-link to="/" class="nav-link text-secondary"
            active-class="active">MovInside</router-link>
          </li>

          
        </div>

        <div class="d-flex me-3">
          <router-link to="/" class="nav-link fw-bold text-secondary"
            active-class="active">Search icon</router-link>
          
          <div>
                <div class="search-form">
                  <div class="search-box">
                    <input type="text" @keydown.enter="search_movie_ID(search_movie)" v-model="search_movie"/>
                    <span></span>
                  </div>
                </div>
              </div> 

          <router-link v-show="!isLoggedIn" :to="{ name: 'LoginView' }"> Log In |</router-link> 
          <router-link v-show="!isLoggedIn" :to="{ name: 'SignUpView' }"> Sign Up |</router-link>
          <router-link v-show="isLoggedIn" :to="{ name: 'LogoutView' }"> Log Out </router-link> 

        </div>
      </ul>
      
    </nav>
    <router-view/>

    <footer class="fs-3 text-center">
      <div class="foot d-flex justify-content-center align-items-center" style="height: 100px">
        <div class="">
          <div><a href="https://github.com/DasisCore/last-project"><i class="fa-brands fa-github"></i></a></div>
          <div style="font-size: 10px;">MADE BY</div>
          <div class="d-flex">
            <div style="font-size: 15px; margin-right: 10px;">Kang Yeah-Chan</div>
            <div style="font-size: 15px; margin-left: 10px;">Rinoue Isoroku</div>
          </div>
        </div>
      </div>
    </footer>

  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';



export default {
  name: 'App',
  components: {

  },
  data: function() {
    return {
      search_movie: "",
    }
  },
  computed: {
    ...mapGetters(['isLoggedIn', 'currentUser',])
  },
  methods: {
    ...mapActions(['fetchCurrentUser', 'search_movie_ID'])
  },
  created() {
    this.fetchCurrentUser()
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>

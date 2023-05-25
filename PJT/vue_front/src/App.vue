<template>
  <div id="MovInside" class="stacked-linear">
    <nav class="border-bottom border-1">
      <ul class="nav align-items-center justify-content-between">
        <div class="d-flex align-items-center justify-content-between">
          
          <li class="nav-item short_menu">
            <router-link to="/" class="nav-link text-white fs-2"
            active-class="active">MovInside</router-link>
          </li>

          
        </div>

        <div class="d-flex me-3">
          <router-link to="/community" class="nav-link fw-bold text-white" active-class="active">Community</router-link>

          <router-link to="/" class="nav-link fw-bold text-white"
            active-class="active">Search</router-link>
          
          <div>
            <div class="search-form">
              <div class="search-box">
                <input type="text" @keydown.enter="search_movie_ID(search_movie)" v-model="search_movie"/>
                &nbsp;
              </div>
            </div>
          </div> 

          <router-link v-show="!isLoggedIn" 
          :to="{ name: 'LoginView' }"
          class="nav-link fw-bold text-white"
          > Login</router-link>  
          <router-link v-show="!isLoggedIn" 
          :to="{ name: 'SignUpView' }"
          class="nav-link fw-bold text-white"
          > Sign Up</router-link> 
          <router-link v-show="isLoggedIn" 
          :to="{ name: 'LogoutView' }"
          class="nav-link fw-bold text-white"
          > Logout</router-link>  
          <router-link v-if="currentUser.username != undefined && isLoggedIn" 
          :to="{ name: 'ProfilePageView',  params:{ username: currentUser.username }}"
          class="nav-link fw-bold text-white"
          >{{currentUser.username}} </router-link> 

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
    //setTimeout(() => { this.fetchCurrentUser() }, 3000)
    //alert('username'+ this.currentUser.username)
  }
}
</script>

<style>

#MovInside {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: white;  
}

.gradient {
  background: linear-gradient(to left, black, rgb(51, 51, 51) 15%, black);
}

.conic-gradient {
  background: conic-gradient(at 0% 30%, black 10%, rgb(51, 51, 51) 30%, rgb(100, 100, 100) 50%);
}

.stacked-linear {
  background: linear-gradient(
      217deg,
      rgba(0, 0, 0, 1),
      rgba(0, 0, 0, 0.5) 70.71%
    ), linear-gradient(127deg, rgba(0, 0, 0, 1), rgba(0, 0, 0, 0) 70.71%),
    linear-gradient(336deg, rgba(0, 0, 0, 1), rgba(0, 0, 0, 0) 70.71%);
}

nav {
  padding: 10px;
}

nav a {
  font-weight: bold;
  color: whitesmoke;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>

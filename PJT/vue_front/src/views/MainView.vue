<template>
        <div class="login_logo display-4">
            
        <div>
            <main-card-list :num="1">main card list</main-card-list>
            <main-card-list :num="2">main card list</main-card-list>
        </div>
    </div>
</template>
  
  <script>
    import MainCardList from '../components/movInside/MainCardList.vue'
    import movie from '../assets/main_movies/movies.json'

    // let num = _.random(1, 9)

  export default {
    name: 'MainView',
    components: {
        MainCardList,
    },
    data: function() {
        return{
            movie_data: movie,
            title: "",
            release_data: "",
            overview: "",
            review: "",
            reviewer: "",
        }
    },
    computed: {},
    methods: {},
    created() {
        // this.title = movie.movies[num].title
    },
}
window.addEventListener('click', function(){
    clickCerosel()
});
function clickCerosel(){
    const ele = document.querySelectorAll('.title');
    let eleOffsetArr = [];

    ele.forEach(e => {
        let eleOffset = e.getBoundingClientRect().top + window.pageYOffset - 800;
        eleOffsetArr.push(eleOffset)
    })

    eleOffsetArr.forEach((offset, idx) => {
        ele[idx].getElementsByClassName.cssText = ( window.scrollY > offset
        ? 'opacity:1; transform: translateY(0);'
        : 'opacity:0; transform: translateY(50px);')
    })
}
  </script>
  
  <style>

  </style>
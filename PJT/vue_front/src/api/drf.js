const HOST = 'http://localhost:8000/'

const ACCOUNTS = 'accounts/'
const REVIEWS = 'review/'
const MOVIES = 'movies/'
const COMMENTS = 'comments/'
export default {
  accounts: {
    login: () => HOST + ACCOUNTS + 'login/',
    logout: () => HOST + ACCOUNTS + 'logout/',
    signup: () => HOST + ACCOUNTS + 'signup/',
    // Token 으로 현재 user 판단
    currentUserInfo: () => HOST + ACCOUNTS + 'user/',
    // username으로 프로필 제공
    profile: username => HOST + ACCOUNTS + 'profile/' + username,
    follow: username => HOST + ACCOUNTS + 'follow/' + `${username}/`,
    // img: username => HOST + ACCOUNTS + 'upload_img/' + `${username}/`,
  },
  reviews: {
    // /articles/
    reviews: () => HOST + REVIEWS,
    // /articles/1/
    review: reviewPk => HOST + REVIEWS + `${reviewPk}/`,
    likeArticle: reviewPk => HOST + REVIEWS + `${reviewPk}/` + 'like/',
    comments: reviewPk => HOST + REVIEWS + `${reviewPk}/` + COMMENTS,
    comment: (reviewPk, commentPk) =>
      HOST + REVIEWS + `${reviewPk}/` + COMMENTS + `${commentPk}/`,
    likeComment: (reviewPk, commentPk) =>
      HOST + REVIEWS + `${reviewPk}/` + COMMENTS + `${commentPk}/` + 'like/'
  },
  movies: {
    movie: movie_id => HOST + MOVIES + `${ movie_id }/`,
    movie_comment: movie_id => HOST + MOVIES + `${ movie_id }/` + COMMENTS,
    movie_comment_delete: (moviePk, commentPk) => HOST + MOVIES + `${moviePk}/` + COMMENTS + `${commentPk}/`,
    likeMovie: moviePk => HOST + MOVIES + `${ moviePk }/` + 'like/'
    // movies: () => HOST + MOVIES,
  }
}

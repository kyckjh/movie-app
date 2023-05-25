import router from '@/router'
import axios from 'axios'
import drf from '@/api/drf'

import _ from 'lodash'
// import accounts from './accounts'

export default {
  // namespaced: true,
  state: {
    reviews: [],
    review: {},
    currentUser: {},
  },

  getters: {
    currentUser: (state) => state.currentUser,
    reviews: (state) => state.reviews,
    review: (state) => state.review,
    isAuthor: (state, getters) => {
      return state.review.user?.username === getters.currentUser.username;
    },
    isReview: (state) => !_.isEmpty(state.review),
    reviewLiking: (state) =>
      _.some(state.review.review_like, { pk: state.currentUser.pk }),
  },

  mutations: {
    SET_CURRENT_USER: (state, user) => (state.currentUser = user),
    SET_REVIEWS: (state, reviews) => (state.reviews = reviews),
    SET_REVIEW: (state, review) => (state.review = review),
    SET_REVIEW_COMMENTS: (state, comments) =>
      (state.review.comments = comments),
  },

  actions: {
    fetchReviewList({ commit, getters }, movie_id) {
      /* 게시글 목록 받아오기
      GET: reviews URL (token)
        성공하면
          응답으로 받은 게시글들을 state.reviews에 저장
        실패하면
          에러 메시지 표시
      */
      axios({
        url: drf.reviews.reviewList(movie_id),
        method: 'get',
        headers: getters.authHeader,
      })
      .then((res) => {
        for (const [key, value] of Object.entries(res.data)) {
          //console.log(key);
          console.log(value)
          axios({
            url: drf.accounts.user(res.data[key]['user']),
            method: 'get',
            headers: getters.authHeader,
          })
          .then((result) => {
            console.log(result.data['username'])
            res.data[key]['user'] = result.data['username'];
          })
          .catch((err) => console.error(err.response));
        }
        commit('SET_REVIEWS', res.data)
      })
      .catch((err) => console.error(err.response));
    },
    fetchReviews({ commit, getters }) {
      /* 게시글 목록 받아오기
      GET: reviews URL (token)
        성공하면
          응답으로 받은 게시글들을 state.reviews에 저장
        실패하면
          에러 메시지 표시
      */
      axios({
        url: drf.reviews.reviews(),
        method: 'get',
        headers: getters.authHeader,
      })
        .then((res) => { 
          console.log(res.data)
          commit('SET_REVIEWS', res.data)
        })
        .catch((err) => console.error(err.response));
    },

    fetchReview({ commit, getters }, reviewPk) {
      /* 단일 게시글 받아오기
      GET: article URL (token)
        성공하면
          응답으로 받은 게시글들을 state.reviews에 저장
        실패하면
          단순 에러일 때는
            에러 메시지 표시
          404 에러일 때는
            NotFound404 로 이동
      */
      axios({
        url: drf.reviews.article(reviewPk),
        method: 'get',
        headers: getters.authHeader,
      })
        .then((res) => commit('SET_REVIEW', res.data))
        .catch((err) => {
          console.error(err.response);
          if (err.response.status === 404) {
            router.push({ name: 'NotFound404' });
          }
        });
    },

    createReview({ commit, getters }, review) {
      /* 게시글 생성
      POST: reviews URL (게시글 입력정보, token)
        성공하면
          응답으로 받은 게시글을 state.article에 저장
          ArticleDetailView 로 이동
        실패하면
          에러 메시지 표시
      */

      axios({
        url: drf.reviews.reviews(),
        method: 'post',
        data: review,
        headers: getters.authHeader,
      }).then((res) => {
        commit('SET_REVIEW', res.data);
        router.push({
          name: 'review',
          params: { reviewPk: getters.review.pk },
        });
      });
    },

    updateReview({ commit, getters }, { pk, title, content }) {
      /* 게시글 수정
      PUT: article URL (게시글 입력정보, token)
        성공하면
          응답으로 받은 게시글을 state.article에 저장
          ArticleDetailView 로 이동
        실패하면
          에러 메시지 표시
      */
      axios({
        url: drf.reviews.review(pk),
        method: 'put',
        data: { title, content },
        headers: getters.authHeader,
      }).then((res) => {
        commit('SET_REVIEW', res.data);
        router.push({
          name: 'review',
          params: { reviewPk: getters.review.pk },
        });
      });
    },

    deleteReview({ commit, getters }, reviewPk) {
      /* 게시글 삭제
      사용자가 확인을 받고
        DELETE: article URL (token)
          성공하면
            state.article 비우기
            AritcleListView로 이동
          실패하면
            에러 메시지 표시
      */

      if (confirm('정말 삭제하시겠습니까?')) {
        axios({
          url: drf.reviews.review(reviewPk),
          method: 'delete',
          headers: getters.authHeader,
        })
          .then(() => {
            commit('SET_REVIEW', {});
            router.push({ name: 'community' });
          })
          .catch((err) => console.error(err.response));
      }
    },

    likeReview({ commit, getters }, reviewPk) {
      /* 좋아요
      POST: likeArticle URL(token)
        성공하면
          state.article 갱신
        실패하면
          에러 메시지 표시
      */
      axios({
        url: drf.reviews.likeReview(reviewPk),
        method: 'post',
        headers: getters.authHeader,
      })
        .then((res) => commit('SET_REVIEW', res.data))
        .catch((err) => console.error(err.response));
    },

    createComment({ commit, getters }, { reviewPk, content }) {
      /* 댓글 생성
      POST: comments URL(댓글 입력 정보, token)
        성공하면
          응답으로 state.article의 comments 갱신
        실패하면
          에러 메시지 표시
      */
      const comment = { content };

      axios({
        url: drf.reviews.comments(reviewPk),
        method: 'post',
        data: comment,
        headers: getters.authHeader,
      })
        .then((res) => {
          commit('SET_REVIEW_COMMENTS', res.data);
        })
        .catch((err) => console.error(err.response));
    },

    updateComment({ commit, getters }, { reviewPk, commentPk, content }) {
      /* 댓글 수정
      PUT: comment URL(댓글 입력 정보, token)
        성공하면
          응답으로 state.article의 comments 갱신
        실패하면
          에러 메시지 표시
      */
      const comment = { content };

      axios({
        url: drf.reviews.comment(reviewPk, commentPk),
        method: 'put',
        data: comment,
        headers: getters.authHeader,
      })
        .then((res) => {
          commit('SET_REVIEW_COMMENTS', res.data);
        })
        .catch((err) => console.error(err.response));
    },

    deleteComment({ commit, getters }, { reviewPk, commentPk }) {
      /* 댓글 삭제
      사용자가 확인을 받고
        DELETE: comment URL (token)
          성공하면
            응답으로 state.article의 comments 갱신
          실패하면
            에러 메시지 표시
      */
      if (confirm('정말 삭제하시겠습니까?')) {
        axios({
          url: drf.reviews.comment(reviewPk, commentPk),
          method: 'delete',
          data: {},
          headers: getters.authHeader,
        })
          .then((res) => {
            commit('SET_REVIEW_COMMENTS', res.data);
          })
          .catch((err) => console.error(err.response));
      }
    },
  },
};

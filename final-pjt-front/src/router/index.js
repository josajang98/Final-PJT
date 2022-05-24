import Vue from 'vue'
import VueRouter from 'vue-router'
import MainUnlogin from '../views/MainUnlogin.vue'
import LoginView from '../views/LoginView.vue'
import LogoutView from '../views/LogoutView.vue'
import SignupView from '../views/SignupView.vue'
import ProfileView from '../views/ProfileView.vue'

import ArticlesView from '../views/ArticlesView.vue'
import GenreWc from '../views/GenreWc.vue'
import WishList from '../views/WishList.vue'
import ArticleDetail from '../views/ArticleDetail.vue'
import PersonDetail from '../views/PersonDetail.vue'
import SearchResult from '../views/SearchResult.vue'
Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: MainUnlogin
  },
  {
    path: '/accounts/login',
    name: 'login',
    component: LoginView
  },
  {
    path: '/logout',
    name: 'logout',
    component: LogoutView
  },
  {
    path: '/accounts/signup',
    name: 'signup',
    component: SignupView
  },
  {
    path: '/articles',
    name: 'articles',
    component: ArticlesView
  },
  {
    path: '/articles/genrewc',
    name: 'genrewc',
    component: GenreWc
  },
  {
    path: '/articles/:movie_id',
    name: 'detail',
    component: ArticleDetail
  },
  {
    path: '/accounts/wishList',
    name: 'wishList',
    component: WishList
  },
  {
    path: '/accounts/:username/profile',
    name: 'profile',
    component: ProfileView
  },
  {
    path: '/articles/search/:query/',
    name: 'search',
    component: SearchResult
  },
  {
    path: '/articles/person/:person_id',
    name: 'personDetail',
    component: PersonDetail
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router

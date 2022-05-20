import Vue from 'vue'
import VueRouter from 'vue-router'
import MainUnlogin from '../views/MainUnlogin.vue'
import LoginView from '../views/LoginView.vue'
import SignupView from '../views/SignupView.vue'

import ArticlesView from '../views/ArticlesView.vue'
import GenreWc from '../views/GenreWc.vue'
import PickMovie from '../views/PickMovie.vue'

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
    path: '/articles/pickmovie',
    name: 'pickmovie',
    component: PickMovie
  },

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router

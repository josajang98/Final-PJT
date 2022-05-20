import Vue from 'vue'
import VueRouter from 'vue-router'
import MainUnlogin from '../views/MainUnlogin.vue'
import LoginView from '../views/LoginView.vue'
import SignupView from '../views/SignupView.vue'

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

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router

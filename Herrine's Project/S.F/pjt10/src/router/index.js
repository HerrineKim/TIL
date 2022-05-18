import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import RandomView from '../views/RandomView.vue'
import WatchList from '../views/WatchList.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/random-view',
    name: 'randomview',
    component: RandomView
  },
  {
    path: '/watch-list',
    name: 'watchlist',
    component: WatchList
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router

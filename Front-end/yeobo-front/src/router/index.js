import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import InfoView from '../views/InfoView.vue'
import LoginView from '../views/LoginView.vue'
import LogoutView from '../views/LogoutView.vue'
import MyMapView from '../views/MyMapView.vue'
import NewView from '../views/NewView.vue'
import VideoDetailView from '../views/VideoDetailView.vue'


Vue.use(VueRouter)

const routes = [
  // 홈 화면 및 마이맵
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/mymap',
    name: 'myMap',
    component: MyMapView
  },
  // 개별 유튜브 비디오 선택
  {
    path: '/video/:videoPk',
    name: 'videoDetail',
    component: VideoDetailView
  },
  // 로그인, 로그아웃
  {
    path: '/login',
    name: 'login',
    component: LoginView
  },
  {
    path: '/logout',
    name: 'logout',
    component: LogoutView
  },
  // info
  {
    path: '/info',
    name: 'info',
    component: InfoView
  },
  {
    path: '/new',
    name: 'new',
    component: NewView
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
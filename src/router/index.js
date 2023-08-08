import { createRouter, createWebHistory } from 'vue-router'
import get_user_token from '../components/get_user_token.vue'
import get_user from '../components/get_user.vue'
import scoreboard_user from '../components/scoreboard_user.vue'
import challenge_list from '../components/challenge_list.vue'
import NotFound from '../components/NotFound.vue'
import scoreboard_team from '../components/scoreboard_team.vue'

const routes = [
  {
    path: '/SignIn',
    name: 'SignIn',
    component: get_user_token
  },
  {
    path: '/StartPage',
    name: 'Start Page',
    component: get_user
  },
  {
    path: '/:catchAll(.*)',
    name: 'NotFound',
    component: NotFound
  },
  {
    path: '/ChallengeList',
    name: 'ChallengeList',
    component: challenge_list
  },
  {
    path: '/scoreboard_user',
    name: 'scoreboard_user',
    component: scoreboard_user
  },
  {
    path: '/scoreboard_team',
    name: 'scoreboard_team',
    component: scoreboard_team
  },
]
const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})
export default router

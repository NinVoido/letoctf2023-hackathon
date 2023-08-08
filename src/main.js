import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

// const routes = [
//     {
//       path: '/SignIn',
//       name: 'SignIn',
//       component: get_user_tokenn
//     },
//     {
//       path: '/StartPage',
//       name: 'Start Page',
//       // route level code-splitting
//       // this generates a separate chunk (about.[hash].js) for this route
//       // which is lazy-loaded when the route is visited.
//       component: () => import(/* webpackChunkName: "about" */ '../views/get.vue')
//     }
// ]
const app = createApp(App)
app.config.globalProperties.$api = 'http://192.168.14.39:8000/api/v1'
app.config.globalProperties.$date = '2023-06-30'

app.use(router).mount('#app')

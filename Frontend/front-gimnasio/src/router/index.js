import { createRouter, createWebHistory } from 'vue-router'
import LoginView from '@/components/login.vue'
import registerUserView from '@/components/registerUser.vue'
import dashboardView from '@/components/dashboard.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'login',
      component: LoginView
    },
    {
      path: '/register',
      name: 'register',
      component: registerUserView
    },
    {
      path: '/dashboard',
      name: 'dashboard',
      component: dashboardView
    },

  ]
})

export default router

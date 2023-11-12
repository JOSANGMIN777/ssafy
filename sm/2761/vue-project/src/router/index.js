import {createRouter, createWebHistory} from 'vue-router'

import SomeView from '@/views/SomeView.vue'
import OtherView from '@/views/OtherView.vue'
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
        path: '/',
        name: 'other',
        component: OtherView
    },
    {
        path: '/',
        name: 'some',
        component: SomeView
    }

      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
    //   component: () => import('../views/AboutView.vue')
    
  ]
})

export default router

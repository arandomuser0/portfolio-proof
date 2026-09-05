import { createRouter, createWebHistory } from 'vue-router'
import Dashboard from '../views/Dashboard.vue'
import Applications from '../views/Applications.vue'
import ApplicationDetail from '../views/ApplicationDetail.vue'
export default createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', component: Dashboard },
    { path: '/applications', component: Applications },
    { path: '/applications/:id', component: ApplicationDetail, props: true }
  ]
})

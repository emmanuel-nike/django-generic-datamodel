import Vue from 'vue';
import Router from 'vue-router';
import store from './store.js';
import DashboardLayout from '@/layout/DashboardLayout';
import AuthLayout from '@/layout/AuthLayout';
import Dashboard from './views/Dashboard.vue';
import Login from './views/Login.vue';
import Register from './views/Register.vue';
import Profile from './views/UserProfile.vue';

Vue.use(Router);

let router = new Router({
  linkExactActiveClass: 'active',
  mode: 'history',
  base: '/',
  routes: [{
      path: '/',
      redirect: 'dashboard',
      component: DashboardLayout,
      children: [{
          path: '/dashboard',
          name: 'dashboard',
          component: Dashboard,
          meta: {
            requiresAuth: true
          }
        },
        {
          path: '/profile',
          name: 'profile',
          component: Profile,
          meta: {
            requiresAuth: true
          }
        }
      ]
    },
    {
      path: '/',
      redirect: 'login',
      component: AuthLayout,
      children: [{
          path: '/login',
          name: 'login',
          component: Login
        },
        {
          path: '/register',
          name: 'register',
          component: Register
        }
      ]
    }
  ]
});

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (store.getters.isLoggedIn) {
      next();
      return;
    }
    next('/login');
  } else {
    next();
  }
})

export default router;
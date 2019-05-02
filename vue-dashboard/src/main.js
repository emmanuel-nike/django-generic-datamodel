import Vue from 'vue';
import App from './App.vue';
import router from './router';
import Dashboard from './plugins/dashboard';
import Axios from 'axios';
import store from './store';

Vue.prototype.$http = Axios;
Vue.config.productionTip = false;

const token = localStorage.getItem('token');
if (token) {
  Vue.prototype.$http.defaults.headers.common.Authorization = 'Token ' + token;
}

Vue.use(Dashboard);
new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app');
import Vue from 'vue'
import App from './App.vue'
import BootstrapVue  from 'bootstrap-vue'
import router from './routes.js'
import 'bootstrap/dist/css/bootstrap.min.css'

//!Utilize BootstrapVue
Vue.use(BootstrapVue)

new Vue({
  el: '#app',
  router,
  render: h => h(App)
})

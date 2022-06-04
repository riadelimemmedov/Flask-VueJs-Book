import Vue from 'vue'
import App from './App.vue'
import BootstrapVue  from 'bootstrap-vue'
import router from './routes.js'
import 'bootstrap/dist/css/bootstrap.min.css'
import DisableAutocomplete from 'vue-disable-autocomplete';

//!Utilize BootstrapVue
Vue.use(BootstrapVue)

//!Utilize DisableAutocomplete
Vue.use(DisableAutocomplete)

new Vue({
  el: '#app',
  router,
  render: h => h(App)
})

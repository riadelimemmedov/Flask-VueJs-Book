import Vue from 'vue'
import Router from 'vue-router'
import Ping from './components/Ping.vue'
import Books from './components/Books.vue'


//!utilize vue-router
Vue.use(Router)

//!export default new Router => direct export Router
export default new Router({
  mode:'history',
  base:process.env.BASE_URL,
  routes:[
    {path:'/',name:'books_list_router',component:Books},
    {path:'/ping',name:'ping_router',component:Ping}
  ]
})

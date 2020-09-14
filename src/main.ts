import 'core-js/stable' // Javascript 标准库
import 'regenerator-runtime/runtime' // 将yield语法转换成 ES5的语法
import Vue from 'vue'
import '@/plugins/bootstrap-vue'
import App from '@/App.vue'
import router from '@/router'
import store from '@/store/index'
import i18n from '@/i18n'
import BootstrapVue from 'bootstrap-vue'
import { library } from '@fortawesome/fontawesome-svg-core'
import {
  faBan,
  faStar,
  faSearch,
  faInfoCircle,
  faArrowLeft,
  faAngleDown,
  faAngleRight,
} from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

library.add(faBan)
library.add(faStar)
library.add(faSearch)
library.add(faArrowLeft)
library.add(faAngleDown)
library.add(faInfoCircle)
library.add(faAngleRight)
Vue.component('font-awesome-icon', FontAwesomeIcon)

Vue.config.productionTip = false
Vue.use(BootstrapVue)

new Vue({
  router,
  store,
  i18n,
  render: (h) => h(App),
}).$mount('#app')

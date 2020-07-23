// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'

import axios from "axios"
Vue.prototype.$axios = axios

import Element from "element-ui"
import "element-ui/lib/theme-chalk/index.css"
Vue.use(Element)

// 导入极验
import "../static/js/gt.js"

//全局CSS
import "../static/css/global.css"

//视频播放器配置
require('video.js/dist/video-js.css');
require('vue-video-player/src/custom-theme.css');
import VideoPlayer from 'vue-video-player'

Vue.use(VideoPlayer);

Vue.config.productionTip = false



import settings from "./settings";
Vue.prototype.$settings = settings;


//Vuex配置
import store from './store/index'

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
    store,
  components: {App},
  template: '<App/>'
})

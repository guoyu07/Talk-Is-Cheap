// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue';
import VueRouter from 'vue-router';
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-default/index.css';
import App from './App';

Vue.use(VueRouter);
Vue.use(ElementUI);

/* eslint-disable no-new */
new Vue({
  el: '#app',
  render: '<App/>',
  components: { App },
});

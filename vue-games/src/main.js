import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap.bundle.min.js';
import '../../static/css/_base.css';

import { createApp } from 'vue';
import router from './router';

import App from './App.vue';

const app = createApp(App);

app.use(router);

app.mount('#app');

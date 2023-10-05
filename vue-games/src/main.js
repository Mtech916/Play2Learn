import axios from 'axios';
import VueAxios from 'vue-axios';

import '../../static/css/_base.css';


import { createApp } from 'vue';
import router from './router';

import App from './App.vue';

const app = createApp(App);

app.use(router);
app.use(VueAxios, axios);

app.mount('#app');

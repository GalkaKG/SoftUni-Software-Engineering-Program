import { createApp } from 'vue';
import App from './App.vue';
import vRipple from './directives/vRipple';

createApp(App).directive('ripple', vRipple).mount('#app');

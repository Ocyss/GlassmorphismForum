import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import axios from "axios";
import VueCookies from "vue-cookies";

const app = createApp(App);

app.config.globalProperties.$axios = axios;
app.config.globalProperties.$cookies = VueCookies;
app.use(router).mount("#app");

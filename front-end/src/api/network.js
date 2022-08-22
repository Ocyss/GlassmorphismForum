import axios from "axios";
import Vue from "vue";

axios.defaults.baseURL = "http:127.0.0.1:3000";
axios.defaults.timeout = 5000;

let count = 0;

axios.interceptors.request.use(
  function (config) {
    count++;
    Vue.showLoading();
    return config;
  },
  function (error) {
    Vue.hiddenLoading();
    return Promise.reject(error);
  }
);

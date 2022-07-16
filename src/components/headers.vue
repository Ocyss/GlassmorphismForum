<template>
  <div class="header">
    <div class="logo">
      <img src="../assets/logo150.png" alt="LOGO" />
    </div>
    <div class="searchBox">
      <n-input :style="{ width: '80%' }" />
      <n-button type="primary" ghost> 搜索 </n-button>
    </div>
    <div class="navigation">
      <n-icon size="28">
        <WeatherMoon28Filled />
      </n-icon>
      <n-icon size="28">
        <People16Filled />
      </n-icon>
      <n-icon size="28">
        <MailMultiple16Filled />
      </n-icon>

      <div class="personal" v-if="islo">
        <n-avatar
          round
          :size="30"
          :src="uinfo.avatar"
          v-if="uinfo.avatar != null"
        />
        <n-avatar round :size="30" v-else>{{ uinfo.name }}</n-avatar>
        <div class="name">{{ uinfo.name }}</div>
        <h1>&nbsp&nbsp&nbsp&nbsp</h1>
        <n-button @click="sign" type="error" size="tiny"> 退出登陆 </n-button>
      </div>
      <login v-else @setislo="setislo" />
    </div>
  </div>
</template>

<script setup>
import {
  MailMultiple16Filled,
  People16Filled,
  WeatherSunny32Filled,
  WeatherMoon28Filled,
} from "@vicons/fluent";
import { ref } from "vue";
import login from "./headers/login.vue";
import { getCurrentInstance } from "vue";
import { userInfo } from "../store/userInfo";
const uinfo = userInfo();
const internalInstance = getCurrentInstance();
const internalData = internalInstance.appContext.config.globalProperties;

let islo = ref(internalData.$cookies.get("token") != null);

function sign() {
  // window.$message.success(`再见~~ ${response.data.data.name}`);
  $cookies.config("0"); //一个月
  // 设置cookies
  if ($cookies.isKey("token")) {
    $cookies.remove("token");
  }
  uinfo.$reset();
  islo.value = false;
}

function setislo() {
  islo.value = internalData.$cookies.get("token") != null;
}
</script>

<style scoped>
.header {
  display: flex;
  width: 100%;
  min-width: 500px;
  justify-content: space-evenly;
  align-items: center;
  position: fixed;
  top: 0;
  left: 0;
  z-index: 9999;
  height: 3.125rem;
  background: rgba(255, 255, 255, 0.6);
  backdrop-filter: blur(40px);
}

.searchBox {
  width: 280px;
}

.logo img {
  width: 50px;
  height: 50px;
}

.navigation {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.navigation i {
  margin-right: 25px;
}

.personal {
  display: flex;
  justify-content: center;
  align-items: center;
}
.personal .name {
  font-size: 1.2rem;
}
</style>

<template>
  <div class="header">
    <div class="logo" @click="router.push('/')">
      <img src="../assets/logo150.png" alt="LOGO" />
    </div>
    <div class="searchBox">
      <n-input :style="{ width: '80%' }" />
      <n-button type="primary" ghost> 搜索 </n-button>
    </div>
    <div class="navigation">
      <n-icon size="28" class="darkSwitching" @click="opti.theme_toggle()">
        <MoonSharp v-if="opti.theme == null" />
        <SunnySharp v-else />
      </n-icon>
      <n-popover trigger="hover" raw :show-arrow="false" style="width: 15vw">
        <template #trigger>
          <n-icon size="28">
            <PeopleCircleOutline />
          </n-icon>
        </template>
        <contacts />
      </n-popover>
      <n-popover trigger="hover" raw :show-arrow="false" style="width: 15vw">
        <template #trigger>
          <n-icon size="28">
            <MailSharp />
          </n-icon>
        </template>
        <notice />
      </n-popover>

      <personal v-if="islo" @logout="logout" />
      <login v-else @setislo="setislo" />
    </div>
  </div>
</template>

<script setup>
import {
  MailSharp,
  PeopleCircleOutline,
  SunnySharp,
  MoonSharp,
} from "@vicons/ionicons5";
import { ref, getCurrentInstance } from "vue";
import login from "./headers/login.vue";
import personal from "./headers/personal.vue";
import contacts from "./headers/contacts.vue";
import notice from "./headers/notice.vue";
import { userInfo } from "../store/userInfo";
import { useRouter } from "vue-router";
import { useMessage } from "naive-ui";
import { Options } from "../store/options";

const opti = Options();
const message = useMessage();
const router = useRouter();
const uinfo = userInfo();
const internalInstance = getCurrentInstance();
const internalData = internalInstance.appContext.config.globalProperties;

let islo = ref(internalData.$cookies.get("token") != null);

function setislo() {
  islo.value = internalData.$cookies.get("token") != null;
}

function logout() {
  message.success(`再见~~ ${uinfo.name}`);
  $cookies.config("0"); //一个月
  // 设置cookies
  if ($cookies.isKey("token")) {
    $cookies.remove("token");
  }
  uinfo.$reset();
  islo.value = false;
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
.logo {
  cursor: pointer;
  user-select: none;
  position: relative;
  z-index: 99;
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

.darkSwitching {
  cursor: pointer;
}
</style>

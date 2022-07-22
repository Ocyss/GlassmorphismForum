<template>
  <n-message-provider>
    <headers />
    <n-config-provider
      :locale="locale"
      :date-locale="dateLocale"
      :key="viewKey"
    >
      <router-view></router-view>
    </n-config-provider>
  </n-message-provider>
</template>

<script setup>
import { ref } from "vue";
import headers from "./components/headers.vue";
import { zhCN, dateZhCN } from "naive-ui";
let dt = new Date();
const viewKey = ref(dt.getMinutes());
const locale = ref(zhCN);
const dateLocale = ref(dateZhCN);
</script>

<style>
#app {
  width: 100vw;
  min-width: 500px;
  min-height: 100vh;
  position: relative;
  z-index: 10;
}

* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
  font-family: Helvetica, "Microsoft Yahei", sans-serif;
}
:root {
  font-size: 15px;
}

body {
  font-family: "Quicksand", sans-serif;
  margin: 0;
  min-height: 100vh;
  background: linear-gradient(
    135deg,
    hsl(170deg, 80%, 80%),
    hsl(190deg, 80%, 80%),
    hsl(250deg, 80%, 80%),
    hsl(320deg, 80%, 80%)
  );
  background-size: 200% 200%;
  animation: gradient-move 15s ease alternate infinite;
}

@keyframes gradient-move {
  0% {
    background-position: 0% 0%;
  }
  100% {
    background-position: 100% 100%;
  }
}

.overallContent {
  position: absolute;
  top: 4.5rem;
  left: 12vw;
  width: 76vw;
  min-width: 750px;
  height: 88vh;
  box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
  backdrop-filter: blur(2px);
  -webkit-backdrop-filter: blur(2px);
  border-radius: 10px;
  border: 1px solid rgba(255, 255, 255, 0.18);
  overflow: hidden;
  background: rgba(246, 247, 246, 0.35);
  display: flex;
  align-items: center;
  overflow-y: scroll;
  scroll-behavior: smooth;
  overscroll-behavior: contain;
}
</style>

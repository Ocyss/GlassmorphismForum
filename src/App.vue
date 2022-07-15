<template>
  <n-message-provider>
    <headers />
  </n-message-provider>
  <router-view></router-view>
  <router-link to="/">Home</router-link> |
  <router-link to="/about">About</router-link>
</template>

<script setup>
import headers from "./components/headers.vue";
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
</style>

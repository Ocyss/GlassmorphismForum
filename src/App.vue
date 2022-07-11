<template>
  <n-config-provider :theme="theme">
    <router-view></router-view>
  </n-config-provider>
  <router-link o="/">Home</router-link> |
  <router-link :key="index" to="/about">About</router-link>
</template>

<!-- <script setup>
import { defineComponent, ref } from "vue";
import { darkTheme } from "naive-ui";

const theme = ref(null);
</script> -->
<script>
import { defineComponent, ref } from "vue";
import { darkTheme } from "naive-ui";

export default defineComponent({
  setup() {
    return {
      darkTheme,
      theme: ref(null),
    };
  },
});
</script>

<style>
#app {
  width: 100vw;
  min-width: 500px;
  min-height: 100vh;
}

body {
  height: 100%;
  width: 100%;
  background: linear-gradient(
    90deg,
    rgba(166, 254, 237, 1) 0%,
    rgba(255, 196, 244, 1) 50%,
    rgba(240, 185, 128, 1) 100%
  );
}

* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
  font-family: Helvetica, "Microsoft Yahei", sans-serif;
}
</style>

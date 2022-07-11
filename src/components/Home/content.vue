<template>
  <div class="content">
    <postVue v-for="(item, index) in 40" :key="index" />
  </div>
</template>

<script setup>
import postVue from "./main/post.vue";
</script>
<style scoped>
.content {
  background: rgba(255, 255, 255, 0.5);
  width: 44vw;
  position: absolute;
  top: 4.5rem;
  left: 28vw;
  height: 88vh;
  overflow-y: scroll;
  scroll-behavior: smooth;
  overscroll-behavior: contain;
  border-style: solid none solid none;
  border-width: 2px;
  border-color: #fff;
}

::-webkit-scrollbar {
  width: 5px;
}

::-webkit-scrollbar-thumb {
  background: rgb(255, 76, 162);
}
</style>

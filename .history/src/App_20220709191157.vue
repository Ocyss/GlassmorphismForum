<template>
  <router-view></router-view>
  <router-link to="/">Home</router-link> |
  <router-link to="/about">About</router-link>
</template>

<script setup>

</script>



<style>
#app {
  width: 100vw;
  min-width: 500px;
  min-height: 100vh;
  background: rgb(203, 210, 240);
}

* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
  font-family: Helvetica, "Microsoft Yahei", sans-serif;

}
</style>
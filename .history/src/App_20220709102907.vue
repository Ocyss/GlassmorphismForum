<template>
  <div class="页头">
    <div class="logo">
      <img src="./assets/logo.png" alt="LOGO">
    </div>
    <div class="搜索框">
      <n-input :style="{ width: '50%' }" />
      <n-button type="primary" ghost>
        搜索
      </n-button>
    </div>
    <div class="导航"></div>
  </div>
  <div class="侧边导航"></div>
  <div class="侧边资料"></div>
  <div class="主体"></div>

</template>

<script setup>

</script>

<style scoped>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  width: 100vh;
}

.logo img {
  width: 50px;
  height: 50px;
}
</style>

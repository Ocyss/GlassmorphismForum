<template>
  <div class="main">
    <div class="pageHeader">
      <div class="logo">
        <img src="./assets/logo.png" alt="LOGO">
      </div>
      <div class="搜索框">
        <n-input :style="{ width: '20%' }" />
        <n-button type="primary" ghost>
          搜索
        </n-button>
      </div>
      <div class="导航"></div>
    </div>
    <div class="侧边导航"></div>
    <div class="侧边资料"></div>
    <div class="主体"></div>
  </div>
</template>

<script setup>

</script>



<style scoped>
.main {
  display: grid;
  grid-template-areas:
    "";
}

.pageHeader {
  width: 100%;
}

.logo img {
  width: 50px;
  height: 50px;
}
</style>


<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  width: 100%;
  min-width: 500px;
}
</style>
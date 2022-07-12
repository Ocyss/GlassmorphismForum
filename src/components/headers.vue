<template>
  <div class="header">
    <div class="logo">
      <img src="../assets/logo.png" alt="LOGO" />
    </div>
    <div class="searchBox">
      <n-input :style="{ width: '80%' }" />
      <n-button type="primary" ghost> 搜索 </n-button>
    </div>
    <div class="navigation">
      <n-icon v-if="theme == null" size="28" @click="theme = darkTheme">
        <WeatherMoon28Filled />
      </n-icon>
      <n-icon v-else-if="theme == darkTheme" size="28" @click="theme = null">
        <WeatherSunny32Filled />
      </n-icon>

      <n-icon size="28">
        <People16Filled />
      </n-icon>

      <n-icon size="28">
        <MailMultiple16Filled />
      </n-icon>

      <div>
        <n-avatar
          round
          :size="30"
          src="https://assets.paopao.info/public/avatar/55/0a/ce/15/75dd-4bec-be1d-125fd1bbdfb7.png"
        />
      </div>
      <div>Qiudie</div>
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
</script>

<style scoped>
.header {
  display: flex;
  width: 100%;
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
</style>

<template>
  <div id="main">
    <div class="header">
      <div class="logo">
        <img src="./assets/logo.png" alt="LOGO">
      </div>
      <div class="searchBox">
        <n-input :style="{ width: '80%' }" />
        <n-button type="primary" ghost>
          搜索
        </n-button>
      </div>
      <div class="导航"></div>
    </div>
    <div class="leftside">
      <div class="重要导航">
        <span>
          <icon></icon>主页
        </span><span>精选</span><span>关注</span>
      </div>
      <div></div>
    </div>
    <div class="rightside"></div>
    <div class="main"></div>
  </div>
</template>

<script setup>
import { Icon } from '@vicons/utils'
import { Home } from '@vicons/fluent'
</script>



<style scoped>
#main {
  display: grid;
  grid-template-areas:
    "header header header header header"
    "leftside content content content rightside";
  align-items: center;
}

.header {
  display: flex;
  width: 100%;
  grid-area: header;
  justify-content: space-evenly;
}

.searchBox {
  width: 280px;
}

.leftside {
  grid-area: leftside;
  background-color: aqua;
}

.rightside {
  grid-area: rightside;
  background: #000;
}

.main {
  grid-area: content;
  background: rgb(204, 3, 3);
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
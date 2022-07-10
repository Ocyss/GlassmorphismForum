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
          <icon size="20">
            <Home24Filled />
          </icon>
          主页
        </span>
        <span>
          <icon size="20">
            <Sticker24Filled />
          </icon>
          精选
        </span>
        <span>
          <icon size="20">
            <Star24Filled />
          </icon>
          关注
        </span>
      </div>
      <div>
        <n-collapse arrow-placement="right">
          <n-collapse-item title="我的关注" name="1">
            <div>可以</div>
          </n-collapse-item>
          <n-collapse-item title="热门话题" name="2">
            <div>很好</div>
          </n-collapse-item>
          <n-collapse-item title="数码话题" name="3">
            <div>真棒</div>
          </n-collapse-item>
        </n-collapse>
      </div>
    </div>
    <div class="rightside">
      <div class="个人信息"></div>
      <div class="关注好友"></div>
    </div>
    <div class="main"></div>
  </div>
</template>

<script setup>
import { Icon } from '@vicons/utils'
import { Home24Filled, Sticker24Filled, Star24Filled } from '@vicons/fluent'
</script>



<style scoped>
#main {
  display: grid;
  grid-template-areas:
    "header header header header header"
    "leftside content content content rightside";
  align-items: center;
  justify-items: center;
}

.header {
  display: flex;
  width: 100%;
  grid-area: header;
  justify-content: space-evenly;
  position: fixed;
}

.searchBox {
  width: 280px;
}

.leftside {
  grid-area: leftside;
  background-color: aqua;
  position: fixed;
}

.rightside {
  grid-area: rightside;
  background: #000;
  position: fixed;
}

.main {
  grid-area: content;
  background: rgb(204, 3, 3);
  height: 1500px;
}

.logo img {
  width: 50px;
  height: 50px;
}
</style>


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
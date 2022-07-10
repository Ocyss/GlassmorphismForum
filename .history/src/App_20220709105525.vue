<template>
  <div id="main">
    <div class="header">
      <div class="logo">
        <img src="./assets/logo.png" alt="LOGO">
      </div>
      <div class="searchBox">
        <n-input />
        <n-button type="primary" ghost>
          搜索
        </n-button>
      </div>
      <div class="导航"></div>
    </div>
    <div class="leftside"></div>
    <div class="rightside"></div>
    <div class="main"></div>
  </div>
</template>

<script setup>

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

.searchBox .n-input {
  width: 180px;
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
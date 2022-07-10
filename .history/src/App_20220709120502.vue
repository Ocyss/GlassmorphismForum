<template>

  <router-link to="/">Home</router-link> |
  <router-link to="/about">About</router-link>
  <router-view></router-view>
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
  justify-items: center;
}

.header {
  display: flex;
  width: 100%;
  grid-area: header;
  justify-content: space-evenly;
  position: fixed;
  top: 0;
  left: 0;
  z-index: 9999;
  height: 3.75rem;
  background: hsla(0, 0%, 100%, .9);
  backdrop-filter: blur(40px);
}

.searchBox {
  width: 280px;
}

.leftside {
  grid-area: leftside;
  background-color: aqua;
  position: fixed;
  left: 0;
  top: 3.75rem;
  z-index: 9999;
  width: 15%;
}

.rightside {
  grid-area: rightside;
  background: rgb(105, 221, 153);
  position: fixed;
  right: 0;
  top: 3.75rem;
  z-index: 9999;
  width: 15%;
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
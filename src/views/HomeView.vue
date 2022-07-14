<template>
  <div class="Home">
    <div class="leftside">
      <leftside />
    </div>
    <div class="content" id="image-scroll-container">
      <content v-for="item in PostData" :key="item.id" :pd="item" />
    </div>
    <div class="rightside"><rightside /></div>
  </div>
</template>

<script setup>
import leftside from "../components/Home/leftside.vue";
import rightside from "../components/Home/rightside.vue";
import content from "../components/Home/content.vue";
import { ref, onMounted, getCurrentInstance } from "vue";
const { proxy } = getCurrentInstance();
const PostData = ref([]);

onMounted(() => {
  // proxy.$axios.get("http://localhost:5000/getPostList").then(function (result) {
  //   for (let d in result.data.data) {
  //     console.log(result.data.data[d]);
  //     PostData.value.push(result.data.data[d]);
  //   }
  // });
});
</script>

<style scoped>
.Home {
  position: absolute;
  top: 4.5rem;
  left: 12vw;
  width: 76vw;
  min-width: 750px;
  height: 88vh;
  display: flex;
  justify-content: center;
  align-items: center;
  box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
  backdrop-filter: blur(2px);
  -webkit-backdrop-filter: blur(2px);
  border-radius: 10px;
  border: 1px solid rgba(255, 255, 255, 0.18);
  overflow: hidden;
}

.leftside {
  background-color: rgba(246, 247, 246, 0.65);
  width: 21%;
  height: 100%;
  overflow-y: scroll;
  scroll-behavior: smooth;
  overscroll-behavior: contain;
}

.rightside {
  background: rgba(246, 247, 246, 0.15);
  backdrop-filter: blur(2px);
  width: 21%;
  height: 100%;
  overflow-y: scroll;
  scroll-behavior: smooth;
  overscroll-behavior: contain;
}

.content {
  background: rgba(246, 247, 246, 0.4);
  width: 58%;
  height: 100%;
  overflow-y: scroll;
  scroll-behavior: smooth;
  overscroll-behavior: contain;
}

::-webkit-scrollbar {
  width: 5px;
}

::-webkit-scrollbar-thumb {
  background: rgb(255, 76, 162);
}
</style>

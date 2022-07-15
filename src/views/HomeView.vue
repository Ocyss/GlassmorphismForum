<template>
  <div class="Home">
    <div class="leftside" @click="rightContent = '热榜'">
      <leftside />
    </div>
    <n-message-provider>
      <div class="content" id="image-scroll-container">
        <content
          v-for="item in PostData"
          :key="item.id"
          :pd="item"
          @click="getComment(item.id)"
        />
      </div>
    </n-message-provider>
    <div class="rightside">
      <rightside v-if="rightContent == '热榜'" />
      <div class="comment" v-else-if="rightContent == '评论'" :key="poid">
        <comment :postid="poid" />
      </div>
    </div>
  </div>
</template>

<script setup>
import leftside from "../components/Home/leftside.vue";
import rightside from "../components/Home/rightside.vue";
import content from "../components/Home/content.vue";
import comment from "../components/Home/comment.vue";
import { ref, onMounted, getCurrentInstance } from "vue";
const { proxy } = getCurrentInstance();
const PostData = ref([]);
const rightContent = ref("热榜");
const poid = ref(null);

onMounted(() => {
  proxy.$axios.get("/api/getPostList").then(function (result) {
    for (let d in result.data.data) {
      PostData.value.push(result.data.data[d]);
    }
  });
});

function getComment(postid) {
  if (rightContent.value == "评论" && postid != poid.value) {
    poid.value = postid;
  } else if (rightContent.value != "评论") {
    rightContent.value = "评论";
    poid.value = postid;
  } else {
    return null;
  }
}
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

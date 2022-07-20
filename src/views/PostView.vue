<template>
  <div class="overallContent" style="flex-direction: column">
    <div class="content"><postContent :redata="$route.query" /></div>
    <div class="comment">
      <postComment :commentData="item" v-for="(item, index) in CommentData" />
    </div>
  </div>
</template>

<script setup>
import postContent from "../components/Post/postContent.vue";
import postComment from "../components/Post/postComment.vue";
import axios from "axios";
import { useRoute } from "vue-router";
import { ref, onMounted } from "vue";
import { useMessage } from "naive-ui";

const message = useMessage();
const $route = useRoute();
const CommentData = ref([]);

function getComment(li) {
  axios({
    url: "/api/getCommentList",
    method: "post",
    data: { postid: $route.query.postid, limit: li },
  }).then(function (response) {
    if (response.data.code != 200) {
      message.error(response.data.msg);
    } else {
      for (let d in response.data.data) {
        CommentData.value.push(response.data.data[d]);
      }
    }
  });
}

onMounted(() => {
  getComment(1);
});
</script>

<style scoped>
.content {
  width: 100%;
  background: rgba(246, 247, 246, 0.9);
  display: flex;
  flex-direction: column;
  align-items: center;
}

.comment {
  width: 100%;
  background: rgba(240, 240, 240, 0.9);
  display: flex;
  flex-direction: column;
  align-items: center;
}
</style>

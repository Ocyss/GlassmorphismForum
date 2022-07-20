<template>
  <div class="commentmain" id="comment-avatar">
    <div class="comment" v-for="(item, index) in CommentData" :key="item.id">
      <Comment :data="item" />
    </div>
    <n-pagination
      v-model:page="page"
      :page-count="parseInt(props.plun_num / 10)"
      :page-slot="3"
      v-if="parseInt(props.plun_num / 10) > 1"
      @update:page="getComment(page)"
      size="small"
      class="pagination"
    />
    <h2 v-if="props.plun_num == 0">
      <br /><br /><br />还没用评论呢，赶快抢沙发呀！
    </h2>
  </div>
  <div class="postComments">
    <n-input-group class="editor">
      <n-input
        v-model:value="value"
        placeholder="快评论"
        type="textarea"
        size="small"
        :autosize="{
          minRows: 1,
          maxRows: 5,
        }"
      />
      <n-button type="primary" @click="sendComment"> 评论 </n-button>
    </n-input-group>
  </div>
</template>

<style scoped>
.commentmain {
  overflow-y: scroll;
  scroll-behavior: smooth;
  overscroll-behavior: contain;
  width: 100%;
  display: flex;
  align-items: center;
  flex-direction: column;
  padding-bottom: 50px;
}
.comment {
  width: 70%;
  display: flex;
  margin: 10px auto;
  background: rgba(255, 255, 255, 0.6);
  padding: 10px;
  padding-right: 10px;
  border-radius: 16px;
  flex-direction: column;
}

::-webkit-scrollbar {
  width: 3px;
}

::-webkit-scrollbar-thumb {
  background: rgb(187, 69, 255);
}

.postComments {
  padding: 5px 0 0 0;
  position: absolute;
  width: 100%;
  bottom: 0;
}
</style>

<script setup>
import Comment from "./comment.vue";
import { ref, onMounted } from "vue";
import axios from "axios";
import { useMessage } from "naive-ui";
import { userInfo } from "../../store/userInfo";
const uinfo = userInfo();
const message = useMessage();
const props = defineProps(["postid", "plun_num"]);
const CommentData = ref([]);
const page = ref(1);
const value = ref(null);

function sendComment() {
  const data = ref({
    postid: props.postid,
    content: value.value,
    imgs: [],
  });
  axios({
    url: "/api/sendComment",
    method: "post",
    data: data.value,
  }).then(function (response) {
    if (response.data.code != 200) {
      message.error(response.data.msg);
    } else {
      let Text = ref({
        avatar: uinfo.avatar,
        content: value.value,
        id: -1,
        imgs: "[]",
        name: uinfo.name,
        permission: uinfo.permission,
        postid: props.postid,
        userid: uinfo.uid,
      });
      CommentData.value.push(Text.value);
      value.value = "";
      message.success(response.data.msg);
    }
  });
}

function getComment(li) {
  axios({
    url: "/api/getCommentList",
    method: "post",
    data: { postid: props.postid, limit: li },
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
  if (props.plun_num != 0) {
    getComment(1);
  }
});
</script>

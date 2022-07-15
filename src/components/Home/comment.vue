<template>
  <div class="comment" v-for="(item, index) in CommentData" :key="item.id">
    <div class="avatar">
      <n-avatar round :size="30" v-if="true">{{ item.name }}</n-avatar>
      <n-avatar
        round
        :size="30"
        v-else
        :src="item.avatar"
        fallback-src="https://07akioni.oss-cn-beijing.aliyuncs.com/07akioni.jpeg"
        lazy
        :intersection-observer-options="{
          root: '#image-scroll-container',
        }"
      />
      <div class="information">
        <n-skeleton v-if="loading" width="100%" :sharp="false" />
        <div class="name">{{ item.name }}</div>
        <div class="time">
          <n-time
            :time="item.comment_time"
            unix
            type="relative"
            time-zone="Asia/Shanghai"
          />
        </div>
      </div>
    </div>
    <div class="main">
      <n-skeleton
        v-if="loading"
        width="100%"
        :height="15"
        :sharp="false"
        text
        :repeat="4"
        size="medium"
      />
      <div class="content">{{ item.content }}</div>
      <div class="pictureGroup"></div>
    </div>
  </div>
</template>

<style scoped>
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
.avatar {
  display: flex;
  align-items: center;
}

.information {
  margin-left: 10px;
}
.information .name {
  font-size: 16px;
}
.information .time {
  font-size: 5px;
  color: rgb(122, 128, 120);
}

::-webkit-scrollbar {
  width: 5px;
}

::-webkit-scrollbar-thumb {
  background: rgb(253, 0, 0);
}
</style>

<script setup>
import { ref, onMounted } from "vue";
import axios from "axios";
import { userInfo } from "../../store/userInfo";
const uinfo = userInfo();
const props = defineProps(["postid"]);
const CommentData = ref([1, 2, 3, 4, 5, 6]);
const loading = ref(true);
onMounted(() => {
  var data = axios({
    url: "/api/getCommentList",
    method: "post",
    data: { postid: props.postid },
  }).then(function (response) {
    if (response.data.code != 200) {
      message.error(response.data.msg);
    } else {
      for (let i = 0; i < 7; i++) {
        CommentData.value.splice(0, 1);
      }

      for (let d in response.data.data) {
        CommentData.value.push(response.data.data[d]);
      }
      loading.value = false;
    }
  });
});
</script>

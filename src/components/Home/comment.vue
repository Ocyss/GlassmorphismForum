<template>
  <div>
    <div class="avatar">
      <n-avatar
        round
        :size="30"
        v-if="(props.data.avatar == null) | (props.data.avatar == '')"
        >{{ props.data.name }}</n-avatar
      >
      <n-avatar
        round
        :size="30"
        v-else
        :src="props.data.avatar"
        fallback-src="/files/liekai.png"
        lazy
        :intersection-observer-options="{
          root: '#comment-avatar',
        }"
      />
      <div class="information">
        <div class="name">{{ props.data.name }}</div>
        <div class="time">
          <n-time
            :time="props.data.comment_time"
            unix
            type="relative"
            time-zone="Asia/Shanghai"
          />
        </div>
      </div>
    </div>
    <div class="main">
      <div class="content">{{ props.data.content }}</div>
      <div class="pictureGroup"></div>
      <div class="operation">
        <div @click="actionClick(props.data)" class="zan">
          <n-icon size="15" color="rgb(90,90,90)">
            <ThumbLike16Filled v-if="zans" />
            <ThumbLike16Regular v-else /> </n-icon
          >{{ zan }}
        </div>
        <!-- <div>
            <n-icon size="15" color="rgb(90,90,90)">
              <Comment16Regular
            /></n-icon>
            {{ plun }}
          </div> -->
      </div>
    </div>
  </div>
</template>

<style scoped>
.operation {
  display: flex;
  justify-content: space-around;
}

.operation .zan {
  cursor: pointer;
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
</style>

<script setup>
import {
  ThumbLike16Regular,
  Comment16Regular,
  ThumbLike16Filled,
  ImageMultiple28Regular,
} from "@vicons/fluent";
import { ref } from "vue";
import axios from "axios";
import { useMessage } from "naive-ui";
import { userInfo } from "../../store/userInfo";
const uinfo = userInfo();
const message = useMessage();
const props = defineProps(["data"]);
const zans = ref(uinfo.uid in props.data.zan);
const zan = ref(Object.keys(props.data.zan).length);
// const plun = ref(0);

function actionClick(comment) {
  if (uinfo.token == "") {
    message.error("孩子你还没登陆呢，在想什么呢？？");
  } else {
    const operateData = {
      comment_userid: props.data.userid,
      commentid: comment.id,
      type: "comment_zan",
      isCancel: zans.value,
    };
    axios({
      url: "/api/operate",
      method: "post",
      data: operateData,
    }).then(function (response) {
      if (response.data.code != 200) {
        message.error(response.data.msg);
      } else {
        if (response.data.ty == "add") {
          zan.value++;
          zans.value = true;
        } else if (response.data.ty == "re") {
          zan.value--;
          zans.value = false;
        }
      }
    });
  }
}
</script>

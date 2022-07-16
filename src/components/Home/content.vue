<template>
  <div class="post">
    <div class="avatar">
      <n-avatar
        round
        :size="30"
        v-if="(props.pd.avatar == null) | (props.pd.avatar == '')"
        >{{ props.pd.name }}
      </n-avatar>
      <n-avatar
        round
        :size="30"
        v-else
        :src="props.pd.avatar"
        fallback-src="https://07akioni.oss-cn-beijing.aliyuncs.com/07akioni.jpeg"
        lazy
        :intersection-observer-options="{
          root: '#image-scroll-container',
        }"
      />
    </div>
    <div class="main">
      <div class="information">
        <div class="name">{{ props.pd.name }}</div>
        <div class="time">
          <n-time
            :time="props.pd.post_time"
            unix
            type="relative"
            time-zone="Asia/Shanghai"
          />
        </div>
      </div>
      <div class="content">
        {{ props.pd.content }}
      </div>
      <div class="pictureGroup">
        <n-image-group>
          <n-space>
            <n-image
              v-for="(src, index) in props.pd.imgs"
              :key="index"
              hidden="100"
              lazy
              :src="'https://picsum.photos/id/4/100/100'"
              :intersection-observer-options="{
                root: '#image-scroll-container',
              }"
            />
          </n-space>
        </n-image-group>
      </div>
      <div class="operation">
        <div @click="actionClick('zan')">
          <n-icon size="20" color="rgb(90,90,90)">
            <ThumbLike16Filled v-if="zans" />
            <ThumbLike16Regular v-else /> </n-icon
          >{{ zan }}
        </div>
        <div @click="getComment(props.pd.id)">
          <n-icon size="20"> <Comment16Regular /></n-icon>
          {{ plun }}
        </div>
        <div @click="actionClick('scang')">
          <n-icon size="20" color="rgb(90,90,90)">
            <Star16Filled v-if="scangs" />
            <Star16Regular v-else /> </n-icon
          >{{ scang }}
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import {
  ThumbLike16Regular,
  ThumbDislike16Regular,
  Star16Regular,
  Comment16Regular,
  ThumbLike16Filled,
  ThumbDislike16Filled,
  Star16Filled,
  Comment16Filled,
} from "@vicons/fluent";
import { ref } from "vue";
import axios from "axios";
import { userInfo } from "../../store/userInfo";
import { useMessage } from "naive-ui";
import { Options } from "../../store/options";
const opti = Options();
const uinfo = userInfo();
const message = useMessage();
const props = defineProps(["pd"]);

const zan = ref(props.pd.zan_num);
const scang = ref(props.pd.scang_num);
const plun = ref(props.pd.plun_num);
const zans = ref(uinfo.uid in props.pd.zan);
const scangs = ref(uinfo.uid in props.pd.scang);

function getComment(postid) {
  if (opti.rightContent != "评论") {
    opti.rightContent = "评论";
    opti.postid = postid;
    opti.commenttotal = plun.value;
  } else if (opti.rightContent == "评论" && postid != opti.poid) {
    opti.postid = postid;
    opti.commenttotal = plun.value;
  }
}

function actionClick(type) {
  const operateData = {
    post_userid: props.pd.userid,
    postid: props.pd.id,
    type: type,
    isCancel: type == "zan" ? zans.value : scangs.value,
  };
  var data = axios({
    url: "/api/operate",
    method: "post",
    data: operateData,
  }).then(function (response) {
    if (response.data.code != 200) {
      message.error(response.data.msg);
    } else {
      if (response.data.ty == "add") {
        if (type == "zan") {
          zan.value++;
          zans.value = true;
        } else if (type == "scang") {
          scang.value++;
          scangs.value = true;
        }
      } else if (response.data.ty == "re") {
        if (type == "zan") {
          zan.value--;
          zans.value = false;
        } else if (type == "scang") {
          scang.value--;
          scangs.value = false;
        }
      }
    }
  });
}
</script>

<style scoped>
.post {
  width: 80%;
  /* height: 200px; */
  margin: 20px auto;
  font-size: 0.8rem;
  background: rgb(255, 255, 255);
  display: flex;
  padding: 10px;
  padding-right: 40px;
  border-radius: 25px;
}

.avatar {
  margin-right: 5px;
}
.information {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.information .name {
  color: rgb(54, 59, 100);
  margin-right: 5px;
  font-size: 1.2rem;
}
.information .time {
  font-size: 0.6rem;
  color: rgb(145, 148, 170);
  float: right;
}
.main {
  width: 100%;
}
.pictureGroup {
  margin-top: 10px;
}
.operation {
  display: flex;
  justify-content: space-between;
  margin-top: 12px;
}

.operation div {
  display: flex;
  align-items: center;
  cursor: pointer;
  user-select: none;
}
</style>

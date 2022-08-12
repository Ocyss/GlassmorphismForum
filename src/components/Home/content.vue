<template>
  <div class="post">
    <div class="avatar">
      <n-avatar
        round
        :size="30"
        v-if="(props.pd.avatar == null) | (props.pd.avatar === '')"
        >{{ props.pd.name }}
      </n-avatar>
      <n-avatar
        round
        :size="30"
        v-else
        :src="props.pd.avatar"
        fallback-src="/files/liekai.png"
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
      <div class="title">
        <h3>{{ props.pd.title }}</h3>
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
              width="100"
              height="100"
              object-fit="contain"
              lazy
              fallback-src="/files/liekai.png"
              :src="src"
              :intersection-observer-options="{
                root: '#image-scroll-container',
              }"
            />
          </n-space>
        </n-image-group>
      </div>
      <div class="topic">
        <n-tag
          :color="{
            color: 'rgba(163, 94, 232, 0.5)',
            borderColor: 'rgb(180,240,180)',
            textColor: '#FFFFFF',
          }"
          size="small"
          style="margin: 0px 5px"
          v-for="topic in props.pd.topic_id"
          :key="topic"
        >
          {{ opti.topic_data[topic] ? opti.topic_data[topic].name : "" }}
          <template #avatar>
            <n-avatar
              :src="opti.topic_data[topic] ? opti.topic_data[topic].logo : ''"
            />
          </template>
        </n-tag>
      </div>
      <div class="operation">
        <div @click.stop="actionClick('zan')">
          <n-icon size="20" color="rgb(90,90,90)">
            <Rose v-if="zans" />
            <RoseOutline v-else /> </n-icon
          >{{ zan }}
        </div>
        <div @click.stop="getComment">
          <n-icon size="20" color="rgb(90,90,90)">
            <ChatboxEllipsesOutline
          /></n-icon>
          {{ plun }}
        </div>
        <div @click.stop="actionClick('scang')">
          <n-icon size="20" color="rgb(90,90,90)">
            <StarSharp v-if="scangs" />
            <StarOutline v-else /> </n-icon
          >{{ scang }}
        </div>
      </div>
    </div>
    <div class="jumpto" @click.stop="jumpTo"></div>
  </div>
</template>

<script setup>
import {
  RoseOutline,
  StarOutline,
  ChatboxEllipsesOutline,
  Rose,
  StarSharp,
} from "@vicons/ionicons5";

import { ref, inject } from "vue";
import axios from "axios";
import { userInfo } from "../../store/userInfo";
import { useMessage } from "naive-ui";
import { Options } from "../../store/options";
import { useRouter } from "vue-router";
const router = useRouter();
const opti = Options();
const uinfo = userInfo();
const message = useMessage();
const props = defineProps(["pd"]);

const zan = ref(Object.keys(props.pd.zan).length);
const scang = ref(Object.keys(props.pd.scang).length);
const plun = ref(props.pd.plun_num);
const zans = ref(uinfo.uid in props.pd.zan);
const scangs = ref(uinfo.uid in props.pd.scang);

function jumpTo() {
  let routeUrl = router.resolve({
    path: "/post",
    query: {
      postid: props.pd.id,
    },
  });
  window.open(routeUrl.href, "_blank");
}

function actionClick(type) {
  console.log(uinfo.token);
  if (uinfo.token === "") {
    message.error("孩子你还没登陆呢，在想什么呢？？");
  } else {
    const operateData = {
      post_userid: props.pd.userid,
      postid: props.pd.id,
      type: type,
      isCancel: type === "zan" ? zans.value : scangs.value,
    };
    axios({
      url: "/api/operate",
      method: "post",
      data: operateData,
    }).then(function (response) {
      if (response.data.code !== 200) {
        message.error(response.data.msg);
      } else {
        if (response.data.ty === "add") {
          if (type === "zan") {
            zan.value++;
            zans.value = true;
          } else if (type === "scang") {
            scang.value++;
            scangs.value = true;
          }
        } else if (response.data.ty === "re") {
          if (type === "zan") {
            zan.value--;
            zans.value = false;
          } else if (type === "scang") {
            scang.value--;
            scangs.value = false;
          }
        }
      }
    });
  }
}

const YgetComment = inject("YgetComment");
const getComment = function () {
  YgetComment(props.pd.id, props.pd.plun_num);
};
</script>

<style scoped>
.post {
  width: 95%;
  /* height: 200px; */
  margin: 1.5% 2.5%;
  font-size: 0.8rem;
  background: rgb(255, 255, 255);
  display: flex;
  padding: 10px 40px 10px 10px;
  border-radius: 25px;
  position: relative;
  z-index: 1;
}

.avatar {
  margin-right: 5px;
  z-index: 10;
  display: inline-block;
  height: 40px;
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
  z-index: 10;
}
.pictureGroup {
  margin-top: 10px;
}
.operation {
  display: flex;
  justify-content: space-between;
  margin-top: 12px;
}

.operation > div {
  display: flex;
  cursor: pointer;
  user-select: none;
  position: relative;
  z-index: 99;
  align-items: flex-end;
}

.jumpto {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: 8;
}

.jumpto:hover::before {
  content: "";
  cursor: pointer;
  width: 100%;
  height: 100%;
  border: 5px solid rgba(176, 133, 232, 0.6);
  display: block;
  position: absolute;
  top: 0;
  left: 0;
  border-radius: 25px;
  box-sizing: border-box;
}
</style>

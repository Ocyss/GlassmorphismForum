<template>
  <div v-if="p" class="main">
    <n-divider style="margin: 10px 0" />
    <n-thing>
      <template #avatar>
        <div class="avatar">
          <n-avatar
            round
            :size="45"
            v-if="(postdata.avatar == null) | (postdata.avatar == '')"
            >{{ postdata.name }}
          </n-avatar>
          <n-avatar
            round
            :size="30"
            v-else
            :src="postdata.avatar"
            fallback-src="/files/liekai.png"
            lazy
            :intersection-observer-options="{
              root: '#image-scroll-container',
            }"
          />
        </div>
      </template>
      <template #header> {{ postdata.name }} </template>
      <template #header-extra>
        <n-button strong secondary round type="error"> 关注 </n-button>
      </template>
      <template #description>
        <n-time
          :time="postdata.post_time"
          unix
          type="relative"
          time-zone="Asia/Shanghai"
        />
      </template>
      <div class="content">{{ postdata.content }}</div>
      <template #footer>
        <a :href="postdata.link">{{ postdata.link }}</a>
        <n-image-group>
          <n-space>
            <n-image
              v-for="(src, index) in postdata.imgs"
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
      </template>
      <template #action>
        <div class="operation">
          <div @click="actionClick('zan')">
            <n-icon size="25" color="rgb(90,90,90)">
              <Rose v-if="zans" />
              <RoseOutline v-else /> </n-icon
            >{{ zan }}
          </div>
          <div @click="actionClick('scang')">
            <n-icon size="25" color="rgb(90,90,90)">
              <StarSharp v-if="scangs" />
              <StarOutline v-else /> </n-icon
            >{{ scang }}
          </div>
        </div>
      </template>
    </n-thing>
  </div>
</template>

<script setup>
import { onMounted, ref } from "vue";
import axios from "axios";
import {
  RoseOutline,
  StarOutline,
  Rose,
  StarSharp,
  ArrowUndo,
} from "@vicons/ionicons5";
import { userInfo } from "../../store/userInfo";
import { useMessage } from "naive-ui";
import { useRouter } from "vue-router";
const router = useRouter();
const message = useMessage();
const uinfo = userInfo();
const postdata = ref(null);
const p = ref(false);
const zan = ref(null);
const zans = ref(null);
const props = defineProps(["redata"]);
onMounted(() => {
  axios({
    url: "/api/getPost",
    method: "post",
    data: { postid: props.redata.postid },
  }).then(function (response) {
    if (response.data.code != 200) {
      router.push({
        path: "/error",
        query: { code: response.data.code },
      });
    } else {
      postdata.value = response.data.data;
      zan.value = Object.keys(postdata.value.zan).length;
      zans.value = uinfo.uid in postdata.value.zan;
      p.value = true;
    }
  });
});

function actionClick(type) {
  const operateData = {
    post_userid: postdata.value.userid,
    postid: postdata.value.id,
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
.main {
  padding: 20px;
  width: 100%;
}
.operation {
  display: flex;
  justify-content: space-around;
}
.content {
  font-size: 15px;
}

.operation div {
  display: flex;
  align-items: center;
  cursor: pointer;
  user-select: none;
  font-size: 25px;
}
.return {
  width: 25%;
  display: flex;
  align-items: center;
  color: rgb(78, 29, 76);
  font-size: 20px;
  cursor: pointer;
}
</style>

<template>
  <div class="post">
    <div class="avatar">
      <n-avatar
        round
        :size="30"
        :src="props.pd.Tx"
        lazy
        :intersection-observer-options="{
          root: '#image-scroll-container',
        }"
      />
    </div>
    <div class="main">
      <div class="information">
        <div class="name">{{ props.pd.name }}</div>
        <div class="time">{{ props.pd.time }}</div>
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
          <n-icon size="20">
            <ThumbLike16Regular v-if="zans" />
            <ThumbLike16Filled v-else /> </n-icon
          >{{ zan }}
        </div>
        <div @click="actionClick('cai')">
          <n-icon size="20">
            <ThumbDislike16Regular v-if="cais" />
            <ThumbDislike16Filled v-else /> </n-icon
          >{{ cai }}
        </div>
        <div @click="actionClick('plun')">
          <n-icon size="20">
            <Comment16Regular v-if="pluns" />
            <Comment16Filled v-else /> </n-icon
          >{{ plun }}
        </div>
        <div @click="actionClick('scang')">
          <n-icon size="20">
            <Star16Regular v-if="scangs" />
            <Star16Filled v-else /> </n-icon
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

const props = defineProps(["pd"]);

const zan = ref(Math.ceil(Math.random() * 400));
const cai = ref(Math.ceil(Math.random() * 400));
const plun = ref(Math.ceil(Math.random() * 400));
const scang = ref(Math.ceil(Math.random() * 400));
const zans = ref(true);
const cais = ref(true);
const pluns = ref(true);
const scangs = ref(true);

function actionClick(type) {
  console.log(type);
  switch (type) {
    case "zan":
      zan.value++;
      zans.value = !zans.value;
      break;
    case "cai":
      cai.value++;
      cais.value = !cais.value;
      break;
    case "plun":
      plun.value++;
      pluns.value = !pluns.value;

      break;
    case "scang":
      scang.value++;
      scangs.value = !scangs.value;
      break;
  }
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

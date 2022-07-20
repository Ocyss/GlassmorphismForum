<template>
  <div class="postComment">
    <n-thing>
      <template #avatar>
        <div class="avatar">
          <n-avatar
            round
            :size="45"
            v-if="
              (props.commentData.avatar == null) |
                (props.commentData.avatar == '')
            "
            >{{ props.commentData.name }}
          </n-avatar>
          <n-avatar
            round
            :size="30"
            v-else
            :src="props.commentData.avatar"
            fallback-src="/files/liekai.png"
            lazy
            :intersection-observer-options="{
              root: '#image-scroll-container',
            }"
          />
        </div>
      </template>
      <template #header> {{ props.commentData.name }} </template>
      <div class="content">{{ props.commentData.content }}</div>
      <template #footer>
        <a :href="props.commentData.link">{{ props.commentData.link }}</a>
        <n-image-group>
          <n-space>
            <n-image
              v-for="(src, index) in props.commentData.imgs"
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
        <div class="foot">
          <n-time
            :time="props.commentData.comment_time"
            unix
            type="relative"
            time-zone="Asia/Shanghai"
          />
          <div class="operation">
            <div @click="actionClick('zan')">
              <n-icon size="25" color="rgb(90,90,90)">
                <ThumbLike16Filled v-if="zans" />
                <ThumbLike16Regular v-else /> </n-icon
              >{{ zan }}
            </div>
          </div>
        </div>
      </template>
    </n-thing>
  </div>
</template>

<script setup>
import { ThumbLike16Regular, ThumbLike16Filled } from "@vicons/fluent";
import { ref } from "vue";
import axios from "axios";
import { userInfo } from "../../store/userInfo";
const uinfo = userInfo();
const props = defineProps(["commentData"]);

const zans = ref(uinfo.uid in props.commentData.zan);
const zan = ref(Object.keys(props.commentData.zan).length);
</script>

<style scoped>
.postComment {
  padding: 10px 30px;
  width: 100%;
}

.foot {
  display: flex;
  justify-content: space-between;
  font-size: 12px;
}
</style>

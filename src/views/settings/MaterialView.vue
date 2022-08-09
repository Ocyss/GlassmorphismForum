<template>
  <div class="overallContent">
    <div class="upperpart">
      <n-avatar
        round
        :size="100"
        :src="uinfo.avatar"
        v-if="uinfo.avatar != null"
      />
      <n-avatar round :size="120" v-else>{{ uinfo.name }}</n-avatar>
      <div class="personal">
        <div class="name">
          {{ uinfo.name }}
          <n-icon-wrapper :size="28" :border-radius="10" :color="genderColor">
            <n-icon :size="20" :component="gender()" />
          </n-icon-wrapper>
        </div>
        <div class="briefIntroduction">{{ uinfo.introduce }}</div>
        <div>注册于 {{ howLongAgo() }} 天前</div>
      </div>
      <div class="buttonGroup">
        <n-button class="button" strong secondary type="error">
          更改密码
        </n-button>
        <n-button class="button" strong secondary type="error">
          绑定微信
        </n-button>
        <n-button class="button" strong secondary type="error">
          绑定钉钉
        </n-button>
        <n-button class="button" strong secondary type="error">
          绑定QQ
        </n-button>
        <br />
        <n-button class="button" strong secondary type="error">
          修改资料
        </n-button>
        <n-button class="button" strong secondary type="error">
          我是傻B
        </n-button>
        <n-button class="button" strong secondary type="error">
          点我变管理员
        </n-button>
        <n-button class="button" strong secondary type="error">
          审核文章
        </n-button>
      </div>
    </div>

    <n-card
      style="
        background: rgba(246, 247, 246, 0.8);
        --n-padding-bottom: 0px;
        height: 100%;
      "
    >
      <n-tabs
        default-value="mypost"
        justify-content="space-evenly"
        type="line"
        @update:value="toggletype"
      >
        <n-tab-pane name="mypost" tab="我的帖子">
          未完成！！！！画大饼1
          <n-menu :options="postOptions" />
        </n-tab-pane>
        <n-tab-pane name="myzan" tab="我的点赞">
          <n-menu :options="zanOptions" />
        </n-tab-pane>
        <n-tab-pane name="myscang" tab="我的收藏">
          <n-menu :options="scangOptions" />
        </n-tab-pane>
      </n-tabs>
    </n-card>
  </div>
</template>

<script setup>
import { userInfo } from "../../store/userInfo";
import { Female, Male, MaleFemale } from "@vicons/ionicons5";
import { ref, onMounted } from "vue";
const postOptions = ref([]);
const zanOptions = ref([]);
const scangOptions = ref([]);
const uinfo = userInfo();

function howLongAgo() {
  let T = new Date().valueOf();
  return ((T - uinfo.Registration_time * 1000) / 86400000).toFixed(1);
}

const genderColor = ref("");
function gender() {
  switch (uinfo.gender) {
    case "女":
      genderColor.value = "rgb(254,89,108)";
      return Female;
    case "男":
      genderColor.value = "rgb(35,191,242)";
      return Male;
    case "保密":
      genderColor.value = "rgb(66,200,107)";
      return MaleFemale;
  }
}

function toggletype(value) {
  switch (value) {
    case "myzan":
      break;
    case "myscang":
      break;
  }
}

function getData() {
  return "未完成 ";
}

onMounted(() => {
  getData();
});
</script>

<style scoped>
.overallContent {
  background: rgba(246, 247, 246, 0.65);
  padding: 2%;
  align-items: normal;
  flex-direction: column;
}
.upperpart {
  display: flex;
  align-items: center;
  margin-bottom: 5%;
}
.personal {
  margin-left: 3%;
}
.personal .name {
  font-size: 26px;
  font-weight: 700;
}

.briefIntroduction {
  font-size: 18px;
}

.buttonGroup {
  margin-left: 30%;
}
.buttonGroup .button {
  width: 110px;
  margin: 10px;
  text-align: center;
}
</style>

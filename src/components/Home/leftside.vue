<template>
  <div class="main">
    <n-menu :options="menuOptions" accordion />
  </div>
</template>

<script setup>
import { Home24Filled, Sticker24Filled, Star24Filled } from "@vicons/fluent";
import { ref, onMounted, h } from "vue";
import { NIcon, useMessage } from "naive-ui";
import axios from "axios";
import { RouterLink } from "vue-router";

import { userInfo } from "../../store/userInfo";
const uinfo = userInfo();
const fileList = ref([]);

function renderIcon(icon) {
  return () => h(NIcon, null, { default: () => h(icon) });
}
const menuOptions = [
  {
    label: () =>
      h(
        RouterLink,
        {
          to: {
            name: "home",
            params: {
              lang: "zh-CN",
            },
          },
        },
        { default: () => "主页" }
      ),
    key: "go-back-home",
    icon: renderIcon(Home24Filled),
  },
  {
    label: () =>
      h(
        RouterLink,
        {
          to: {
            name: "selected",
            params: {
              lang: "zh-CN",
            },
          },
        },
        { default: () => "精选" }
      ),
    key: "go-back-selected",
    icon: renderIcon(Sticker24Filled),
  },
  {
    label: () =>
      h(
        RouterLink,
        {
          to: {
            name: "star",
            params: {
              lang: "zh-CN",
            },
          },
        },
        { default: () => "关注" }
      ),
    key: "go-back-srar",
    icon: renderIcon(Star24Filled),
  },
  {
    label: "熊掌",
    key: "bear-paw",
    children: [
      {
        label: "保护野生动物",
        key: "protect-wild-animals",
      },
    ],
  },
  {
    label: "两个都要",
    key: "both",
  },
];
function getpost() {
  axios({
    url: "/api/getMyFile",
    method: "get",
  }).then(function (response) {
    if ((response.data.code = 200)) {
      for (let d in response.data.data) {
        fileList.value.push(response.data.data[d]);
      }
    }
  });
}
onMounted(() => {
  getpost();
});
</script>

<style scoped>
.main {
  overflow-y: scroll;
  scroll-behavior: smooth;
  overscroll-behavior: contain;
  width: 100%;
  display: flex;
  align-items: center;
  flex-direction: column;
}
.navigation {
  margin-top: 15%;
}

.navigation div {
  height: 3rem;
  font-size: 1.1rem;
}

.folder {
  width: 90%;
  font-size: 1.1rem;
}
</style>

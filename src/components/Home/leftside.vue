<template>
  <div class="main">
    <n-menu class="routeNavigation" :options="routeNavigation" />
    <n-menu
      ref="menuInstRef"
      v-model:value="selectedKeyRef"
      class="personalFolder"
      :options="personalFolder"
      accordion
      :icon-size="25"
      @update:value="(key) => $emit('changeTopic', key)"
    />
  </div>
</template>

<script setup>
import { Home, DiamondSharp, Star, FolderOpenOutline } from "@vicons/ionicons5";

import { ref, onMounted, h } from "vue";
import { NIcon, useMessage } from "naive-ui";
import axios from "axios";
import { RouterLink, useRoute } from "vue-router";
import { userInfo } from "../../store/userInfo";
import { Options } from "../../store/options";
const opti = Options();
const selectedKeyRef = ref("");
const route = useRoute();
const uinfo = userInfo();
const fileList = ref([]);
const message = useMessage();
const menuInstRef = ref(null);

function renderIcon(icon, size = 23) {
  return () => h(NIcon, { size: size }, { default: () => h(icon) });
}

const routeNavigation = [
  {
    label: () =>
      h(
        RouterLink,
        {
          to: {
            name: "home",
          },
        },
        { default: () => "主页" }
      ),
    key: "go-back-home",
    icon: renderIcon(Home),
  },
  {
    label: () =>
      h(
        RouterLink,
        {
          to: {
            name: "home",
            query: {
              type: "selected",
            },
          },
        },
        { default: () => "精选" }
      ),
    key: "go-back-selected",
    icon: renderIcon(DiamondSharp),
  },
  {
    label: () =>
      h(
        RouterLink,
        {
          to: {
            name: "home",
            query: {
              type: "star",
            },
          },
        },
        { default: () => "关注" }
      ),
    key: "go-back-srar",
    icon: renderIcon(Star),
  },
];

const personalFolder = ref([]);

function getMyFile() {
  axios({
    url: "/api/getMyFile",
    method: "get",
  }).then(function (response) {
    if (response.data.code == 200) {
      uinfo.myFile = response.data.data;
    }
  });
}

onMounted(() => {
  getMyFile();
  for (let d of uinfo.myFile) {
    let fileList = {
      label: d.name,
      key: d.name,
      icon: renderIcon(FolderOpenOutline, 18),
      children: [],
    };
    for (let l of d.list) {
      fileList.children.push({
        label: () =>
          h(
            RouterLink,
            {
              to: {
                name: "home",
                query: {
                  topic_id: l,
                },
              },
            },
            { default: () => opti.topic_data[l].name }
          ),
        key: l.toString(),
      });
    }
    personalFolder.value.push(fileList);
  }
  if (route.query.hasOwnProperty("topic_id")) {
    selectedKeyRef.value = route.query.topic_id;
    menuInstRef.value?.showOption(route.query.topic_id);
  }
});
</script>

<style scoped>
.main {
  overflow-y: scroll;
  scroll-behavior: smooth;
  overscroll-behavior: contain;
  width: 100%;
  display: flex;
  flex-direction: column;
}

.navigation div {
  height: 3rem;
  font-size: 1.1rem;
}

.routeNavigation {
  font-size: 20px;
}

.personalFolder {
  margin-top: 2rem;
  font-size: 16px;
}
</style>

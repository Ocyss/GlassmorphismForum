<template>
  <div class="main">
    <n-menu class="routeNavigation" :options="routeNavigation" />
    <n-menu
      class="personalFolder"
      :options="personalFolder"
      accordion
      :icon-size="25"
      @update:value="(key) => $emit('changeTopic', key)"
    />
  </div>
</template>

<script setup>
import {
  Home24Filled,
  Sticker24Filled,
  Star24Filled,
  Folder28Regular,
} from "@vicons/fluent";
import { ref, onMounted, h } from "vue";
import { NIcon, useMessage } from "naive-ui";
import axios from "axios";
import { RouterLink } from "vue-router";

import { userInfo } from "../../store/userInfo";

const uinfo = userInfo();
const fileList = ref([]);
function renderIcon(icon, size = 32, color) {
  return () =>
    h(NIcon, { size: size, color: color }, { default: () => h(icon) });
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
    icon: renderIcon(Home24Filled),
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
    icon: renderIcon(Sticker24Filled),
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
    icon: renderIcon(Star24Filled),
  },
];

const personalFolder = ref([]);

function getMyFile() {
  axios({
    url: "/api/getMyFile",
    method: "get",
  }).then(function (response) {
    if ((response.data.code = 200)) {
      for (let d of response.data.data) {
        let fileList = {
          label: d.name,
          key: d.name,
          icon: renderIcon(Folder28Regular, 18),
          children: [],
        };

        for (let l in d.list) {
          fileList.children.push({
            label: () =>
              h(
                RouterLink,
                {
                  to: {
                    name: "home",
                    query: {
                      topic_id: d.list[l],
                    },
                  },
                },
                { default: () => l }
              ),
            key: d.list[l],
          });
        }
        personalFolder.value.push(fileList);
      }
    }
  });
}

onMounted(() => {
  getMyFile();
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

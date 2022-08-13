<template>
  <div id="image-scroll-container">
    <n-transfer
      ref="transfer"
      v-model:value="value"
      :options="Object.values(opti.topic_data).slice(1, 5)"
      :render-target-label="renderTLabel"
      :render-source-label="renderSlabel"
    />
  </div>
</template>

<script setup>
import { Options } from "../../store/options";
import { FolderOpenOutline } from "@vicons/ionicons5";
import { ref, h, computed, onMounted } from "vue";
import { NAvatar, NTabPane } from "naive-ui";
const opti = Options();
const value = ref([]);
// const AllTopic = ref([]);
console.log(Object.values(opti.topic_data).slice(1, 5));

const renderTLabel = function ({ option }) {
  return h(
    "div",
    {
      style: {
        display: "flex",
        margin: "6px 0",
      },
    },
    {
      default: () => [
        h(NAvatar, {
          round: true,
          src: option.logo,
          size: "small",
          fallbackSrc: "/files/liekai.png",
        }),
        h(
          "div",
          {
            style: {
              display: "flex",
              marginLeft: "6px",
              alignSelf: "center",
            },
          },
          { default: () => option.name }
        ),
      ],
    }
  );
};

const renderSlabel = function ({ option }) {
  return h(
    "div",
    {
      style: {
        display: "flex",
        margin: "6px 0",
      },
    },
    {
      default: () => [
        h(NAvatar, {
          round: true,
          src: option.logo,
          size: "small",
          fallbackSrc: "/files/liekai.png",
          lazy: true,
          intersectionObserverOptions: {
            root: "#image-scroll-container",
          },
        }),
        h(
          "div",
          {
            style: {
              display: "flex",
              marginLeft: "6px",
              alignSelf: "center",
            },
          },
          { default: () => option.name }
        ),
      ],
    }
  );
};
</script>

<style scoped></style>

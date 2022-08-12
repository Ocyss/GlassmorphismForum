<template>
  <div class="folderConfigurationBox">
    <n-tabs
      v-model:value="TabsValue"
      type="card"
      :addable="addableRef"
      :closable="closableRef"
      @close="handleClose"
      @add="handleAdd"
      size="small"
    >
      <n-tab-pane v-for="panel in panelsRef" :key="panel" :name="panel">
        <n-transfer
          ref="transfer"
          v-model:value="value"
          :options="options"
          :render-target-label="renderLabel"
        />
      </n-tab-pane>
    </n-tabs>
  </div>
</template>

<script setup>
import { FolderOpenOutline } from "@vicons/ionicons5";
import { ref, h, computed } from "vue";
import { NAvatar } from "naive-ui";
import { Options } from "../../store/options";

const value = ref([]);
const TabsValue = ref(1);
const panelsRef = ref([1, 2, 3, 4, 5]);
const opti = Options();
const addableRef = computed(() => {
  return {
    disabled: panelsRef.value.length >= 10,
  };
});
const closableRef = computed(() => {
  return panelsRef.value.length > 1;
});

const options = ref();

// for (let topic in opti.topic_data[(1, 10)]) {
//   options.value.push({
//     label: opti.topic_data[topic].name,
//     value: opti.topic_data[topic].logo,
//   });
// }

function handleAdd() {
  const newValue = Math.max(...panelsRef.value) + 1;
  panelsRef.value.push(newValue);
  TabsValue.value = newValue;
}

function handleClose(name) {
  const panels = panelsRef.value;
  const nameIndex = panels.findIndex((panelName) => panelName === name);
  if (!~nameIndex) return;
  panels.splice(nameIndex, 1);
  if (name === TabsValue.value) {
    TabsValue.value = panels[Math.min(nameIndex, panels.length - 1)];
  }
}

const renderLabel = function ({ option }) {
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
          src: option.value,
          size: "small",
          fallbackSrc:
            "https://07akioni.oss-cn-beijing.aliyuncs.com/07akioni.jpeg",
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
          { default: () => option.label }
        ),
      ],
    }
  );
};
</script>

<style scoped>
.folderConfigurationBox {
  width: 55vw;
  height: 70vh;
  min-width: 400px;
  min-height: 350px;
  background: rgba(255, 255, 255, 0.55);
  backdrop-filter: blur(5px);
  -webkit-backdrop-filter: blur(20px);
  border-radius: 10px;
  padding: 30px;
}

.folder {
  background: rgba(150, 230, 150, 0.2);
  min-height: 100px;
  margin: auto;
  padding: 10px;
  box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
  border-radius: 8px;
}

.folderName {
  font-size: 20px;
  display: flex;
  align-items: center;
}
</style>

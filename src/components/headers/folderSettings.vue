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
        <transfer />
      </n-tab-pane>
    </n-tabs>
  </div>
</template>

<script setup>
import { FolderOpenOutline } from "@vicons/ionicons5";
import { ref, h, computed } from "vue";
import { Options } from "../../store/options";
import transfer from "./transfer.vue";

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

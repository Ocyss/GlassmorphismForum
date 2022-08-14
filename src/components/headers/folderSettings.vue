<template>
  <div class="folderConfigurationBox">
    <n-tabs
      v-model:value="TabsValue"
      type="card"
      :addable="addableRef"
      :closable="true"
      @close="handleClose"
      @add="handleAdd"
      size="small"
      @update:value="tabsUpdata"
    >
      <n-tab-pane
        v-for="(panel, index) in panelsRef"
        :key="index"
        :name="index"
      >
        <n-input
          type="text"
          :allow-input="noSideSpace"
          maxlength="10"
          show-count
          clearable
          v-model:value="inputText"
          @blur="updateFileName"
        />
        <div id="image-scroll-container">
          <n-transfer
            ref="transfer"
            v-model:value="transFerValue"
            :options="transFerOptions"
            :render-target-label="renderTLabel"
            filterable
          />
        </div>
        <template #tab
          ><n-icon :size="20"><FolderOpenOutline /></n-icon
          >{{ panel.name }}</template
        >
      </n-tab-pane>
    </n-tabs>
    <n-button type="success" class="buttonSave"> 保存 </n-button>
    <n-button type="error" style="margin-left: 5%" @click="$emit('cloneModal')">
      取消
    </n-button>
  </div>
</template>

<script setup>
import { FolderOpenOutline } from "@vicons/ionicons5";
import { ref, h, computed, onMounted } from "vue";
import { Options } from "../../store/options";
import axios from "axios";
import { NAvatar, NTabPane } from "naive-ui";

const TabsValue = ref(); //当前标签下标
const panelsRef = ref([]); //标签内容
const opti = Options(); //通用pinia
const newTabnum = ref(1); //新标签名
const addableRef = computed(() => {
  return {
    disabled: panelsRef.value.length >= 10,
  };
}); //标签添加上限
const inputText = ref(""); //标签名文本框内容
const noSideSpace = (value) => !value.startsWith(" ") && !value.endsWith(" "); //标签名文本框禁止前后空格

const transFerValue = ref([]); //穿梭框选择的值
const transFerOptions = ref([]); //穿梭框内容

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
          src: option.value,
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
          { default: () => option.label }
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
          src: option.value,
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
          { default: () => option.label }
        ),
      ],
    }
  );
};

function handleAdd() {
  const newValue = { name: `新文件夹${newTabnum.value}`, list: [] };
  panelsRef.value.push(newValue);
  TabsValue.value = newValue.name;
  inputText.value = newValue.name;
  newTabnum.value++;
}

function handleClose(name) {
  for (let i in panelsRef.value) {
    if (panelsRef.value[i].name == name) {
      panelsRef.value.splice(i, 1);
      break;
    }
  }
}

function updateFileName() {
  let current = panelsRef.value[TabsValue.value];
  if (inputText.value != current.name) {
    //当文本内容和标签页名字不一样再改名
    panelsRef.value[TabsValue.value].name = inputText.value;
  }
}

function tabsUpdata() {
  let current = panelsRef.value[TabsValue.value];
  inputText.value = current.name;
  transFerValue.value = [];
  // for (let i of current.list) {
  //   transFerValue.value.push({
  //     id: i,
  //     disabled: false,
  //     label: opti.topic_data[i].name,
  //     value: opti.topic_data[i].logo,
  //   });
  // }
}

function getMyFile() {
  axios({
    url: "/api/getMyFile",
    method: "get",
  }).then(function (response) {
    if (response.data.code == 200) {
      if (response.data.data.length > 1) {
        panelsRef.value = panelsRef.value.concat(response.data.data);
        TabsValue.value = 0;
        tabsUpdata();
      }
    }
  });
}

onMounted(() => {
  getMyFile();
  let netTransFerValue = [];
  for (let i in opti.topic_data) {
    netTransFerValue.push({
      id: i,
      disabled: false,
      label: opti.topic_data[i].name,
      value: opti.topic_data[i].logo,
    });
  }
  console.log(netTransFerValue);
  transFerOptions.value = netTransFerValue;
});
</script>

<style scoped>
.folderConfigurationBox {
  width: 55vw;
  min-width: 400px;
  background: rgba(255, 255, 255, 0.55);
  backdrop-filter: blur(5px);
  -webkit-backdrop-filter: blur(20px);
  border-radius: 10px;
  padding: 20px;
  position: relative;
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

.buttonSave {
  margin-top: 20px;
}
</style>

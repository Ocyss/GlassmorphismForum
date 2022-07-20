<template>
  <n-drawer
    v-model:show="opit.writepost"
    :default-width="502"
    placement="left"
    resizable
    display-directive="show"
  >
    <n-drawer-content
      title="发布帖子"
      body-style="--n-body-padding:2px 12px 12px 12px;"
    >
      <div class="menu">
        <n-popselect v-model:value="value" :options="options" trigger="click">
          <n-button>{{ value || "选择帖子类型" }}</n-button>
        </n-popselect>
        <n-input type="text" placeholder="标题(可不写)" v-model:value="title" />
      </div>
      <div class="allEd">
        <div class="edPureGraph" v-if="value == '纯文图'">
          <PureGraph :title="title" />
        </div>
        <div class="edImageText" v-else-if="value == '图文'">
          <ImageText :title="title" />
        </div>
        <div class="edRichText" v-else-if="value == '富文本'">
          <RichText :title="title" />
        </div>
      </div>
    </n-drawer-content>
  </n-drawer>
</template>

<script setup>
import PureGraph from "../editor/PureGraph.vue";
import ImageText from "../editor/ImageText.vue";
import RichText from "../editor/RichText.vue";
import { ref } from "vue";
import { Options } from "../../store/options";
const opit = Options();
const value = ref("纯文图");

const title = ref("");
const options = ref([
  {
    label: "纯文图",
    value: "纯文图", //pureGraph
  },
  {
    label: "图文",
    value: "图文", //imageText
  },
  {
    label: "富文本",
    value: "富文本", //richText
  },
]);
</script>

<style scoped>
.menu {
  display: flex;
  justify-content: center;
  align-items: center;
}
.allEd {
  height: 80%;
  margin-top: 10px;
}
</style>

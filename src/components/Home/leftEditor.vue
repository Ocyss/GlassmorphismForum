<template>
  <button @click="active = !active"><h1>别点我</h1></button>
  <n-drawer
    v-model:show="active"
    :default-width="502"
    placement="left"
    resizable
    :show-mask="false"
  >
    <n-drawer-content
      title="发布帖子"
      body-style="--n-body-padding:2px 12px 12px 12px;"
    >
      <div class="menu">
        <n-popselect v-model:value="value" :options="options" trigger="click">
          <n-button>{{ value || "选择帖子类型" }}</n-button>
        </n-popselect>
        <n-input type="text" placeholder="标题(可不写)" />
      </div>
      <div class="allEd">
        <div class="edPureGraph" v-if="value == '纯文图'">
          <n-input
            type="textarea"
            maxlength="500"
            show-count
            clearable
            round
            rows="20"
          />
        </div>

        <div class="edImageText" v-else-if="value == '图文'"><h1>图文</h1></div>
        <div class="edRichText" v-else-if="value == '富文本'"><editor /></div>
      </div>
      <n-button strong secondary size="large" type="success" class="sendbutton">
        发 射! 射! 射!
      </n-button>
    </n-drawer-content>
  </n-drawer>
</template>

<script setup>
import editor from "../editor.vue";
import { ref } from "vue";
const value = ref("");
const active = ref(true);
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

.sendbutton {
  margin-left: 70%;
}
</style>

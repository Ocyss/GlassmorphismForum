<template>
  <div class="rightside">
    <div class="digital">
      数码热榜
      <ol>
        <li v-for="(item, index) in digitalList" :key="index">
          <span
            ><n-ellipsis style="max-width: 100px">{{
              item.name
            }}</n-ellipsis></span
          ><span class="qu">{{ item.quantity }}</span>
        </li>
      </ol>
    </div>
    <div class="label">
      话题热榜
      <ol>
        <li v-for="(item, index) in labellList" :key="index">
          <span
            ><n-ellipsis style="max-width: 100px">{{
              item.name
            }}</n-ellipsis></span
          ><span class="qu">{{ item.quantity }}</span>
        </li>
      </ol>
    </div>
  </div>
</template>
<script setup>
import { ref } from "vue";
const digitalList = ref([
  { name: "小米12S Ultra", quantity: "49.8w" },
  { name: "Redmi K40", quantity: "45.8w" },
  { name: "Redmi K50", quantity: "43.5w" },
  { name: "Redmi K60", quantity: "41.6w" },
  { name: "Redmi K70", quantity: "39.7w" },
  { name: "Redmi K80", quantity: "37.8w" },
  { name: "小米11S Ultra", quantity: "32.2w" },
  { name: "小米10S", quantity: "30.1w" },
  { name: "小米13S Ultra", quantity: "28.5w" },
  { name: "小米12S", quantity: "25.3w" },
]);

const labellList = ref([
  { name: "薅羊毛", quantity: "99.8w" },
  { name: "魅族售后", quantity: "95.8w" },
  { name: "耍猴米", quantity: "93.5w" },
  { name: "爱国为", quantity: "91.6w" },
  { name: "黑苹果", quantity: "89.7w" },
  { name: "三星爆炸", quantity: "87.8w" },
  { name: "格力手机", quantity: "82.2w" },
  { name: "实力单身", quantity: "80.1w" },
  { name: "吾辈楷模", quantity: "78.5w" },
  { name: "脱胶电视", quantity: "25.3w" },
]);
</script>

<style scoped>
div {
  padding: 10px;
  font-size: 1.2rem;
}
li {
  font-size: 0.8rem;
  width: 100%;
  padding: 7px 10px;
  list-style-position: inside;
}

li .qu {
  position: absolute;
  right: 15px;
}

.rightside {
  height: 100%;
}
</style>

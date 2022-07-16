<template>
  <div class="content" id="image-scroll-container">
    <content v-for="item in PostData" :key="item.id" :pd="item" />
    <n-pagination
      v-model:page="opti.page"
      :page-count="parseInt(opti.pagetotal / 10) + 1"
      :page-slot="8"
      @update:page="getpost(opti.page)"
    />
  </div>
</template>

<script setup>
import axios from "axios";
import { useMessage } from "naive-ui";
import content from "./content.vue";
import { ref, onMounted } from "vue";
import { Options } from "../../store/options";
const opti = Options();
const message = useMessage();
const PostData = ref([]);

function getpost(page) {
  var data = axios({
    url: "/api/getPostList",
    method: "post",
    data: { limit: page },
  }).then(function (response) {
    if (response.data.code != 200) {
      message.error(response.data.msg);
    } else {
      opti.pagetotal = response.data.total;
      PostData.value = [];
      for (let d in response.data.data) {
        PostData.value.push(response.data.data[d]);
      }
    }
  });
}
onMounted(() => {
  getpost(opti.page);
});
</script>

<style scoped>
.content {
  background: rgba(246, 247, 246, 0.4);
  height: 100%;
  overflow-y: scroll;
  scroll-behavior: smooth;
  overscroll-behavior: contain;
  display: flex;
  flex-direction: column;
  align-items: center;
}
.n-pagination {
  margin-bottom: 10px;
}
</style>

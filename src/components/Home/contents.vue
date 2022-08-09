<template>
  <div class="content" id="image-scroll-container">
    <n-button
      color="rgba(138,43,226,0.7)"
      circle
      class="writepost"
      @click="opti.writepost = true"
    >
      <template #icon>
        <n-icon>
          <Compose16Regular />
        </n-icon>
      </template>
    </n-button>
    <content
      v-for="item in PostData"
      :key="item.id"
      :pd="item"
      @getComment="(pid, plun) => $emit('getComment', pid, plun)"
    />
    <n-pagination
      v-model:page="opti.page"
      :page-count="parseInt(opti.pagetotal / 10)"
      :page-slot="8"
      @update:page="getpost(opti.page, 'ordinary')"
    />
  </div>
</template>

<script setup>
import { Compose16Regular } from "@vicons/fluent";
import axios from "axios";
import { useMessage } from "naive-ui";
import content from "./content.vue";
import { ref, onMounted, defineExpose } from "vue";
import { Options } from "../../store/options";
const opti = Options();
const message = useMessage();
const PostData = ref([]);

function getpost(page, type, json) {
  let data = { limit: page };
  if (type == "topic") {
    data["type"] = "topic";
    data["topic_id"] = json["topic_id"];
  }
  axios({
    url: "/api/getPostList",
    method: "post",
    data: data,
  }).then(function (response) {
    if (response.data.code != 200) {
      message.error(response.data.msg);
    } else {
      opti.pagetotal = response.data.total;
      opti.topic_data = response.data.topic;
      PostData.value = [];
      for (let d in response.data.data) {
        PostData.value.push(response.data.data[d]);
      }
    }
  });
}
onMounted(() => {
  getpost(opti.page, "ordinary");
});

defineExpose({
  getpost,
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

.writepost {
  margin: 10px 10px 5px 85%;
}
</style>

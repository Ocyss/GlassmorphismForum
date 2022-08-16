<template>
  <div class="topicDetails">
    <n-thing content-indented>
      <template #avatar>
        <n-avatar round :size="50" :src="topic.logo" />
      </template>
      <template #header> {{ topic.name }} </template>
      <template #header-extra>
        <n-button strong round v-if="topic_follow" @click="cancelAttention">
          已关注
        </n-button>
        <n-button strong round v-else type="success"> 关注 </n-button>
      </template>

      <template #footer>
        <div class="footer">
          <div>热度: {{ topic.attention }}</div>
          <div>帖子: {{ topic.post_num }}</div>
        </div>
      </template>
    </n-thing>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { Options } from "../../store/options";
import { userInfo } from "../../store/userInfo";
import axios from "axios";
const opti = Options();
const uinfo = userInfo();
const props = defineProps(["topic_id"]);
const topic_id = props.topic_id;
const topic = ref(opti.topic_data[topic_id]);
const topic_follow = ref(false); //是否关注

function UpTopic() {
  axios.post("/api/UpTopic", { data: uinfo.myFile }).then((res) => {
    if (res.data.code == 200) {
      return true;
    } else {
      return false;
    }
  });
}

function cancelAttention() {
  for (let i in uinfo.myFile) {
    for (let j in uinfo.myFile[i].list) {
      if (topic_id == uinfo.myFile[i].list[j]) {
        uinfo.myFile[i].list.splice(j, 1);
        if (UpTopic()) {
          topic_follow.value = false;
        }
      }
    }
  }
}

onMounted(() => {
  for (let d of uinfo.myFile) {
    for (let l of d.list) {
      if (topic_id == l) {
        topic_follow.value = true;
        break;
      }
    }
  }
});
</script>

<style scoped>
.topicDetails {
  width: 95%;
  margin: 1.5% 2.5%;
  font-size: 0.8rem;
  background: rgba(255, 255, 255, 0.6);
  border-radius: 25px;
  padding: 15px;
}

.footer {
  display: flex;
  justify-content: space-around;
  align-items: center;
}
</style>

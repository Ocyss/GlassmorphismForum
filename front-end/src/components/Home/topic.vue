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
        <n-popselect
          v-else
          v-model:value="popselectValue"
          :options="popselectOptions"
          size="medium"
          scrollable
          @update:value="attention"
        >
          <n-button strong round type="success"> 关注 </n-button>
          <template #action
            ><n-input-group>
              <n-input v-model:value="newInput" :allow-input="noSpace" />
              <n-button type="primary" ghost @click="newFile"> + </n-button>
            </n-input-group>
          </template>
        </n-popselect>
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
const popselectValue = ref(null);
const popselectOptions = ref([]);
const newInput = ref("");
const noSpace = (value) => !value || /[^\u4E00-\u9FA5]/g.test(value);

async function upMyFile(type, FileName, tid = -1) {
  let res;
  await axios
    .post("/api/upMyFile", {
      type: type,
      FileName: FileName,
      topic_id: tid,
    })
    .then((response) => {
      res = response;
    });

  if (res.data.code == 200) {
    return true;
  } else {
    return false;
  }
}

function cancelAttention() {
  for (let FileName in uinfo.myFile) {
    for (let i in uinfo.myFile[FileName]) {
      if (uinfo.myFile[FileName][i] == topic_id) {
        if (upMyFile("remove", FileName, i)) {
          topic_follow.value = false;
          uinfo.myFile[FileName].splice(i, 1);
          break;
        }
      }
    }
  }
}

function attention(value) {
  if (upMyFile("add", value, topic_id)) {
    topic_follow.value = true;
  }
}

function newFile() {
  if (newInput.value != "") {
    if (upMyFile("newFile", newInput.value)) {
      popselectOptions.value.push({
        label: newInput.value,
        value: newInput.value,
      });
      newInput.value = "";
    }
  }
}

onMounted(() => {
  for (let FileName in uinfo.myFile) {
    popselectOptions.value.push({ label: FileName, value: FileName });
    for (let l of uinfo.myFile[FileName]) {
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

<template>
  <div class="main">
    <div>
      <n-input
        type="textarea"
        maxlength="500"
        show-count
        clearable
        round
        rows="20"
        v-model:value="content"
      />
    </div>

    <div>
      <n-upload
        ref="upload"
        action="/api/upload"
        list-type="image-card"
        :max="8"
        multiple
        :default-upload="false"
        with-credentials
        :data="{ type: 'PureGraph' }"
        :custom-request="customRequest"
        @finish="uploadComplete"
        v-model:file-list="fileList"
      />
    </div>
    <div>
      <n-button
        strong
        secondary
        size="large"
        type="success"
        class="sendbutton"
        @click="send"
      >
        发 射! 射! 射!
      </n-button>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { lyla } from "lyla"; //https://github.com/07akioni/lyla
import { useMessage } from "naive-ui";
import axios from "axios";
import { Options } from "../../store/options";
const opit = Options();
const props = defineProps(["title"]);
const fileList = ref([]);
const message = useMessage();
const upload = ref(null);
const imgs = ref([]);
const content = ref("");

function send() {
  upload.value.submit();
  uploadComplete(0);
}

function uploadComplete(file) {
  if (imgs.value.length == fileList.value.length) {
    const data = ref({
      title: props.title,
      type: "PureGraph",
      content: content.value,
      link: "",
      imgs: imgs.value,
    });

    axios({
      url: "/api/sendPost",
      method: "post",
      data: data.value,
    }).then(function (response) {
      if (response.data.code != 200) {
        message.error(response.data.msg);
      } else {
        opit.writepost = false;
        message.success(response.data.msg);
      }
    });
  }
}

const customRequest = ({
  file,
  data,
  headers,
  withCredentials,
  action,
  onError,
  onFinish,
  onProgress,
}) => {
  const formData = new FormData();
  if (data) {
    Object.keys(data).forEach((key) => {
      formData.append(key, data[key]);
    });
  }
  formData.append("file", file.file);
  lyla
    .post(action, {
      withCredentials,
      headers,
      body: formData,
      onUploadProgress: ({ percent }) => {
        onProgress({ percent: Math.ceil(percent) });
      },
    })
    .then(({ json }) => {
      if (json.code == 200) {
        imgs.value.push(json.url);
        onFinish();
      } else {
        message.error(json.msg);
      }
    })
    .catch((error) => {
      message.success(error.message);
      onError();
    });
  return {
    customRequest,
  };
};
</script>

<style scoped>
div {
  margin-top: 10px;
}
.sendbutton {
  margin-left: 70%;
}
</style>

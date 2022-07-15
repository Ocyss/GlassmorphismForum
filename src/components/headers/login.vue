<template>
  <div class="lore">
    <n-button
      round
      @click="showModal = true"
      text-color="#f72585"
      strong
      size="large"
      color="rgba(86,11,173,0.2)"
    >
      > 登陆&注册 &lt;
    </n-button>
    <n-modal v-model:show="showModal" class="loginmodal">
      <div class="loginBox">
        <n-tabs size="large" justify-content="space-evenly">
          <n-tab-pane name="signin" tab="登录">
            <n-collapse-transition :show="true">
              <h3 style="color: #ff0000">{{ loginlog }}</h3>
            </n-collapse-transition>
            <n-form
              ref="loginformRef"
              :model="loginformValue"
              label-placement="left"
              class="loginform"
            >
              <n-form-item label="账号" path="user">
                <n-input
                  v-model:value="loginformValue.user"
                  placeholder="输入账号"
                  :maxlength="16"
                  round
                />
              </n-form-item>
              <n-form-item label="密码" path="pswd">
                <n-input
                  v-model:value="loginformValue.pswd"
                  placeholder="输入密码"
                  type="password"
                  show-password-on="click"
                  :maxlength="16"
                  round
                />
              </n-form-item>
              <n-form-item size="large">
                <n-button
                  attr-type="button"
                  strong
                  secondary
                  round
                  @click="login"
                  type="warning"
                  style="width: 100%"
                >
                  登陆
                </n-button>
              </n-form-item>
            </n-form>
          </n-tab-pane>
          <n-tab-pane name="signup" tab="注册">
            <n-collapse-transition :show="true">
              <h3 style="color: #ff0000">{{ registerlog }}</h3>
            </n-collapse-transition>
            <n-form
              ref="formRef"
              :model="registerformValue"
              label-placement="left"
              class="registerform"
            >
              <n-form-item label="账号" path="user">
                <n-input
                  v-model:value="registerformValue.user"
                  placeholder="输入账号"
                  :maxlength="16"
                  round
                  @blur="userrepeat"
                />
              </n-form-item>
              <n-form-item label="密码" path="pswd">
                <n-input
                  v-model:value="registerformValue.pswd"
                  placeholder="输入密码"
                  type="password"
                  show-password-on="click"
                  :maxlength="16"
                  round
                />
              </n-form-item>
              <n-form-item label="重复" path="pswd2">
                <n-input
                  v-model:value="registerformValue.pswd2"
                  placeholder="再次输入密码"
                  type="password"
                  show-password-on="click"
                  :maxlength="16"
                  round
                  @blur="verify"
                />
              </n-form-item>
              <n-form-item size="large">
                <n-button
                  attr-type="button"
                  strong
                  secondary
                  round
                  @click="register"
                  type="warning"
                  style="width: 100%"
                >
                  注册
                </n-button>
              </n-form-item>
            </n-form>
          </n-tab-pane>
        </n-tabs>
      </div>
    </n-modal>
  </div>
</template>

<script setup>
import axios from "axios";
import { ref } from "vue";

import { useMessage } from "naive-ui";
import { userInfo } from "../../store/userInfo";
const uinfo = userInfo();
window.$message = useMessage();
const emit = defineEmits(["setislo"]);
let showModal = ref(false);
let loginformRef = ref(null);
let loginlog = ref(null);
let loginformValue = ref({
  user: "admin",
  pswd: "admin",
});

let registerformRef = ref(null);
let registerlog = ref(null);
let registerformValue = ref({
  user: "",
  pswd: "",
  pswd2: "",
});

function login() {
  var data = axios({
    url: "/api/login",
    method: "post",
    data: loginformValue.value,
  }).then(function (response) {
    if (response.data.code != 200) {
      loginlog.value = response.data.msg;
    } else {
      showModal.value = false;
      window.$message.success(`登陆成功！欢迎回来 ${response.data.data.name}`);
      $cookies.config("1m"); //一个月
      // 设置cookies
      $cookies.set("islo", true);
      $cookies.set("token", response.data.token);
      $cookies.set("userid", response.data.data.id);
      console.log(response.data.data);
      uinfo.setUser(response.data.data);
      emit("setislo");
    }
  });
}

function register() {
  if (verify() == true) {
    var data = axios({
      url: "/api/register",
      method: "post",
      data: registerformValue.value,
    }).then(function (response) {
      if (response.data.code != 200) {
        registerlog.value = response.data.msg;
      } else {
        window.$message.success(`注册成功！ ${registerformValue.value.user}`);
      }
    });
  }
}

function verify() {
  if (registerformValue.value.pswd != registerformValue.value.pswd2) {
    registerlog.value = "两次密码输入不一致";
    return false;
  } else {
    registerlog.value = response.data.data.name;
    return true;
  }
}

function userrepeat() {
  var data = axios({
    url: "/api/judge",
    method: "get",
    params: { type: "user", data: registerformValue.value.user },
  }).then(function (response) {
    if (response.data.code != 200) {
      registerlog.value = response.data.msg;
    } else {
      registerlog.value = response.data.data.name;
    }
  });
}
</script>

<style scoped>
.loginBox {
  width: 35vw;
  height: 40vh;
  min-width: 400px;
  min-height: 350px;
  background: rgba(255, 255, 255, 0.7);
  box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  border-radius: 10px;
  border: 1px solid rgba(255, 255, 255, 0.08);
  text-align: center;
}

.loginform,
.registerform {
  width: 60%;
  margin: 6% auto;
  text-align: left;
}
</style>

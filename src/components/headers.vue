<template>
  <div class="header">
    <div class="logo">
      <img src="../assets/logo.png" alt="LOGO" />
    </div>
    <div class="searchBox">
      <n-input :style="{ width: '80%' }" />
      <n-button type="primary" ghost> 搜索 </n-button>
    </div>
    <div class="navigation">
      <n-icon v-if="theme == null" size="28" @click="theme = darkTheme">
        <WeatherMoon28Filled />
      </n-icon>
      <n-icon v-else-if="theme == darkTheme" size="28" @click="theme = null">
        <WeatherSunny32Filled />
      </n-icon>

      <n-icon size="28">
        <People16Filled />
      </n-icon>

      <n-icon size="28">
        <MailMultiple16Filled />
      </n-icon>

      <div class="personal" v-if="internalData.$cookies.get('islo') != null">
        <n-avatar round :size="30" :src="uinfo.avatar" />

        <div class="name">{{ uinfo.name }}</div>
        <h1>&nbsp&nbsp&nbsp&nbsp</h1>
        <n-button @click="sign" type="error" size="tiny"> 退出登陆 </n-button>
      </div>

      <div class="lore" v-else>
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

        <n-modal v-model:show="showModal">
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
    </div>
  </div>
</template>

<script setup>
import {
  MailMultiple16Filled,
  People16Filled,
  WeatherSunny32Filled,
  WeatherMoon28Filled,
} from "@vicons/fluent";
import axios from "axios";
import { ref } from "vue";
import { useMessage } from "naive-ui";
import { getCurrentInstance } from "vue";
import userInfo from "../store/userInfo";

window.$message = useMessage();
const internalInstance = getCurrentInstance();
const internalData = internalInstance.appContext.config.globalProperties;
const uinfo = userInfo();
let theme = ref(null);
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
  let logindata = new FormData();
  logindata.append("user", loginformValue.value.user);
  logindata.append("pswd", loginformValue.value.pswd);
  var data = axios({
    url: "/api/login",
    method: "post",
    data: logindata,
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
    }
  });
}

function register() {
  if (verify() == true) {
    let registerdata = new FormData();
    registerdata.append("user", registerformValue.value.user);
    registerdata.append("pswd", registerformValue.value.pswd);
    var data = axios({
      url: "/api/register",
      method: "post",
      data: registerdata,
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

function sign() {
  // window.$message.success(`再见~~ ${response.data.data.name}`);
  $cookies.config("0"); //一个月
  // 设置cookies
  if ($cookies.isKey("islo")) {
    $cookies.remove("islo");
  }
  location.reload();
}
</script>

<style scoped>
.header {
  display: flex;
  width: 100%;
  justify-content: space-evenly;
  align-items: center;
  position: fixed;
  top: 0;
  left: 0;
  z-index: 9999;
  height: 3.125rem;
  background: rgba(255, 255, 255, 0.6);
  backdrop-filter: blur(40px);
}

.searchBox {
  width: 280px;
}

.logo img {
  width: 50px;
  height: 50px;
}

.navigation {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.navigation i {
  margin-right: 25px;
}

.loginBox {
  width: 35vw;
  height: 40vh;
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

.personal {
  display: flex;
  justify-content: center;
  align-items: center;
}

.personal .name {
  font-size: 1.2rem;
}
</style>

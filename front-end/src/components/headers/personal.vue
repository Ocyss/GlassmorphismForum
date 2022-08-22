<template>
  <n-dropdown :options="options" @select="handleSelect">
    <div class="personal">
      <n-avatar
        round
        :size="30"
        :src="uinfo.avatar"
        v-if="uinfo.avatar != null"
      />
      <n-avatar round :size="30" v-else>{{ uinfo.name }}</n-avatar>
      <div class="name">{{ uinfo.name }}</div>
    </div>
  </n-dropdown>
</template>

<script setup>
import { userInfo } from "../../store/userInfo";

import {
  PersonCircleOutline as UserIcon,
  Settings as SettingsIcon,
  LogOutOutline as LogoutIcon,
} from "@vicons/ionicons5";
import { h, ref } from "vue";
import { NIcon } from "naive-ui";
import { useRouter } from "vue-router";
const Foldershow = ref(false);
const router = useRouter();
const uinfo = userInfo();
const emit = defineEmits(["logout"]);
function handleSelect(key) {
  switch (key) {
    case "logout":
      emit("logout");
      break;
    case "profile":
      let routeUrl = router.resolve({
        path: "/settings/material",
      });
      window.open(routeUrl.href, "_blank");
      break;
  }
}
const renderIcon = (icon) => {
  return () => {
    return h(NIcon, null, {
      default: () => h(icon),
    });
  };
};
const options = ref([
  {
    label: "用户资料",
    key: "profile",
    icon: renderIcon(UserIcon),
  },
  {
    label: "退出登录",
    key: "logout",
    icon: renderIcon(LogoutIcon),
  },
]);
</script>

<style scoped>
.personal {
  display: flex;
  justify-content: center;
  align-items: center;
  user-select: none;
}
.personal .name {
  font-size: 1.2rem;
}
</style>

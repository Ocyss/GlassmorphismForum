<template>
  <div class="overallContent">
    <div class="homebutton" @click="router.push('/')">
      <n-button strong secondary type="primary"> 点我回家 </n-button>
    </div>
    <c404 v-if="code == 404" />
  </div>
</template>

<script setup>
import { useRoute } from "vue-router";
import { ref } from "vue";
import c404 from "../components/error/c404.vue";
import { useRouter } from "vue-router";
const router = useRouter();
const $route = useRoute();
const code = ref($route.query.code);
</script>

<style scoped>
.homebutton {
  position: absolute;
  left: 0;
  top: 0;
}
</style>

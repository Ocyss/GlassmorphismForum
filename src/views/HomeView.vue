<template>
  <div class="Home">
    <div class="leftside" :style="opti.leftwi">
      <leftside />
      <div class="putAway" @click="opti.putAway" :style="opti.putAwayrig">
        <n-icon size="28" color="#FFF" class="icon"
          ><ChevronCircleLeft20Regular
            v-if="opti.letstate"
          /><ChevronCircleRight20Regular v-else />
        </n-icon>
      </div>
    </div>
    <contents :style="opti.contentwi" />
    <div class="rightside" :style="opti.rightwi">
      <rightside v-if="opti.rightContent == '热榜'" />
      <comment
        :postid="opti.postid"
        v-else-if="opti.rightContent == '评论'"
        :key="opti.postid"
      />
      <div
        class="putAway"
        v-if="opti.rightContent != '热榜'"
        style="left: -15px"
        @click="opti.rightContent = '热榜'"
      >
        <n-icon size="28" color="#FFF" class="icon"
          ><ArrowHookUpLeft24Regular />
        </n-icon>
      </div>
    </div>
  </div>
</template>

<script setup>
import {
  ChevronCircleLeft20Regular,
  ChevronCircleRight20Regular,
  ArrowHookUpLeft24Regular,
} from "@vicons/fluent";
import leftside from "../components/Home/leftside.vue";
import rightside from "../components/Home/rightside.vue";
import comment from "../components/Home/comment.vue";
import contents from "../components/Home/contents.vue";
import { Options } from "../store/options";
const opti = Options();
opti.rightContent = "热榜";
</script>

<style scoped>
.Home {
  position: absolute;
  top: 4.5rem;
  left: 12vw;
  width: 76vw;
  min-width: 750px;
  height: 88vh;
  display: flex;
  justify-content: center;
  align-items: center;
  box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
  backdrop-filter: blur(2px);
  -webkit-backdrop-filter: blur(2px);
  border-radius: 10px;
  border: 1px solid rgba(255, 255, 255, 0.18);
  overflow: hidden;
}

.leftside {
  background-color: rgba(246, 247, 246, 0.65);
  height: 100%;
  position: relative;
  display: flex;
}

.rightside {
  background: rgba(246, 247, 246, 0.15);
  height: 100%;
  position: relative;
  display: flex;
  flex-direction: column;
}

::-webkit-scrollbar {
  width: 5px;
}

::-webkit-scrollbar-thumb {
  background: rgb(255, 76, 162);
}

.putAway {
  transition: color 0.3s var(--n-bezier), right 0.3s var(--n-bezier),
    left 0.3s var(--n-bezier), border-color 0.3s var(--n-bezier),
    background-color 0.3s var(--n-bezier);
  cursor: pointer;
  position: absolute;
  transform: translateX(50%) translateY(-50%);
  z-index: 1;
  top: 2%;
}
</style>

<template>
  <div class="overallContent">
    <div class="leftside" :style="opti.leftwi">
      <leftside @changeTopic="changeTopic" />
      <div class="putAway" @click="opti.putAway" :style="opti.putAwayrig">
        <n-icon size="28" color="#FFF" class="icon"
          ><ChevronBackCircleOutline
            v-if="opti.letstate"
          /><ChevronForwardCircleOutline v-else />
        </n-icon>
      </div>
    </div>
    <contents
      :style="opti.contentwi"
      @getComment="getComment"
      ref="contentsRef"
    />
    <div class="rightside" :style="opti.rightwi">
      <div class="drag" @mousedown="drag"></div>
      <rightside v-if="rightContent === '热榜'" />
      <comments
        :postid="postid"
        :plun_num="plun_num"
        v-else-if="rightContent === '评论'"
        :key="postid"
      />
      <div
        class="putAway"
        v-if="rightContent !== '热榜'"
        style="left: -15px"
        @click="rightContent = '热榜'"
      >
        <n-icon size="28" color="#FFF" class="icon"
          ><ArrowUndoCircle />
        </n-icon>
      </div>
    </div>
    <leftEditor />
  </div>
</template>

<script setup>
import {
  ChevronBackCircleOutline,
  ChevronForwardCircleOutline,
  ArrowUndoCircle,
} from "@vicons/ionicons5";
import { ref, provide } from "vue";
import leftside from "../components/Home/leftside.vue";
import rightside from "../components/Home/rightside.vue";
import comments from "../components/Home/comments.vue";
import contents from "../components/Home/contents.vue";
import { Options } from "../store/options";
import leftEditor from "../components/Home/leftEditor.vue";
const opti = Options();
const rightContent = ref("热榜");
const postid = ref(null);
const plun_num = ref(null);
const contentsRef = ref();
function getComment(pid, plun) {
  postid.value = pid;
  plun_num.value = plun;
  rightContent.value = "评论";
}

provide("YgetComment", getComment);

function drag() {
  console.log("难实现，先不做了");
}

function changeTopic(key) {
  contentsRef.value.getpost(1, "topic", { topic_id: key });
}
</script>

<style scoped>
.leftside {
  background-color: rgba(246, 247, 246, 0.65);
  height: 100%;
  position: relative;
  display: flex;
}

.rightside {
  background: rgba(246, 247, 246, 0.05);
  height: 100%;
  position: relative;
  display: flex;
  flex-direction: column;
  overflow-y: scroll;
  scroll-behavior: smooth;
  overscroll-behavior: contain;
}

.rightside::-webkit-scrollbar {
  width: 0px;
}

.putAway {
  transition: color 0.3s var(--n-bezier), right 0.3s var(--n-bezier),
    left 0.3s var(--n-bezier), border-color 0.3s var(--n-bezier),
    background-color 0.3s var(--n-bezier);
  cursor: pointer;
  position: absolute;
  transform: translateX(50%) translateY(-50%);
  z-index: 1;
  top: 4%;
}

.drag {
  position: absolute;
  left: -1%;
  top: 45%;
  height: 5%;
  width: 2%;
  background-color: rgba(128, 128, 128, 0.6);
  cursor: w-resize;
}
</style>

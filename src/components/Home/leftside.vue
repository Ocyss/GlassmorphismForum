<template>
  <div class="navigation">
    <div>
      <n-icon size="16" tag="i">
        <Home24Filled />
      </n-icon>
      主页
    </div>
    <div>
      <n-icon size="16" tag="i">
        <Sticker24Filled />
      </n-icon>
      精选
    </div>
    <div>
      <n-icon size="16" :tag="i">
        <Star24Filled />
      </n-icon>
      关注
    </div>
  </div>
  <div class="folder">
    <n-collapse arrow-placement="right" :default-expanded-names="['1']">
      <n-collapse-item title="我的关注" name="1">
        <div>
          <ul class="topicOfConversation">
            <li>K40</li>
            <li>K30S</li>
            <li>MI12</li>
            <li>MI10</li>
            <li>MI6</li>
          </ul>
        </div>
      </n-collapse-item>
      <n-collapse-item title="热门话题" name="2">
        <div>很好</div>
      </n-collapse-item>
      <n-collapse-item title="数码话题" name="3">
        <div>真棒</div>
      </n-collapse-item>
    </n-collapse>
  </div>
</template>

<script setup>
import { Home24Filled, Sticker24Filled, Star24Filled } from "@vicons/fluent";
</script>

<style scoped>
.navigation {
  /* text-align: center; */
}

.navigation div {
  height: 3rem;
  font-size: 1.1rem;
  margin: 20px 15px;
  padding-left: 1.5rem;
}

.folder {
  width: 60%;
  margin: auto;
}

.topicOfConversation li {
  margin: 10px 20px;
  list-style-type: none;
}
</style>

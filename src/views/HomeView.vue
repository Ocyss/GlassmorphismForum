<template>
  <div id="main">
    <headers />
    <leftside />
    <rightside />
    <content />
  </div>
</template>

<script setup>
import headers from "../components/Home/headers.vue";
import leftside from "../components/Home/leftside.vue";
import rightside from "../components/Home/rightside.vue";
import content from "../components/Home/content.vue";
</script>

<style scoped>
#main {
  display: grid;
  grid-template-areas:
    "header header header header header"
    "leftside content content content rightside";
  align-items: center;
  justify-items: center;
}
</style>

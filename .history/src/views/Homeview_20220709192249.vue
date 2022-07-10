<template>
    <div id="main">
        <headers />
        <leftside />
        <rightside />
    </div>
</template>


<script setup>
import headers from '../components/Home/headers.vue'
import leftside from '../components/Home/leftside.vue'
import rightside from '../components/Home/rightside.vue'
import { Icon } from '@vicons/utils'
import { Home24Filled, Sticker24Filled, Star24Filled } from '@vicons/fluent'
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

.main {
    grid-area: content;
    background: rgb(204, 3, 3);
    height: 1500px;
}
</style>

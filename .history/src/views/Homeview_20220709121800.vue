<template>
    <div id="main">


    </div>
</template>


<script setup>
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

.rightside {
    grid-area: rightside;
    background: rgb(105, 221, 153);
    position: fixed;
    right: 0;
    top: 3.75rem;
    z-index: 9999;
    width: 15%;
}

.main {
    grid-area: content;
    background: rgb(204, 3, 3);
    height: 1500px;
}

.logo img {
    width: 50px;
    height: 50px;
}
</style>
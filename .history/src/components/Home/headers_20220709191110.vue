<template>
    <div class="header">
        <div class="logo">
            <img src="../../assets/logo.png" alt="LOGO">
        </div>
        <div class="searchBox">
            <n-input :style="{ width: '80%' }" />
            <n-button type="primary" ghost>
                搜索
            </n-button>
        </div>
        <div class="导航"></div>
    </div>
</template>


<style scoped>
.header {
    display: flex;
    width: 100%;
    grid-area: header;
    justify-content: space-evenly;
    position: fixed;
    top: 0;
    left: 0;
    z-index: 9999;
    height: 3.75rem;
    background: hsla(0, 0%, 100%, .9);
    backdrop-filter: blur(40px);
}

.searchBox {
    width: 280px;
}
</style>
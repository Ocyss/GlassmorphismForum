<template>
    <div id="main">
        <div class="header">
            <div class="logo">
                <img src="./assets/logo.png" alt="LOGO">
            </div>
            <div class="searchBox">
                <n-input :style="{ width: '80%' }" />
                <n-button type="primary" ghost>
                    搜索
                </n-button>
            </div>
            <div class="导航"></div>
        </div>
        <div class="leftside">
            <div class="重要导航">
                <span>
                    <icon size="20">
                        <Home24Filled />
                    </icon>
                    主页
                </span>
                <span>
                    <icon size="20">
                        <Sticker24Filled />
                    </icon>
                    精选
                </span>
                <span>
                    <icon size="20">
                        <Star24Filled />
                    </icon>
                    关注
                </span>
            </div>
            <div>
                <n-collapse arrow-placement="right">
                    <n-collapse-item title="我的关注" name="1">
                        <div>可以</div>
                    </n-collapse-item>
                    <n-collapse-item title="热门话题" name="2">
                        <div>很好</div>
                    </n-collapse-item>
                    <n-collapse-item title="数码话题" name="3">
                        <div>真棒</div>
                    </n-collapse-item>
                </n-collapse>
            </div>
        </div>
        <div class="rightside">
            <div class="个人信息">
                我是右侧栏我是右侧栏我是右侧栏我是右侧栏我是右侧栏我是右侧栏我是右侧栏我是右侧栏我是右侧栏我是右侧栏我是右侧栏我是右侧栏我是右侧栏我是右侧栏我是右侧栏我是右侧栏我是右侧栏我是右侧栏我是右侧栏我是右侧栏我是右侧栏我是右侧栏
                我是右侧栏我是右侧栏我是右侧栏我是右侧栏我是右侧栏我是右侧栏我是右侧栏</div>
            <div class="关注好友"></div>
        </div>
        <div class="main"></div>
    </div>
</template>
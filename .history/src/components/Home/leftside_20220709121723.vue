<template>
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
</template>
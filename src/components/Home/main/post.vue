<template>
  <div class="post">
    <div class="avatar">
      <n-avatar
        round
        :size="30"
        src="https://assets.paopao.info/public/avatar/55/0a/ce/15/75dd-4bec-be1d-125fd1bbdfb7.png"
      />
    </div>
    <div class="main">
      <div class="information">
        <div class="name">QIudie</div>
        <div class="time">1天前</div>
      </div>

      <div class="content">
        我是内容。。。我是内容。。。<br />我是内容。。。 我是内容。。。
        我是内容。。。 我是内容。。。
      </div>
      <div class="operation"></div>
    </div>
  </div>
</template>

<style scoped>
.post {
  width: 80%;
  height: 200px;
  margin: 20px auto;
  font-size: 0.8rem;
  background: rgb(255, 255, 255);
  display: flex;
  padding: 10px;
  border-radius: 25px;
}

.avatar {
  margin-right: 5px;
}
.information {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.information .name {
  color: rgb(54, 59, 100);
  margin-right: 5px;
  font-size: 1.2rem;
}
.information .time {
  font-size: 0.6rem;
  color: rgb(145, 148, 170);
  float: right;
}
.main {
  width: 100%;
}
</style>

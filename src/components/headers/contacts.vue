<template>
  <div class="contacts">
    <div>
      朋友
      <div>
        <ul>
          <li>1</li>
          <li>2</li>
          <li>3</li>
          <li>4</li>
          <li>5</li>
          <li>6</li>
        </ul>
      </div>
    </div>
    <div>
      关注
      <div>
        <ul>
          <li>1</li>
          <li>2</li>
          <li>3</li>
          <li>4</li>
          <li>5</li>
          <li>6</li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script setup></script>

<style scoped>
.contacts {
  min-height: 5vh;
  background: rgba(246, 247, 246, 0.9);
  padding: 10px 30px;
  max-height: 45vh;
  overflow-y: scroll;
  scroll-behavior: smooth;
  overscroll-behavior: contain;
}

.contacts div {
  font-size: 15px;
}
.contacts > div {
  font-size: 30px;
}
</style>

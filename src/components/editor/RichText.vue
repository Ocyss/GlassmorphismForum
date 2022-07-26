<template>
  <div style="border: 1px solid #ccc" class="main">
    <we-editor
        toolbar-class="toolbar"
        editable-class="editable"
        toolbar-style="border: 1px solid #d9d9d9"
        editable-style="border: 1px solid #d9d9d9;height:400px"
        :toolbar-option="toolbar"
        :editable-option="editable"
        :toolbar-reloadbefore="onToolbarReloadBefore"
        :editable-reloadbefore="onEditableReloadBefore"
        v-model="formData.jarr"
        v-model:json="formData.jstr"
        v-model:html="formData.html"
    />
  </div>
  <div>
    <n-button
        strong
        secondary
        size="large"
        type="success"
        class="sendbutton"
        @click="send"
    >
      发 射! 射! 射!
    </n-button>
  </div>
</template>

<script setup>
import '@wangeditor/editor/dist/css/style.css'
import {WeEditor, useWangEditor} from 'wangeditor5-for-vue3'
import {defineComponent, shallowReactive} from 'vue'
//https://clinfc.github.io/wangeditor5-for-vue3/

// 编辑器配置
const editableOption = {
  mode: 'simple',
  config: {
    MENU_CONF: {
      uploadImage: {
        server: '/api/upload',
        fieldName: 'your-fileName',
        base64LimitSize: 10 * 1024 * 1024,
        maxNumberOfFiles: 8,
      }
    },
  }
}

// 菜单栏配置
const toolbarOption = {
  mode: 'simple',
  config: {
    excludeKeys: [
      'insertVideo',
    ]
  }
}

// 防抖时长。当会触发重载的配置项发生变化 365ms 后，编辑器会重载
const reloadDelary = 365

const {editable, toolbar, getEditable, getToolbar, clearContent, reloadEditor} = useWangEditor(
    editableOption,
    toolbarOption,
    reloadDelary
)

// 不要使用 reactive/ref，应该使用 shallowReactive/shallowRef 来接收 json array 数据
const formData = shallowReactive({jarr: [], jstr: '', html: ''})

function onEditableReloadBefore(inst) {
  console.log('editable 即将重载: ' + new Date().toLocaleString())
}

function onToolbarReloadBefore(inst) {
  console.log('toolbar 即将重载: ' + new Date().toLocaleString())
}

function send() {
  console.log(formData.html)
}
</script>


<style scoped>

.sendbutton {
  margin-left: 70%;
  margin-top: 10%;
}

</style>

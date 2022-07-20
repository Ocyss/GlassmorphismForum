import { defineStore } from "pinia";

export const Options = defineStore("Options", {
  id: "Options",
  state: () => {
    return {
      letstate: true, // 侧栏打开还是关闭
      leftwi: "width: 0%;",
      contentwi: "width: 70%;",
      rightwi: "width: 30%;",
      putAwayrig: "right: -15px;",
      postid: -1,
      page: 1,
      pagetotal: -1,
      commenttotal: -1,
      writepost: false,
    };
  },
  getters: {},
  actions: {
    putAway() {
      if (this.letstate) {
        this.letstate = false;
        this.leftwi = "width: 0%;";
        this.contentwi = "width: 70%;";
        this.rightwi = "width: 30%;";
        this.putAwayrig = "right: -15px;";
      } else {
        this.letstate = true;
        this.leftwi = "width: 17%;";
        this.contentwi = "width: 58%;";
        this.rightwi = "width: 25%;";
        this.putAwayrig = "right: 0;";
      }
    },
  },
  persist: {
    enabled: true,
    strategies: [
      {
        key: "Options",
        storage: localStorage,
        paths: ["letstate", "leftwi", "contentwi", "rightwi", "putAwayrig"],
      },
    ],
  },
});

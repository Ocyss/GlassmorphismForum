import { defineStore } from "pinia";

export const userInfo = defineStore("storeUser", {
  id: "user",
  state: () => {
    return {
      uid: -1,
      user: "",
      name: "",
      permission: "",
      introduce: "",
      gender: "",
      configure: "",
      avatar: "",
      token: "",
    };
  },
  getters: {},
  actions: {
    setUser(data) {
      this.uid = data.id;
      this.user = data.user;
      this.name = data.name;
      this.permission = data.permission;
      this.introduce = data.introduce;
      this.gender = data.gender;
      this.configure = data.configure;
      this.avatar = data.avatar;
      this.token = data.token;
    },
  },
  persist: {
    enabled: true,
    strategies: [
      {
        key: "user",
        storage: localStorage,
      },
    ],
  },
});

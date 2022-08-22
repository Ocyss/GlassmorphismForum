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
      Registration_time: "",
      myFile: "",
    };
  },
  getters: {},
  actions: {
    setUser(data, token) {
      this.uid = data.id;
      this.user = data.user;
      this.name = data.name;
      this.permission = data.permission;
      this.introduce = data.introduce;
      this.gender = data.gender;
      this.configure = data.configure;
      this.avatar = data.avatar;
      this.token = token;
      this.Registration_time = data.Registration_time;
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

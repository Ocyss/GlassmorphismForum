import { createRouter, createWebHashHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";

const routes = [
  {
    path: "/",
    name: "home",
    component: HomeView,
  },
  {
    path: "/post",
    name: "post",
    component: () => import("../views/PostView.vue"),
  },
  {
    path: "/error",
    name: "error",
    component: () => import("../views/ErrorView.vue"),
  },
  {
    path: "/settings",
    name: "settings",
    children: [
      {
        path: "material",
        component: () => import("../views/settings/MaterialView.vue"),
      },
    ],
  },
];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

export default router;

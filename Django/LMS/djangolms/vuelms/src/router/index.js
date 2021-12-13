import { createRouter, createWebHistory } from "vue-router";
import Home from "../views/Home.vue";
import About from "../views/About.vue";
// auth
import Register from "../views/Register.vue";
import Login from "../views/Login.vue";
// Pages
import Account from "../views/pages/Account.vue";

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/about",
    name: "About",
    component: About,
  },
  {
    path: "/signup",
    name: "Register",
    component: Register,
  },
  {
    path: "/signin",
    name: "Login",
    component: Login,
  },
  {
    path: "/pages/my-account",
    name: "Account",
    component: Account,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;

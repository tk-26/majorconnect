import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home
  },
  {
    path: "/interest",
    name: "Interest",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "interest" */ "../views/Interest.vue")
  },
  {
    path: "/career",
    name: "Career",
    component: () =>
      import(/* webpackChunkName: "career" */ "../views/Career.vue")
  },
  {
    path: "/major",
    name: "Major",
    component: () =>
      import(/* webpackChunkName: "major" */ "../views/Major.vue")
  },
  {
    path: "/salary",
    name: "Salary",
    component: () =>
      import(/* webpackChunkName: "salary" */ "../views/Salary.vue")
  },
  {
    path: "/skill",
    name: "Skill",
    component: () =>
      import(/* webpackChunkName: "skill" */ "../views/Skill.vue")
  }
];

const router = new VueRouter({
  routes
});

export default router;

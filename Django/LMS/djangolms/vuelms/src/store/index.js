import { createStore } from "vuex";

export default createStore({
  state: {
    user: {
      token: "",
      isAuthenticated: false,
    },
  },
  mutations: {
    // function init store
    initializeStore(state) {
      if (localStorage.getItem("token")) {
        state.user.token = localStorage.getItem("token");
        state.user.isAuthenticated = true;
      } else {
        (state.user.token = ""), (state.user.isAuthenticated = false);
      }
    },
    // function set token
    setToken(state, token) {
      state.user.token = token;
      state.user.isAuthenticated = true;
    },
    // function hapus token
    removeToken(state) {
      state.user.token = "";
      state.user.isAuthenticated = false;
    },
  },
  actions: {},
  modules: {},
});

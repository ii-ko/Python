<template>
  <div class="signup">
    <div class="hero is-info">
      <div class="hero-body has-text-centered">
        <h1 class="title">Sign In Here</h1>
      </div>
    </div>

    <section class="section">
      <div class="container">
        <div class="columns">
          <div class="column is-4 is-offset-4">
            <form v-on:submit.prevent="submitForm">
              <div class="field">
                <label for="email">Email</label>
                <div class="control">
                  <input type="text" class="input" v-model="username" />
                </div>
              </div>
              <div class="field">
                <label for="password">Password</label>
                <div class="control">
                  <input type="password" class="input" v-model="password" />
                </div>
              </div>
              <div class="notification is-danger" v-if="errors.length">
                <p v-for="error in errors" v-bind:key="error">•{{ error }}</p>
              </div>
              <div class="field">
                <div class="control">
                  <button type="submit" class="button is-dark">Sign In</button>
                </div>
              </div>
            </form>
            <hr />
            <p>Need an account? <a href="/signup">Register Here</a></p>
            <a href="">Forgot Password</a>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      username: "",
      password: "",
      errors: [],
    };
  },
  methods: {
    submitForm() {
      console.log("Login User");
      axios.defaults.headers.common["Authorization"] = "";

      localStorage.removeItem("token");

      this.errors = [];

      if (this.username == "") {
        this.errors.push("The email is missing");
      }
      if (this.password == "") {
        this.errors.push("The password is missing");
      }

      if (!this.errors.length) {
        const formData = {
          username: this.username,
          password: this.password,
        };

        axios
          .post("/api/v1/token/login/", formData)
          .then((response) => {
            const token = response.data.auth_token;

            this.$store.commit("setToken", token);

            axios.defaults.headers.common["Authorization"] = "Token " + token;

            localStorage.setItem("token", token);

            this.$router.push("/pages/my-account");
          })
          .catch((error) => {
            if (error.response) {
              for (const property in error.response.data) {
                this.errors.push(property + ": " + error.response.data[property]);
              }
              console.log(JSON.stringify(error.response.data));
            } else if (error.message) {
              this.errors.push("Something went wrong. Please try again");
              console.log(JSON.stringify(error));
            }
          });
      }
    },
  },
};
</script>

<style></style>

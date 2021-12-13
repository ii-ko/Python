<template>
  <div class="signup">
    <div class="hero is-info">
      <div class="hero-body has-text-centered">
        <h1 class="title">Sign Up Here</h1>
      </div>
    </div>

    <section class="section">
      <div class="container">
        <div class="columns">
          <div class="column is-4 is-offset-4">
            <form v-on:submit.prevent="submitForm">
              <div class="field">
                <label for="username">Username</label>
                <div class="control">
                  <input type="text" class="input" v-model="username" />
                </div>
              </div>
              <div class="field">
                <label for="email">Email</label>
                <div class="control">
                  <input type="email" class="input" v-model="email" />
                </div>
              </div>
              <div class="field">
                <label for="password">Password</label>
                <div class="control">
                  <input type="password" class="input" v-model="password.password" />
                </div>
              </div>
              <div class="field">
                <label for="conf_password">Confirm Password</label>
                <div class="control">
                  <input type="password" class="input" v-model="password.confirm" />
                </div>
              </div>
              <div class="notification is-danger" v-if="errors.length">
                <p v-for="error in errors" v-bind:key="error">•{{ error }}</p>
              </div>
              <div class="field">
                <div class="control">
                  <button type="submit" class="button is-dark">Sign Up</button>
                </div>
              </div>
            </form>
            <hr />
            <p>Already have an account? <a href="/signin">Login Here</a></p>
            <a href="">Forgot Password</a>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
export default {
  data() {
    return {
      username: "",
      email: "",
      password: {
        password: "",
        confirm: "",
      },
      errors: [],
    };
  },
  methods: {
    submitForm() {
      console.log("Register User");

      this.errors = [];

      if (this.username == "") {
        this.errors.push("The username is missing");
      }
      if (this.email == "") {
        this.errors.push("The email is missing");
      }
      if (this.password.password == "") {
        this.errors.push("The password is missing");
      }
      if (this.password.confirm == "" || this.password.confirm != this.password.password) {
        this.errors.push("The password are not match. Please try again");
      }
    },
  },
};
</script>

<style></style>

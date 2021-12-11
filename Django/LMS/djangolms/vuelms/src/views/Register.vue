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
            <form action="">
              <div class="field">
                <label for="username">Username</label>
                <div class="control">
                  <input type="email" class="input" />
                </div>
              </div>
              <div class="field">
                <label for="email">Email</label>
                <div class="control">
                  <input type="text" class="input" />
                </div>
              </div>
              <div class="field">
                <label for="password">Password</label>
                <div class="control">
                  <input type="password" class="input" />
                </div>
              </div>
              <div class="field">
                <label for="conf_password">Confirm Password</label>
                <div class="control">
                  <input type="password" class="input" />
                </div>
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
import { required, minLength, maxLength, between } from "vuelidate/lib/validators";

export default {
  name: "FormValidation",
  data() {
    return {
      username: "",
      email: "",
      password: "",
      conf_password: "",
    };
  },
};
</script>

<style></style>

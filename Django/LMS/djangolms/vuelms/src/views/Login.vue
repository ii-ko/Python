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
            <form action="">
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
export default {};
</script>

<style></style>

<template>
  <div class="header">
    <nav class="navbar is-info" role="navigation" aria-label="main navigation" style="min-height: 5rem">
      <div class="navbar-brand">
        <a href="/" class="navbar-item is-size-4">DjangoLMS</a>
      </div>
      <div id="navbar-item" class="navbar-menu">
        <div class="navbar-start">
          <a href="/" class="navbar-item">Home</a>
          <a href="/about" class="navbar-item">About</a>
        </div>

        <div class="navbar-end">
          <div class="navbar-item">
            <div class="buttons">
              <div class="button is-primary">
                <strong>Sign Up</strong>
              </div>
              <div class="button is-light">Sign In</div>
            </div>
          </div>
        </div>
      </div>
    </nav>
    <router-view />
    <footer class="footer">
      <p class="has-text-centered">Copyright © 2021</p>
    </footer>
  </div>
</template>

<style lang="scss">
@import "../node_modules/bulma";
</style>

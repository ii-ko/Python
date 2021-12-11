<template>
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
            <a href="/signup" class="button is-primary">
              <strong>Sign Up</strong>
            </a>
            <a href="/signin" class="button is-light">Sign In</a>
          </div>
        </div>
      </div>
    </div>
  </nav>
</template>

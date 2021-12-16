<template>
  <nav class="navbar is-info" role="navigation" aria-label="main navigation" style="min-height: 5rem">
    <div class="navbar-brand">
      <router-link to="/" class="navbar-item is-size-4">DjangoLMS</router-link>
    </div>
    <div id="navbar-item" class="navbar-menu">
      <div class="navbar-start">
        <router-link to="/" class="navbar-item">Home</router-link>
        <router-link to="/pages/courses" class="navbar-item">Courses</router-link>
        <router-link to="/about" class="navbar-item">About</router-link>
      </div>

      <div class="navbar-end">
        <div class="navbar-item">
          <div class="buttons">
            <template v-if="$store.state.user.isAuthenticated">
              <router-link to="/pages/my-account" class="button is-info">My Account</router-link>
              <router-link to="" class="button is-danger">Log Out</router-link>
            </template>
            <template v-else>
              <router-link to="/signup" class="button is-primary">
                <strong>Sign Up</strong>
              </router-link>
              <router-link to="/signin" class="button is-light">Sign In</router-link>
            </template>
          </div>
        </div>
      </div>
    </div>
  </nav>
</template>

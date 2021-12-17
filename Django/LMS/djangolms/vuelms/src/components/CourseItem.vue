<template>
  <div class="card">
    <div class="card-image">
      <figure class="image is-4yb3">
        <img src="@/assets/default.png" alt="placeholders" />
      </figure>
    </div>
    <div class="card-content">
      <div class="media">
        <div class="media-body">
          <p class="is-size-5">{{ course.title }}</p>
        </div>
      </div>
      <div class="content">
        <p>{{ course.short_description }}</p>
        <router-link :to="{ name: 'Course_detail', params: { slug: course.slug } }" href="">More</router-link>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: ["course"],
};
</script>

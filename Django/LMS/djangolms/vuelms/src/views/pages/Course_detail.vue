<template>
  <div class="course">
    <div class="hero is-info">
      <div class="hero-body has-text-centered">
        <h1 class="title">{{ course.title }}</h1>
      </div>
    </div>
    <section class="section">
      <div class="container">
        <div class="columns content">
          <div class="column is-2">
            <h2>Table of contents</h2>
            <ul>
              <li class="li" v-for="lesson in lessons" v-bind:key="lesson.id">
                <a @click="activeLesson = lesson">{{ lesson.title }}</a>
              </li>
            </ul>
          </div>

          <div class="column is-10">
            <template v-if="$store.state.user.isAuthenticated">
              <template v-if="activeLesson">
                <h2>{{ activeLesson.title }}</h2>
                {{ activeLesson.long_description }}
              </template>

              <template v-else>
                {{ course.long_description }}
              </template>
            </template>

            <template v-else>
              <h2>Restricted Access</h2>

              <p>You need to have an account to continue</p>
            </template>
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
      course: {},
      lessons: [],
      activeLesson: null,
    };
  },
  // Mounted merupakan tipe lifecycle pada Vue yang memungkinkan kita untuk mengakses dom persis sebelum dan sesudah template di-render.
  // Jangan gunakan lifecycle tipe ini untuk keperluan mengambil data dan event, karena template membutuhkan data tersebut sebelum ditampilkan
  mounted() {
    console.log("mounted");

    const slug = this.$route.params.slug;
    axios.get("/api/v1/courses/" + slug).then((response) => {
      console.log(response.data);

      this.course = response.data.course;
      this.lessons = response.data.lesson;
    });
  },
};
</script>

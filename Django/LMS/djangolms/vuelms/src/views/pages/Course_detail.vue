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
              <li class="li"><a href="">Introduction</a></li>
              <li class="li"><a href="">Get Started</a></li>
              <li class="li"><a href="">Part 1</a></li>
              <li class="li"><a href="">Part 2</a></li>
              <li class="li"><a href="">Summary</a></li>
            </ul>
          </div>

          <div class="column is-10">
            {{ course.long_description }}
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
      course: [],
    };
  },
  // Mounted merupakan tipe lifecycle pada Vue yang memungkinkan kita untuk mengakses dom persis sebelum dan sesudah template di-render.
  // Jangan gunakan lifecycle tipe ini untuk keperluan mengambil data dan event, karena template membutuhkan data tersebut sebelum ditampilkan
  mounted() {
    console.log("mounted");

    const slug = this.$route.params.slug;
    axios.get("/api/v1/courses/" + slug).then((response) => {
      console.log(response.data);

      this.course = response.data;
    });
  },
};
</script>

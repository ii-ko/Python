<template>
  <div class="home">
    <div class="hero is-info is-medium">
      <div class="hero-body has-text-centered">
        <h1 class="title">Welcome to DjangoLMS</h1>

        <h2 class="subtitle">An online place for learning what you want.</h2>
      </div>
    </div>

    <section class="section">
      <div class="container">
        <div class="columns is-multiline">
          <div class="column is-4">
            <div class="box has-text-centered">
              <span class="icon is-size-2 has-text-info"><i class="far fa-clock"></i></span>
              <h2 class="is-size-4 mt-4 mb-4">Study at your own pace</h2>
              <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Dolorum doloremque blanditiis iste adipisci esse quas debitis quo nobis.</p>
            </div>
          </div>
          <div class="column is-4">
            <div class="box has-text-centered">
              <span class="icon is-size-2 has-text-info"><i class="far fa-comments"></i></span>
              <h2 class="is-size-4 mt-4 mb-4">Study with others</h2>
              <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Dolorum doloremque blanditiis iste adipisci esse quas debitis quo nobis.</p>
            </div>
          </div>
          <div class="column is-4">
            <div class="box has-text-centered">
              <span class="icon is-size-2 has-text-info"><i class="fas fa-home"></i></span>
              <h2 class="is-size-4 mt-4 mb-4">Study from your home</h2>
              <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Dolorum doloremque blanditiis iste adipisci esse quas debitis quo nobis.</p>
            </div>
          </div>

          <div class="column is-12 has-text-centered">
            <a href="" class="button is-info is-size-3 mt-6 mb-6"> Click to get started </a>
          </div>

          <hr />
          <div class="column is-3" v-for="course in courses" v-bind:key="course.id">
            <CourseItem :course="course" />
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import axios from "axios";
import CourseItem from "@/components/CourseItem";

export default {
  name: "Home",
  data() {
    return {
      courses: [],
    };
  },
  components: {
    CourseItem,
  },
  // Mounted merupakan tipe lifecycle pada Vue yang memungkinkan kita untuk mengakses dom persis sebelum dan sesudah template di-render.
  // Jangan gunakan lifecycle tipe ini untuk keperluan mengambil data dan event, karena template membutuhkan data tersebut sebelum ditampilkan
  mounted() {
    console.log("mounted");

    axios.get("/api/v1/courses/get_frontpage_courses/").then((response) => {
      console.log(response.data);

      this.courses = response.data;
    });
  },
};
</script>

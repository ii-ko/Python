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
                <a @click="setActiveLesson(lesson)">{{ lesson.title }}</a>
              </li>
            </ul>
          </div>

          <div class="column is-10">
            <template v-if="$store.state.user.isAuthenticated">
              <template v-if="activeLesson">
                <h2>{{ activeLesson.title }}</h2>
                {{ activeLesson.long_description }}
                <hr />

                <h2>Comments</h2>
                <article class="media box" v-for="comment in comments" v-bind:key="comment.id">
                  <div class="media-content">
                    <div class="content">
                      <template> </template>
                      <p>
                        <strong>{{ comment.name }}</strong>
                        {{ dateTime(comment.create_at) }}<br />
                        {{ comment.content }}
                      </p>
                    </div>
                  </div>
                </article>
                <br />

                <h2>Add Comment</h2>
                <form v-on:submit.prevent="submitComment()">
                  <div class="field">
                    <label for="label">Name</label>
                    <div class="control">
                      <input type="text" class="input" v-model="comment.name" />
                    </div>
                  </div>

                  <div class="field">
                    <label for="label">Comment</label>
                    <div class="control">
                      <textarea class="textarea" v-model="comment.content" />
                    </div>
                  </div>

                  <div class="field">
                    <div class="control">
                      <button class="button is-link">Submit</button>
                    </div>
                  </div>
                </form>
                <br />
                <div class="notification is-danger" v-if="errors.length">
                  <p v-for="error in errors" v-bind:key="error">•{{ error }}</p>
                </div>
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
import moment from "moment";

export default {
  data() {
    return {
      course: {},
      lessons: [],
      comments: [],
      activeLesson: null,
      comment: {
        name: "",
        content: "",
      },
      errors: [],
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

  methods: {
    dateTime(value) {
      return moment(value).format("YYYY-MM-DD");
    },

    submitComment() {
      console.log("submit comment");

      this.errors = [];

      if (this.comment.name == "") {
        this.errors.push("The name must be filled out");
      }

      if (this.comment.content == "") {
        this.errors.push("The comment must be filled out");
      }

      if (!this.errors.length) {
        axios
          .post("/api/v1/courses/" + this.course.slug + "/" + this.activeLesson.slug + "/", this.comment)
          .then((response) => {
            this.comment.name = "";
            this.comment.content = "";
            this.comments.push(response.data);
          })
          .catch((error) => {
            console.log(error);
          });
      }
    },

    setActiveLesson(lesson) {
      this.activeLesson = lesson;
      this.getComments();
    },

    getComments() {
      axios.get("/api/v1/courses/" + this.course.slug + "/" + this.activeLesson.slug + "/comments/").then((response) => {
        console.log(response.data);
        this.comments = response.data;
      });
    },
  },
};
</script>

<template>
  <v-app>
    <v-app-bar
      app
      color="#25272b"
      dark
    >
      <div class="d-flex align-center">
        <v-img
          alt="Project Jesaja Logo"
          class="shrink mr-2"
          contain
          src="../data/logo_transparent.png"
          transition="scale-transition"
          width="120"
        />

        <h3>
          Projekt Jesaja
        </h3>
      </div>

      <v-spacer></v-spacer>

    </v-app-bar>

    <v-main>
      <mainPage/>
    </v-main>
  </v-app>
</template>

<script>
//import WritingFeedbackComp from './components/writingFeedback/WritingFeedbackComp';
import mainPage from './components/mainPage/mainPage';

export default {
  name: 'App',

  components: {
    //WritingFeedbackComp,
    mainPage
  },
};
</script>

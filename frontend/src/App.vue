<template>
  <v-app>
    <v-app-bar
      app
      color="#25272b"
      dark
    >
      <div class="d-flex align-center">
        <v-img
          alt="Vuetify Logo"
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
      <v-btn @click="callPredict"></v-btn>
      <HelloWorld/>
    </v-main>
  </v-app>
</template>

<script>
import { mapActions } from 'vuex';
import * as types from './store/types';
import HelloWorld from './components/HelloWorld';

export default {
  name: 'App',

  components: {
    HelloWorld,
  },

  data: () => ({
    test: 'Test text to test vuex store and api calls.'
  }),
  methods: {
    ...mapActions({
    predict: types.predictEval
    }),
    callPredict() {
      this.predict(this.test);
    }
  }
};
</script>

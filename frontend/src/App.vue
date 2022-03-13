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
      <router-view />
    </v-main>
  </v-app>
</template>

<script>


export default {
  name: 'App',

  components: {
  },
};
</script>

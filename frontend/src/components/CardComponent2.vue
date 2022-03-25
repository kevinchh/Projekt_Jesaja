<template>
  <v-card
    class="mx-auto my-12 rounded-lg card"
    max-width="374"
  >
    <v-img
      height="150"
      class="white--text align-end"
      src="@/assets/feedback_eval/feedback_evaluation.png"
    >
        <div class="overlay2">
            <v-card-title class="py-0">{{title}}</v-card-title>
        </div>
    </v-img>

    <v-card-text class="pb-0">
      <div>Receive feedback on your writing and increase opportunities to improve writing outcomes!</div>
    </v-card-text>

    <v-divider class="mx-4"></v-divider>

    <span class="pl-4 subtitle-2">Tools</span>

    <v-card-text class="py-0">
      <v-chip-group
        column
      >
        <v-chip small>Transformers</v-chip>

        <v-chip small>BigBird</v-chip>

        <v-chip small>Flask</v-chip>

        <v-chip small>. . .</v-chip>
      </v-chip-group>
    </v-card-text>

    <v-card-actions>
      <v-row
        align="center"
        justify="end"
        class="ma-0"
      >
        <v-btn
          text
          color="orange lighten-3"
          dark
          @click="openApp()"
        >
          Go to
          <v-icon
              right
              dark
          >
              mdi-open-in-new
          </v-icon>
        </v-btn>
      </v-row>
    </v-card-actions>
  </v-card>
</template>

<script>
import {ROUTE_NAMES as router} from '@/router/routerNames';

export default {
  name: 'CardComponent2',
  props: {
    title: {
      // title text
      type: String,
      required: true
    }
  },
  data: () => ({}),
  methods: {
    openApp() {
      //pass link over parameters
      this.$router.push(router.EVAL)
    }
  }
}
</script>

<style>
  .card {
    transition: transform 500ms ease;
  }

  .card:hover,
  .card:focus-within {
    transform: scale(1.05);
  }

  .overlay2 {
    width: 100%;
    height: 100%;
    padding-top: 2rem;
    background: linear-gradient(
      hsl(0 0% 0% / 0),
      hsl(20 0% 0% / 0.05) 40%,
      hsl(20 0% 0% / 0.2) 70%,
      hsl(0 0% 0% / 0.7)
    );
  }
</style>
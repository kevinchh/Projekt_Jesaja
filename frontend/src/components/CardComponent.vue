<template>
  <v-card class="rounded-lg card" dark color="primary" >
    <div class="overlay">
      <div class="card-content">
        <div class="headline card-title">
          {{title}}
        </div>

        <p class="caption card-subtitle">
          Receive feedback on your writing and increase opportunities to improve writing outcomes!
        </p>

       <div class="tech-tags">
        <v-chip x-small color="success">Transformers</v-chip>
        <v-chip x-small color="error">BigBird</v-chip>
        <v-chip x-small color="primary">Flask</v-chip>
        <v-chip x-small>. . .</v-chip>
       </div> 

        <v-card-actions class="mb-4">
          <v-row
            align="center"
            justify="end"
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
      </div>
    </div> 
    
  </v-card>
</template>

<script>
import {ROUTE_NAMES as router} from '@/router/routerNames';

export default {
  name: 'CardComponent',
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
    background-image: url(../assets/feedback_eval/feedback_evaluation.png);
    background-size: cover;
    max-width: 35ch;
    overflow: hidden;
    margin-left: auto;
    margin-right: auto;
    transition: transform 500ms ease;
  }

  .card:hover,
  .card:focus-within {
    transform: scale(1.1);
  }

  .overlay {
    padding: 7rem 0 0;
    width: 100%;
    height: 100%;
    background: linear-gradient(
      hsl(0 0% 0% / 0) 20%,
      hsl(20 0% 0% / 0.2) 40%,
      hsl(0 0% 0% / 0.7)
    );
  }

  .card-content {
    --padding: 1.2rem;
    padding: var(--padding) var(--padding) 0.1rem;
  }

  .card-title {
      width: max-content;
      position: relative;
      margin-bottom: 0.6rem;
  }

  .card-title::after {
      content: '';
      position: absolute;
      height: 2px;
      left: calc(var(--padding) * -1);
      bottom: 0;
      width: calc(100% + var(--padding));
      background: hsl(36 100% 65% / 1);
  }


  .card-subtitle {
    padding-top: var(--paading);
    color: rgb(255 255 255 / 0.85)
  }

  @media (hover) {
    .overlay {
      background: linear-gradient(
        hsl(0 0% 0% / 0) 50%,
        hsl(20 0% 0% / 0.2) 80%,
        hsl(0 0% 0% / 0.7)
      );
    }

    .card:hover .overlay,
    .card:focus-within .overlay {
      background: linear-gradient(
        hsl(0 0% 0% / 0),
        hsl(20 0% 0% / 0.2) 40%,
        hsl(0 0% 0% / 0.7)
      );
    }

    .card-content {
      transform: translateY(70%);
      transition: transform 500ms ease;
    }

    .card:hover .card-content,
    .card:focus-within .card-content {
      transform: translateY(0);
      transition-delay: 500ms;
    }

    .card:focus-within .card-content {
      transition-duration: 0ms;
      transition-delay: 0ms;
    }

    .card-content > *:not(.card-title) {
      opacity: 0;
      transition: opacity 500ms linear;
      transition-delay: 800ms;
    }

    .card:hover .card-content > *:not(.card-title),
    .card:focus-within .card-content > *:not(.card-title) {
      opacity: 1;
    }

    .card-title::after {
      transform: scaleX(0);
      transform-origin: left;
      transition: transform 500ms ease;
    }

    .card:hover .card-title::after, 
    .card:focus-within .card-title::after {
      transform: scaleX(1);
    }
  }

  .tech-tags {
    display: flex;
    flex-wrap: wrap;
    justify-content: flex-start;
  }

  .tech-tags > .v-chip {
    margin: 4px;
  }
</style>
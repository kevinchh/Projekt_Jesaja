<template>
  <div class="background">
    <v-container class="pb-0">
      <v-row class="text-start mt-2">
        <v-col cols="12">
          <div class="display-2 font-weight-light">Feedback Evaluation</div>
        </v-col>
      </v-row>
      <v-row>
        <v-col>
          <v-btn
            class="my-2 rounded-lg"
            x-large
            dark
            :plain="app_site == 0"
            color="blue-grey darken-2"
            @click="goToApp"
          >
            Application
          </v-btn>
          <v-btn
            class="ml-2 my-2 rounded-lg"
            x-large
            dark
            :plain="app_site == 1"
            color="blue-grey darken-2"
            @click="goToExpl"
          >
            Explanation
          </v-btn>
        </v-col>
      </v-row>
    </v-container>
    <div v-if= "app_site == 1">
      <WritingFeedbackApp/>
    </div>
    <div v-if= "app_site == 0">
      <WritingFeedbackExp/>
    </div>
  </div>
</template>

<script>
import WritingFeedbackApp from './WritingFeedbackApp';
import WritingFeedbackExp from './WritingFeedbackExp';

export default {
  name: 'WritingFeedbackComp',
  components: {
    WritingFeedbackApp,
    WritingFeedbackExp
  },
  data: () => ({
    app_site : 1
  }),
  methods: {
    goToApp(){
      this.app_site = 1
    },
    goToExpl(){
      this.app_site = 0
    }
  }
}
</script>

<style>
  .background {
    background-color: #F5F4F4;
    width: 100%;
    height: 100%;
  }
</style>
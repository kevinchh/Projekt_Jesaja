<template>
  <div>
    <v-container>
      <v-row class="text-center">
        <v-col cols="12">
          <h1>Feedback Evaluation</h1>
        </v-col>
      </v-row>
      <v-row>
        <v-col>
          <div class="text-center">
            <v-btn
              class="ma-2"
              outlined
              color="black"
              @click="goToApp"
            >
              Application
            </v-btn>
            <v-btn
              class="ma-2"
              outlined
              color="black"
              @click="goToExpl"
            >
              Explanation
            </v-btn>
          </div>
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

<template>
  <AppHeader
    title="Feedback Evaluation"
    :size="2"
    :buttonTexts="buttonTexts"
  >
    <template v-slot:button1>
      <WritingFeedbackApp />
    </template>
    <template v-slot:button2>
      <WritingFeedbackExp />
    </template>
  </AppHeader>
</template>

<script>
import AppHeader from '../AppHeader';
import WritingFeedbackApp from './WritingFeedbackApp';
import WritingFeedbackExp from './WritingFeedbackExp';

export default {
  name: 'WritingFeedbackComp',
  components: {
    AppHeader,
    WritingFeedbackApp,
    WritingFeedbackExp
  },
  data: () => ({
    buttonTexts: [
      'Application',
      'Explanation'
    ]
  })
}
</script>
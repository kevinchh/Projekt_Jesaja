<template>
  <div>
    <v-container>
      <v-row :style = "{'padding-top': '100px'}">
        <v-col cols="5" class = "text-center">
          <div :style="{'background': '#eee', 'padding-bottom':'20px'}">
            <h2 :style = "{'padding-top': '10px'}">What does the model do?</h2>
            <br />
            <p class =".subtitle-1 text--secondary font-italic">
              Helping students increase their writing proficiency.
            </p>
          </div>
        </v-col>
        <v-col col = "7" :style = "{
          'text-align': 'left',
          'padding-left': '50px',
          'padding-right': '50px',
          'overflow': 'auto'}">
          <span class=".body-1" >
            Writing is an important prerequisite for success. But according to the American National Assessment of Educational Progress,
            less than a third of US high school students are proficient writers. Low-income students fare even worse than that,
            as less than 15 percent demonstrate writing proficiency. Therefore, the goal of our model is to
            help students improve their writing via automated feedback tools. More specifically, we want to provide feedback by
            identifying writing structures, such as thesis statements and support for claims in student essays.
            We took data provided by a Kaggle competition and used it to train a model which is able to
            automatically segment texts and classify argumentative,
            as well as rhetorical elements in essays written by 6th-12th grade students. All in all, the model we implemented is able to differentiate between Leads (L),
            Positions (Pos), Claims (C), Counterclaims (CC), Rebuttals (R), Evidences (Ev) and Concluding Statements (ConSt).
          </span>
          <v-img
            alt="textfeedback"
            contain
            src="../../assets/feedback_eval/txtfeedback.png"
            transition="scale-transition"
          />
          <br />
          <span class=".body-1">
            Our model can be used to make it easier for students to receive feedback on their writing and increase opportunities to improve writing outcomes.
            It may be directly integrated and used by virtual writing tutors or automated writing systems, while teachers could make us them to reduce grading time.
          </span>
        </v-col>
      </v-row>
      <v-row :style = "{'padding-top': '200px'}">
        <v-col col = "7" :style = "{
          'text-align': 'left',
          'padding-left': '50px',
          'padding-right': '50px',
          'overflow': 'auto'}">
          <span class=".body-1">
              The model we use for solving this task is the implemented version provided by HuggingFace. More specifically, we leverage their implementation of the
            </span>
               <a href="https://arxiv.org/abs/2007.14062">Big Bird architecture</a>,
          <span> which is a transformer-based model. Such models are some of the most successfull when it comes to
                the application of DL to NLP. However, they come with a core limitation: they have a quadratic dependency on the sequence length due to their full attention
                mechanism.
          </span>
          <span class ="font-weight-bold">
            But what is the full-attention mechanism?
          </span>
          <p>
            Basically transformers receive
          </p>
        </v-col>
        <v-col cols="5" class = "text-center">
          <div :style="{'background': '#eee', 'padding-bottom':'20px'}">
            <h2 :style = "{'padding-top': '10px'}">How does the model work?</h2>
            <br />
            <p class =".subtitle-1 text--secondary font-italic">
              Levering scientifc advances in the field of NLP through usage of the Big Bird architecture.
            </p>
          </div>
        </v-col>
      </v-row>
      <v-row :style = "{'padding-top': '200px'}">
        <v-col cols="5" class = "text-center">
          <div :style="{'background': '#eee', 'padding-bottom':'20px'}">
            <h2 :style = "{'padding-top': '10px'}">How is the data processed?</h2>
            <br />
            <p class =".subtitle-1 text--secondary font-italic">
              Our data processing pipeline explained.
            </p>
          </div>
        </v-col>
        <v-col col = "7" :style = "{
          'text-align': 'left',
          'padding-left': '50px',
          'padding-right': '50px',
          'overflow': 'auto'}">
          <span class=".body-1">
            Hi lets go
          </span>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>





<script>

  export default {
    name: 'WritingFeedbackExp',
    components : {
    }
}
</script>

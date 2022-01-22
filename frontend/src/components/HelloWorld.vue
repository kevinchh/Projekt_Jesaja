<template>
  <v-container>
    <v-row class="text-center">
      <v-col cols="12">
        <h1>Feedback Evaluation</h1>
      </v-col>
    </v-row>
    <v-row class="grey d-flex lighten-5" justify-content="center">
      <v-col cols="6"  align-self="center">
        <v-card outlined width="600" height = "400">
          <v-textarea
            v-model = "inp"
            name="name"
            label="Test Eingabe"
            id="id"
            no-resize
            full-width
            height= 370
            loading = false
          ></v-textarea>
          </v-card>
      </v-col >
      <v-col cols = "6" >
          <v-card outlined width="600" height = "400">
            <div v-if="loading">
                <span :style = "{'text-align': 'center'}" >
                  Progressing your input
                </span>
                <v-progress-linear
                color="success"
                indeterminate
                rounded
                height="10"
                width = "4"
              ></v-progress-linear>
            </div>
            <span v-for="i in calcData" :key="i.text" :style = "{ 'color': i.color, 'text-align': 'left' }">
              {{i.text}}
            </span>
          </v-card>
      </v-col>
      <v-col cols="6" >
          <v-card outlined width="600" height = "400">
            <div v-if="loading">
                Loading Bar
            </div>
                <span
                  v-for="(val, idx) in output" 
                  :key="idx"
                  @mouseover="mouseOverSpan(idx)"
                  @mouseleave="mouseLeaveSpan(idx)"
                  :style = "{ 
                    'background-color': active[idx] ? val.transitionColor : val.color, 
                    'border-radius': '20px', 
                    'text-align': 'left', 
                    'padding': '3px 2px 3px'}">

                  <v-tooltip v-if="val.queryName !== 'O'" top>
                    <template v-slot:activator="{ on, attrs }">
                      <v-chip 
                        v-bind="attrs"
                        v-on="on"
                        dark 
                        small 
                        :color="val.shadeColor">{{val.arg}}</v-chip>
                    </template>
                    <span>{{val.queryName}}</span>
                  </v-tooltip>
                  {{val.text}}
                </span>
          </v-card>
      </v-col>
    </v-row>
    <v-row>
      <v-col cols="12">
        <v-btn
          color="blue-grey"
          class="ma-2 white--text"
          fab
          :disabled = "!inp "
          @click="callPredict">
          <v-icon dark>
            mdi-cloud-upload
          </v-icon>
        </v-btn>
      </v-col >
    </v-row >
    <v-row>
      <v-expansion-panels>
        <v-expansion-panel>
          <v-expansion-panel-header>
            Color Description
          </v-expansion-panel-header>
          <v-expansion-panel-content>
            <div v-for="(k,i) in color_code" :key="k">
              <span v-bind:style = "{ 'color': k}">
                {{i}}
              </span>
            </div>
          </v-expansion-panel-content>
        </v-expansion-panel>
      </v-expansion-panels>
    </v-row>
  </v-container>
</template>

<script>
import Vue from 'vue';
import { mapActions, mapGetters } from 'vuex';
import * as types from '../store/types';
import { colorCode } from '../const/evaluationTypes';


  export default {
    name: 'HelloWorld',
    components : {
  },

    data: () => ({
      color_code: colorCode,
      inp: "Furthermore, asking for multiple opinions can benifit during competitions for a position slot, as cadidates needs to make decisions on what they need to say or do. For example, it can be helpful in situations like elections, both for the U.S. or simply in school. If a student is running for a position in office to represent his/her school, he/she can ask a widespread and diverse audience. First, asking other students is their best bet to obtaining information. Other students can inform him/her about what they want, like better water fountains, recess, or healthier food. Then, the student running can make changes to the way they run for the election, and on his/her speech, take a different approach. In addition, if the student running asks an adult, they will get to know a more realistic way the school can be improved. Since a student, even as a student officer, isn't able to make a significant change to a school, they can inform the school board about ways to make the school better.",
      active: Array(8).fill(false),
      output: [
        {
          text: "Furthermore, asking for multiple opinions can benifit during competitions for a position slot, as cadidates needs to make decisions on what they need to say or do.",
          color: "#6ce26d66",
          transitionColor: "#6CE26D",
          shadeColor: "#187719",
          arg: "L",
          queryName: "Lead"
        },
        {
          text: "For example, it can be helpful in situations like elections, both for the U.S. or simply in school.",
          color: "#49b4dc66",
          transitionColor: "#49B4DC",
          shadeColor: "#175E78",
          arg: "Ev",
          queryName: "Evidence"
        },
        {
          text: " If a student is running for a position in office to represent his/her school, he/she can ask a widespread and diverse audience. First, asking other students is their best bet to obtaining information.",
          color: "#e19a6366",
          transitionColor: "#E19A63",
          shadeColor: "#894A1A",
          arg: "Pos",
          queryName: "Position"
        },
        {
          text: "Since a student, even as a student officer, isn't able to make a significant change to a school, they can inform the school board about ways to make the school better.",
          color: "#eba69a66",
          transitionColor: "#EBA69A",
          shadeColor: "#882B1B",
          arg: "C",
          queryName: "Claim"
        },
        {
          text: "For example, it can be helpful in situations like elections, both for the U.S. or simply in school.",
          color: "",
          transitionColor: "",
          shadeColor: "",
          arg: "O",
          queryName: "O"
        },
        {
          text: "For example, it can be helpful in situations like elections, both for the U.S. or simply in school.",
          color: "#c2c34b66",
          transitionColor: "#C2C34B",
          shadeColor: "#7A7A29",
          arg: "CC",
          queryName: "Counterclaim"
        },
        {
          text: "For example, it can be helpful in situations like elections, both for the U.S. or simply in school.",
          color: "#aa6cce66",
          transitionColor: "#AA6CCE",
          shadeColor: "#5C297A",
          arg: "R",
          queryName: "Rebuttal"
        },
        {
          text: "For example, it can be helpful in situations like elections, both for the U.S. or simply in school.",
          color: "#54c67666",
          transitionColor: "#54C676",
          shadeColor: "#297A41",
          arg: "ConSt",
          queryName: "Concluding Statement"
        }
      ]
    }),
    methods: {
      ...mapActions({
        predict: types.predictEval
      }),
      callPredict() {
        this.predict(this.inp);
      },
      mouseOverSpan(index) {
        Vue.set(this.active, index, true);
      },
      mouseLeaveSpan(index) {
        Vue.set(this.active, index, false);
      }
    },
    computed: {
      ...mapGetters({
        calcData: types.GET_MAPPED_PREDICTION,
        loading: types.IS_LOADING
      })
    },
    watch: {
      calcData(newVal) {
        this.active = Array(Object.keys(newVal).length).fill(false);
      }
    }

  }

</script>
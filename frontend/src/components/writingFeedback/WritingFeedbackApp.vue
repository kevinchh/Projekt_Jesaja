<template>
  <v-container>
    <v-row class="d-flex" justify-content="center">
      <v-col cols="12" md="6" align-self="start" :class="{'pb-15': $vuetify.breakpoint.mdAndDown, 'pb-0': $vuetify.breakpoint.lgAndUp}">
        <v-card class="rounded-xl" height = "395" style="border-bottom-left-radius: 6px !important; border-bottom-right-radius: 6px !important;">
          <v-textarea
            v-model = "inp"
            name="name"
            id="scroll"
            class="pl-3 pr-2 textarea__label"
            no-resize
            full-width
            height= 370
            loading = false
          >
            <template v-slot:label>
              <div class="headline mb-1">
                Enter or insert text here
              </div>
              <div style="white-space: normal; line-height: 1.3rem;" class="subtitle-1">
                After entering, press the CALCULATE button and the result will be presented to the right or below.
              </div>
            </template>
          </v-textarea>
          <v-card  height="50" style="transform: translate(0px, -8px); border-bottom-left-radius: 36px !important; border-bottom-right-radius: 36px !important;">
            <v-card-actions>
              <v-list-item class="grow">
                <v-row
                  align="center"
                  justify="end"
                >
                  <v-btn
                    rounded
                    color="blue-grey"
                    class="ma-2 white--text"
                    :dark="!!inp"
                    style="transform: translate(0px, -9px);"
                    :disabled = "!inp"
                    :loading="loading"
                    @click="callPredict"
                  >
                    Calculate
                    <v-icon
                      right
                      dark
                    >
                      mdi-play-network
                    </v-icon>
                  </v-btn>
                </v-row>
              </v-list-item>
            </v-card-actions>
          </v-card>
        </v-card>
      </v-col >
      <v-col cols="12" md="6">
          <v-card class="rounded-xl"  height = "450">
            <v-row v-if="loading" align-content="center" style="height: 100%">
              <v-col class="mx-4">
                <div>
                  <div :style = "{'text-align': 'center'}" >
                    Progressing your input
                  </div>
                  <v-progress-linear
                    color="success"
                    indeterminate
                    rounded
                    height="10"
                    width = "4"
                  ></v-progress-linear>
                </div>
              </v-col>
            </v-row>
            <div v-else class="pl-3 mt-4 mr-2" id="scroll" style="height: 420px; display: inline-block; overflow: auto;">
              <span
                v-for="(val, idx) in calcData"
                :key="idx"
                @mouseover="mouseOverSpan(idx)"
                @mouseleave="mouseLeaveSpan(idx)"
                :style = "{
                  'background-color': active[idx] ? val.color.hover : val.color.light,
                  'border-radius': '20px',
                  'text-align': 'left',
                  'padding': '3px 2px 3px',
                  'height': '430px',
                  'overflow': 'auto'}">

                <v-tooltip v-if="val.queryName !== 'O'" top>
                  <template v-slot:activator="{ on, attrs }">
                    <v-chip
                      v-bind="attrs"
                      v-on="on"
                      dark
                      small
                      :color="val.color.dark">{{getIdByQueryName[val.queryName]}}</v-chip>
                  </template>
                  <span>{{val.queryName}}</span>
                </v-tooltip>
                {{val.text}}
              </span>
            </div>
          </v-card>
      </v-col>
    </v-row>
    <v-row>
    <v-col cols="12">
      <v-expansion-panels :value="0">
        <v-expansion-panel class="rounded-xl" open>
          <v-expansion-panel-header style="background: #eee">
            <span style="font-weight: bold">Legend</span>
          </v-expansion-panel-header>
          <v-expansion-panel-content>
            <template v-for="(k,i) in color_code">
              <span :key="i+'x'" style="display: inline-block">
                <span :key="i+'l'" style="white-space: nowrap">
                  <v-chip
                    v-if="i !== 'O'"
                    :key="i"
                    dark
                    small
                    :color="k.dark">{{getIdByQueryName[i]}}</v-chip>
                        {{i !== 'O' ? '-' : ''}}
                  <span
                    v-if="i !== 'O'"
                    :key="i+'a'"
                    :style = "{'font-weight': 'bold', 'margin-right': '40px'}">
                    {{i}}
                  </span>
                </span>
              </span>
            </template>
          </v-expansion-panel-content>
        </v-expansion-panel>
      </v-expansion-panels>
    </v-col>
    </v-row>
  </v-container>
</template>

<script>
import Vue from 'vue';
import { mapActions, mapGetters } from 'vuex';
import * as types from '../../store/types';
import { colorCode, getIdByQueryName } from '../../const/evaluationTypes';


  export default {
    name: 'WritingFeedbackApp',
    components : {
    },

    data: () => ({
      color_code: colorCode,
      inp: "",
      exampleText: "Furthermore, asking for multiple opinions can benifit during competitions for a position slot, as cadidates needs to make decisions on what they need to say or do. For example, it can be helpful in situations like elections, both for the U.S. or simply in school. If a student is running for a position in office to represent his/her school, he/she can ask a widespread and diverse audience. First, asking other students is their best bet to obtaining information. Other students can inform him/her about what they want, like better water fountains, recess, or healthier food. Then, the student running can make changes to the way they run for the election, and on his/her speech, take a different approach. In addition, if the student running asks an adult, they will get to know a more realistic way the school can be improved. Since a student, even as a student officer, isn't able to make a significant change to a school, they can inform the school board about ways to make the school better.",
      active: [],
      getIdByQueryName: getIdByQueryName,
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
      },
      onResize () {
        this.isMobile = window.innerWidth < 600
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

<style>
  #scroll::-webkit-scrollbar {
    width: 8px;
    background-color: #F5F5F5;
  }

  #scroll::-webkit-scrollbar-thumb {
    -webkit-box-shadow: inset 0 0 3px rgba(0,0,0,0.3);
    border-radius: 10px;
    background-color: #D5D5D5;
  }

  .textarea__label > .v-input__control > .v-input__slot > .v-text-field__slot > label {
    height: 100% !important;
  }
</style>

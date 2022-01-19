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
            <span v-for="i in entities" :key="i.text" :style = "{ 'color': i.color, 'text-align': 'left' }">
              {{i.text}}
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
          @click="predict">
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

  // Vue.component('main-table', {
  //   template: "<ul>" +
  //     "<li v-for='(set, index) in settings'>" +
  //     "{{index}}) " +
  //     "{{set.title}}" +
  //     "<button @click='changeSetting(index)'> Info </button>" +
  //     "</li>" +
  //     "</ul>",
  //   props: ['settings'],
  //   methods: {
  //     changeSetting(value) {
  //       this.$emit('change', value);
  //     },
  //   },
  // });

  export default {
    name: 'HelloWorld',
    components : {
  },

    data: () => ({
      queries: ['O', 'Lead', 'Position', 'Claim', 'Counterclaim', 'Rebuttal', 'Evidence', 'Concluding Statement'],
      color_code: {'O':"#595446", 'Lead':"#967a2c", 'Position':"#95962c", 'Claim':"#76962c", 'Counterclaim':"#2c3d20", 'Rebuttal':"#203d2c",
       'Evidence':"#21b59f", 'Concluding Statement':"#13303b"},
      entities: [],
      inp: "Furthermore, asking for multiple opinions can benifit during competitions for a position slot, as cadidates needs to make decisions on what they need to say or do. For example, it can be helpful in situations like elections, both for the U.S. or simply in school. If a student is running for a position in office to represent his/her school, he/she can ask a widespread and diverse audience. First, asking other students is their best bet to obtaining information. Other students can inform him/her about what they want, like better water fountains, recess, or healthier food. Then, the student running can make changes to the way they run for the election, and on his/her speech, take a different approach. In addition, if the student running asks an adult, they will get to know a more realistic way the school can be improved. Since a student, even as a student officer, isn't able to make a significant change to a school, they can inform the school board about ways to make the school better.",
      out: "O Lead Position",
      loading: false
    }),
    methods: {
      set_entities(data){
        let words = data["input"][0].split(" ")
        for(let i in data["out_dict"]){
          let temp ={}
          temp.text = words.slice(parseInt(i), data["out_dict"][i][0] + 1).join(" ")
          temp.color = this.color_code[data["out_dict"][i][1]]
          this.entities.push(temp)
        }
        this.loading = false
      },
      predict(){
        this.entities = []
        this.loading = true
        fetch("http://localhost:7000/predict", {
          method: "POST",
          headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({"1":this.inp})
        }).then((res) => res.json())
        //.then(data => console.log(data))
        .then(data => this.set_entities(data))
        .catch(err => console.error("Failed to load: ",err))
      }
    },
    computed: {
    }

  }

</script>

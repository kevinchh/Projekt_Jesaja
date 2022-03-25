<template>
  <div>
    <v-parallax fluid dark src="../../../data/banner2.png"
    :style = "{'text-align': 'center','height': '600px','color': 'white'}">
      <div class="pt-16" :style = "{'color': '#f7f6f2'}">
        APPLY MACHINE LEARNING TO SUPPORT EVERYDAY PROBLEM SOLVING
      </div>
      <div class="pt-6" :style = "{'font-size': 'xx-large', 'font-weight': 'bold'}">
        LEVERAGE PUBLIC DATA TO FUEL INNOVATION
      </div>
      <div class="py-6" :style = "{'color': '#f7f6f2', 'width': '70%', 'margin':'auto'}">
        We apply machine learning algorithms in order to support problem solving and decision making affecting many different people in everyday life.
        These machine learning algorithms are integrated in simple-to-use webmasks. Furthermore an explanation for every model
        used in our use cases is provided. Have a look at our portfolio and convince yourself!
      </div>
      <div class="pt-16" :style = "{'margin':'auto'}">
        <v-btn rounded color="#6d756f" dark @click="bottom">
          GET TO KNOW US
        </v-btn>
      </div>
    </v-parallax>
    <v-container>
      <v-row>
        <v-col cols="3"></v-col>
        <v-col cols="6">
          <h1 :style = "{'text-align': 'center','margin-top': '100px','margin-bottom': '20px'}">
            Implementations
          </h1>
        </v-col>
        <v-col cols="3"></v-col>
      </v-row>
    </v-container>
    <v-item-group active-class="primary">
    <v-container>
      <v-row justify="center" align="center">
        <v-col v-for="n in 3" :key="n" cols="12" md="4" >
          <CardComponent title="Feedback Evaluation" />
        </v-col>
      </v-row>
    </v-container>
  </v-item-group>
  <v-container>
    <div class="pt-6" :style = "{'font-size': 'xx-large', 'font-weight': 'bold', 'margin':'auto', 'text-align': 'center', 'margin-top': '20%', 'margin-bottom': '5%'}">
      Who are we?
    </div>
    <v-row :style = "{'padding-bottom': '10%'}">
      <v-col cols= "6">
        <v-card class="mx-auto" max-width="344" outlined color="transparent">
          <v-img src="../../../data/kc.jpeg" height="400px" contain></v-img>
          <v-card-title>
            Kevin Chhoeu
          </v-card-title>
          <v-card-subtitle>
            M. Sc. Computer Science
          </v-card-subtitle>
          <v-card-actions>
            <v-btn color="orange lighten-2" text>
              Get my CV
            </v-btn>
            <v-spacer></v-spacer>
            <v-btn icon @click="show_k = !show_k">
              <v-icon>{{ show_k ? 'mdi-chevron-up' : 'mdi-chevron-down' }}</v-icon>
            </v-btn>
          </v-card-actions>
          <v-expand-transition>
            <div v-show="show_k">
              <v-divider></v-divider>
              <v-card-text>
                I'm a graduate student from the RWTH Aachen University. I'm passionate about everything related to data and process optimization. Contact me @kevin.chhoeu22@gmail.com!
              </v-card-text>
            </div>
          </v-expand-transition>
        </v-card>
      </v-col>
      <v-col cols= "6">
        <v-card class="mx-auto" max-width="344" outlined color="transparent">
          <v-img src="../../../data/banner2.png" height="400px" contain></v-img>
          <v-card-title>
            Mark Christy Georgy
          </v-card-title>
          <v-card-subtitle>
            B. Sc. Computer Science
          </v-card-subtitle>
          <v-card-actions>
            <v-btn color="orange lighten-2" text>
              Get my CV
            </v-btn>
            <v-spacer></v-spacer>
            <v-btn icon @click="show_m = !show_m">
              <v-icon>{{ show_m ? 'mdi-chevron-up' : 'mdi-chevron-down' }}</v-icon>
            </v-btn>
          </v-card-actions>
          <v-expand-transition>
            <div v-show="show_m">
              <v-divider></v-divider>
              <v-card-text>
                I'm a graduate student from the RWTH Aachen University. I'm passionate about everything related to data and process optimization. Contact me @kevin.chhoeu22@gmail.com!
              </v-card-text>
            </div>
          </v-expand-transition>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
  </div>
</template>

<script>
import CardComponent from '../CardComponent';

export default {
  name: 'MainPage',
  components: {
    CardComponent
  },
  methods: {
    bottom(){
      window.scrollTo({
        top: document.body.scrollHeight,
        left: 0,
        behavior: 'smooth'
        });
    }
  },
  data: () => ({
      show_k: false,
      show_m: false,
    })
}
</script>

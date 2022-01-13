<template>
  <v-container>
    <v-row class="text-center">
      <v-col cols="12">
        <h1>Hallo Kevin</h1>
      </v-col>
      <v-col cols="12">
        <v-textarea
          v-model = "inp"
          name="name"
          label="Test Eingabe"
          id="id"
          outlined
        ></v-textarea>
      </v-col>
      <v-btn
        color="blue-grey"
        class="ma-2 white--text"
        fab
        @click="predict">
        <v-icon dark>
          mdi-cloud-upload
        </v-icon>
      </v-btn>
      <p>Message is: {{ inp }}</p>
    </v-row>
  </v-container>
</template>

<script>
  export default {
    name: 'HelloWorld',

    data: () => ({
      inp: ""
    }),
    methods: {
      predict(){
        fetch("http://localhost:7000/predict", {
          method: "POST",
          headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({"1":this.inp})
        }).then((res) => console.log(res))
        .catch(err => console.error("Failed to load: ",err))
        /* fetch("http://localhost:7000/", {
          method: "GET"
        }).then(res => console.log(res)) */
      }
    }
  }
</script>
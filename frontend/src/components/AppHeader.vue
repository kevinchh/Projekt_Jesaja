<template>
  <div class="background">
    <v-container class="pb-0">
      <v-row class="text-start mt-2">
        <v-col cols="12">
          <div class="display-2 font-weight-light">{{title}}</div>
        </v-col>
      </v-row>
      <v-row>
        <v-col>
          <v-btn
            v-for="cur in size"
            :key="cur"
            class="my-2 rounded-lg"
            x-large
            dark
            color="blue-grey darken-2"
            :plain="cur !== active"
            @click="onActiveButton(cur)"
          >
          {{buttonTexts[cur-1]}}
          </v-btn>
        </v-col>
      </v-row>
    </v-container>
    <template v-for="cur in size">
      <div v-if="cur === active" :key="getKey(cur+1)">
        <slot :name="getKey(cur)" />
      </div>
    </template>
  </div>
</template>

<script>
export default {
  name: 'AppHeader',
  props: {
    title: {
      // title text
      type: String,
      required: true
    },
    size: {
      // how many buttons are needed
      type: Number,
      required: true
    },
    buttonTexts: {
      // specify for each button the text in an array
      type: Array,
      required: true
    }
  },
  data: () => ({
    active: 1
  }),
  methods: {
    getKey(cur) {
      return `button${cur}`;
    },
    onActiveButton(cur) {
      this.active = cur;
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
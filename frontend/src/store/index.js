import Vue from 'vue';
import Vuex from 'vuex';

import evaluation from './modules/evaluation';

Vue.use(Vuex);

export const store = new Vuex.Store({
    state: {},
    getters: {},
    mutations: {},
    actions: {},
    modules: {
        evaluation
    }
});
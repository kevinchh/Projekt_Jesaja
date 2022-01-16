import axios from 'axios';

import * as types from '../types';

axios.defaults.baseURL = 'http://localhost:7000';

const defaultState = () => ({
    loading: false,
    prediction: {}
});

const state = defaultState();

const getters = {
    [types.GET_PREDICTIONS]: (state) => state.prediction
}

const mutations = {
    [types.SET_LOADING]: (state, payload) => {
        state.loading = payload;
    },
    [types.SET_PREDICTIONS]: (state, payload) => {
        state.prediction = payload;
    }
};

const actions = {
    async [types.predictEval]({commit}, payload) {
        let response;
        try {
            commit(types.SET_LOADING, true);
            // get predictions
            response = await axios.post('/predict', {"1":payload});
        } catch (error) {
            console.error(`POST Error: localhost:7000/predict`, error);
        } finally {
            console.log("From Store", response.data);
            commit(types.SET_PREDICTIONS, response.data);
            commit(types.SET_LOADING, false);
        }
    }
};

export default {
    state,
    getters,
    mutations,
    actions
};
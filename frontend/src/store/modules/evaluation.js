import axios from 'axios';

import * as types from '../types';
import { colorCode } from '../../const/evaluationTypes';

axios.defaults.baseURL = 'http://localhost:7000';

const defaultState = () => ({
    loading: false,
    prediction: {}
});

const state = defaultState();

const getters = {
    [types.GET_PREDICTIONS]: (state) => state.prediction,
    [types.GET_MAPPED_PREDICTION]: (state) => {
        if (Object.keys(state.prediction).length === 0) {
            return {}
        }

        const words = state.prediction ? state.prediction.input[0].split(" ") : [];
        return Object.entries(state.prediction["out_dict"]).map(value => {
            return {
                text: words.slice(parseInt(value[0]), value[1][0] + 1).join(" "),
                color: colorCode[value[1][1]]
            };
        });
    },
    [types.IS_LOADING]: (state) => state.loading

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
            commit(types.SET_PREDICTIONS, response.data);
        } catch (error) {
            console.error(`POST Error: localhost:7000/predict`, error);
        } finally {
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

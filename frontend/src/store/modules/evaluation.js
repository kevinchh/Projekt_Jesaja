// import axios from 'axios';

import * as types from '../types';

//axios.defaults.baseURL = 'hhtp://localhost:7000';

const defaultState = () => ({
    prediction: {},
    lastInput: {}
});

const state = defaultState();

const getters = {
    [types.GET_PREDICTIONS]: (state) => state.prediction;
}
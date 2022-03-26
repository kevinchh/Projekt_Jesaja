import Vue from 'vue';
import VueRouter from 'vue-router';
import { ROUTE_NAMES } from './routerNames';

import WritingFeedbackComp from '../components/writingFeedback/WritingFeedbackComp';
import MainPage from '../components/mainPage/mainPage';

Vue.use(VueRouter);

const routes = [
    {
        path: '/eval',
        name: ROUTE_NAMES.EVAL,
        component: WritingFeedbackComp
    },
    {
        path: '/',
        name: ROUTE_NAMES.MAIN,
        component: MainPage
    },
    { path: '*', redirect: { name: ROUTE_NAMES.MAIN}}
];

const router = new VueRouter({
    mode: 'history',
    routes
});

export default router;

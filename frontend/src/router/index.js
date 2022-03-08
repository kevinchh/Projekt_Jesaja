import Vue from 'vue';
import VueRouter from 'vue-router';
import { ROUTE_NAMES } from './routerNames';

import WritingFeedbackComp from '../components/writingFeedback/WritingFeedbackComp';

Vue.use(VueRouter);

const routes = [
    {
        path: '/eval',
        name: ROUTE_NAMES.EVAL,
        component: WritingFeedbackComp
    },
    { path: '*', redirect: { name: ROUTE_NAMES.EVAL}}
];

const router = new VueRouter({
    mode: 'history',
    routes
});

export default router;
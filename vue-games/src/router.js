import { createWebHistory, createRouter  } from 'vue-router';

import AnagramHuntView from './views/AnagramHuntView.vue';
import MathFactsView from './views/MathFactsView.vue';

const routes = [
    {
        path: '/games/anagram-hunt',
        name: 'AngramHuntView',
        component: AnagramHuntView
    },
    {
        path: '/games/math-facts',
        name: 'MathFactsView',
        component: MathFactsView
    },
]

const router = createRouter({
    history: createWebHistory(),
    routes: routes,
});

export default router;
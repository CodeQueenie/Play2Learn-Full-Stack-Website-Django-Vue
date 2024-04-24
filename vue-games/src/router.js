import { createWebHistory, createRouter  } from 'vue-router';

import AnagramHuntView from './views/AnagramHuntView.vue';
import HomeView from './views/HomeView.vue';
import MathFactsView from './views/MathFactsView.vue';
import GameConfig from './components/math-facts-practice/GameConfig.vue';
import GamePlay from './components/math-facts-practice/GamePlay.vue';

const routes = [
    {
        path: '/',
        name: 'HomeView',
        component: HomeView
    },
    {
        path: '/games/anagram-hunt',
        name: 'AngramHuntView',
        component: AnagramHuntView
    },
    {
        path: '/games/math-facts',
        name: 'MathFactsView',
        component: MathFactsView,
        children: [
            {
                path: '',
                name: 'GameConfig',
                component: GameConfig,
            },
            {
                path: '/play',
                name: 'GamePlay',
                component: GamePlay,
                props: (route) => ({
                    operation: route.query.operation,
                    maxNumber: route.query.maxNumber
                }),
            },
        ],
    },
]

const router = createRouter({
    history: createWebHistory(),
    routes: routes,
});

export default router;
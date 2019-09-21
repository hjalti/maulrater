import Vue from 'vue'
import Vuex from 'vuex'
import { getRestaurants, submitRating } from './api'

Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        restaurants: [],
    },
    getters: {
        restaurantById: (state) => (id) => {
            return state.restaurants.find(r => r.id === id)
        }
    },
    mutations: {
        updateRestaurants(state, restaurants) {
            state.restaurants = restaurants;
        },
        addRating(state, payload) {
            var r = state.restaurants.find(r => r.id === payload.restaurant.id)
            if (r) {
                r.av_rating = (r.av_rating * r.rating_count + payload.rating) / (r.rating_count + 1)
                r.rating_count += 1
            }
        },
    },
    actions: {
        async fetchRestaurants({ commit }) {
            commit('updateRestaurants', (await getRestaurants()).data)
        },
        async rateRestaurant({ commit, getters }, payload) {
            commit('addRating', payload)
            await submitRating(payload.restaurant.id, payload.rating)
        }
    }
})

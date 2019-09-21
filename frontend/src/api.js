import axios from 'axios';

let API = 'http://127.0.0.1:1337/api'
if (process.env.NODE_ENV === 'production') {
    API = `http://${window.location.hostname}:1337/api`
}

function getRestaurants() {
    return axios.get(`${API}/restaurants/`)
    return new Promise(resolve => setTimeout(
        _ => resolve({'data': [
            {
                'name': 'Bergson Mathús',
                'id': 1,
                'av_rating': 1.9,
                'rating_count': 10,
            },
            {
                'name': 'Local',
                'id': 2,
                'av_rating': 0.9,
                'rating_count': 5,
            },
        ]}), 2000
    ));
}

function submitRating(restaurant, rating) {
    return axios.post(`${API}/ratings/create/`,
        {
            'rating': rating,
            'restaurant_id': restaurant,
        }).catch(err => {
            console.log(err.response)
        })
    return new Promise(resolve => setTimeout(
        _ => resolve([
            {
                'name': 'Bergson Mathús',
                'id': 1,
                'av_rating': 1.3,
                'rating_count': 10,
            },
            {
                'name': 'Local',
                'id': 2,
                'av_rating': 0.3,
                'rating_count': 5,
            },
        ]), 2000
    ));
}

export { getRestaurants, submitRating };

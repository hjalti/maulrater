<template>
  <div class="wrapper">
    <div id="nav">
      <div class="header">
        Restaurant Overview
      </div>
      <div>
        <dropdown :items="sorters" title="Order by" @selected="selectSort"/>
      </div>
    </div>
    <RestaurantItem v-for="item in restaurants" :key="item.id" :restaurant="item" @click.native="choose(item)"/>
  </div>
</template>

<script>
import RestaurantItem from '@/components/RestaurantItem.vue'
import Dropdown from '@/components/Dropdown.vue'
import _ from 'lodash'

var sorters = [
  {
    name: 'Number of ratings',
    sorter(list) { return _.sortBy(list, [r => -r.rating_count, 'name'])},
  },
  {
    name: 'Rating',
    sorter(list) { return _.sortBy(list, [r => -r.av_rating, 'name'])},
  },
  {
    name: 'Alphabetical',
    sorter(list) { return _.sortBy(list, ['name'])},
  },
]

export default {
  name: 'RestaurantOverview',
  data() {
    return {
      sorters: sorters,
      selectedSorter: sorters[0],
    }
  },
  methods: {
    choose(item) {
      this.$router.push({ name: 'rate', params: { id: item.id } })
    },
    selectSort(sorter) {
      this.selectedSorter = sorter
    },
  },
  computed: {
    restaurants() {
      return this.selectedSorter.sorter(this.$store.state.restaurants)
    },
  },
  components: {
    RestaurantItem,
    Dropdown,
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
#nav {
  display: flex;
  align-items: center;
  justify-content: space-between;

  padding: 40px 20px;

  .header {
    font-size: 40px;
    font-weight: bold;
  }
}
</style>

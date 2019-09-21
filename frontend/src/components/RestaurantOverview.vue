<template>
  <div class="hello">
    <RestaurantItem v-for="item in restaurants" :key="item.id" :restaurant="item" @click.native="choose(item)"/>
  </div>
</template>

<script>
import RestaurantItem from '@/components/RestaurantItem.vue'

export default {
  name: 'HelloWorld',
  created() {
    this.fetchData()
  },
  methods: {
    fetchData() {
      this.$store.dispatch('fetchRestaurants')
    },
    choose(item) {
      this.$router.push({ name: 'rate', params: { id: item.id } })
    },
  },
  computed: {
    restaurants() {
      return this.$store.state.restaurants;
    },
  },
  components: {
    RestaurantItem
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
</style>

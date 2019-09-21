<template>
  <div>
    <div id="nav">
      <router-link to="/">Back</router-link>
    </div>
    <Rater :restaurant="restaurant" />
  </div>
</template>

<script>
import Rater from '@/components/Rater.vue'

export default {
  props: ['id'],
  name: 'rate',
  components: {
    Rater
  },
  computed: {
    restaurant() {
        return this.$store.getters.restaurantById(this.id)
    },
  },
}
</script>

<style scoped lang="scss">
#nav {
  text-align: right;
  padding: 30px;
  a {
    font-size: 25px;
    font-weight: bold;
    color: #2c3e50;
    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
</style>

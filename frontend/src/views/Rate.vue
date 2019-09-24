<template>
  <div>
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
  methods: {
    back() {
      this.$router.go(-1);
    },
  },
  computed: {
    restaurant() {
        return this.$store.getters.restaurantById(parseInt(this.id))
    },
  },
}
</script>

<style scoped lang="scss">
</style>

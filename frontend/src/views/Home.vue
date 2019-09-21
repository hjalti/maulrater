<template>
  <div class="home">
    <restaurant-overview />
  </div>
</template>

<script>
// @ is an alias to /src
import RestaurantOverview from '@/components/RestaurantOverview.vue'

export default {
  name: 'home',
  components: {
    RestaurantOverview
  }
}
</script>

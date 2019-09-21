<template>
  <div class="rest-item">
    <div class="name">
      {{ restaurant.name }}
    </div>
    <div class="rating">
      <star-rating
        :rating="extrapolatedRating"
        :round-start-rating="false"
        :read-only="true"
        :star-size="40"
        :show-rating="false"
      />
    </div>
  </div>
</template>

<script>
import StarRating from 'vue-star-rating'

export default {
  name: 'RestaurantItem',
  props: ['restaurant'],
  computed: {
    extrapolatedRating() {
      return this.restaurant.av_rating / 2.0 * 5
    },
  },
  components: {
    StarRating,
  }
}
</script>

<style scoped lang="scss">
.rest-item {
  display: flex;
  justify-content: space-between;
  padding: 30px 20px;

  &:hover {
    background-color: #1111;
  }

  .name {
    font-size: 24px;
  }
}
</style>

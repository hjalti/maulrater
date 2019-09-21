<template>
  <div class="wrapper">
    <div class="header">
      Rating: <i>{{ restaurant.name }}</i>
    </div>
    <div class="ratings-wrapper">
      <div class="ratings">
        <RateEmoji :rating="0" @click.native="rate(0)" :size="150"/>
        <RateEmoji :rating="1" @click.native="rate(1)" :size="150"/>
        <RateEmoji :rating="2" @click.native="rate(2)" :size="150"/>
      </div>
    </div>
  </div>
</template>

<script>
import RateEmoji from '@/components/RateEmoji.vue'

export default {
  name: 'Rater',
  props: ['restaurant'],
  methods: {
    rate(rating) {
      this.$store.dispatch('rateRestaurant', {'restaurant': this.restaurant, 'rating': rating})
      this.$router.push({ name: 'home' })
    },
  },
  components: {
    RateEmoji,
  },
}

</script>

<style scoped lang="scss">
.wrapper {
  .header {
    font-size: 30px;
    padding: 0px 30px;
  }
  .ratings-wrapper {
    display: flex;
    justify-content: center;
    align-items: center;

    .ratings {
      flex: 1 0 0;
      margin-top: 150px;
      display: flex;
      justify-content: space-around;

      div {
        padding: 70px;
      }

      .bad {
        color: red;
      }
      .good {
        color: green;
      }
    }
  }
}
</style>

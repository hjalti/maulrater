<template>
  <div>
    <div class="wrapper" v-if="restaurant">
      <div id="nav">
        <div class="header">
          Rating: <i>{{ restaurant.name }}</i>
        </div>
        <div class="back-btn" @click="back">Back</div>
      </div>
      <div class="ratings-wrapper">
        <div class="ratings">
          <RateEmoji :rating="0" @click.native="rate(0)" :size="150"/>
          <RateEmoji :rating="1" @click.native="rate(1)" :size="150"/>
          <RateEmoji :rating="2" @click.native="rate(2)" :size="150"/>
        </div>
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
    back() {
      this.$router.go(-1);
    },
  },
  components: {
    RateEmoji,
  },
}

</script>

<style scoped lang="scss">
.wrapper {
  #nav {
    display: flex;
    justify-content: space-between;
    padding: 40px 30px 10px 30px;
    align-items: baseline;

    .back-btn {
      border-radius: 0px;
      cursor: pointer;
      font-size: 25px;
      font-weight: bold;
      color: #777;

      background-color: inherit;
      border-width: 1px;
      border-color: #eee;
      border-style: solid;
      padding: 20px 45px;
    }
  }

  .header {
    font-size: 35px;
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

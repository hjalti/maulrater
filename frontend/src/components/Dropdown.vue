<template>
  <div class="wrapper" @mouseleave="close">
    <div class="title" @click="openDropdown">
      <div class="title-header">{{ title }}</div>
      <div>{{ selectedText }}</div>
    </div>
    <div class="list" v-show="open">
      <div class="item" v-for="item in items" @click="select(item)" :class="{selected: item == selected}">
        {{ item.name }}
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      open: false,
      selected: null
    }
  },
  created() {
    this.selected = this.items[0]
  },
  name: 'Dropdown',
  props: ['title', 'items'],
  methods: {
    openDropdown() {
      this.open = !this.open
    },
    select(item) {
      this.selected = item
      this.close()
      this.$emit('selected', item)
    },
    close() {
      this.open = false;
    },
  },
  computed: {
    selectedText() {
      if (!this.selected) {
        return "[Nothing selected]"
      }
      return this.selected.name
    },
  },
}

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
.wrapper {

  .title {
    font-size: 20px;
    width: 300px;
    border-style: solid;
    border-width: 1px;
    border-color: #eee;
    border-radius: 3px;
    padding: 15px 25px;

    .title-header {
      font-size: 15px;
      padding-bottom: 5px;
    }
  }

  .list{
    background-color: white;
    width: 350px;
    border-style: solid;
    border-width: 1px;
    border-color: #eee;
    position: absolute;

    .item {
      font-size: 25px;
      padding: 20px 15px;

      &:hover {
        background-color: #eee;
      }

      &.selected {
        font-weight: bold;
      }
    }
  }
  cursor: pointer;
  .header {
    display: flex;
  }

}
</style>

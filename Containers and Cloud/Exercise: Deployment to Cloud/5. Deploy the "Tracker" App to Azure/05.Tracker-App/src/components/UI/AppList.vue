<template>
  <ul class="q-list">
    <app-list-item
      @checkTodo="$emit('checkTodo', item.id)"
      @deleteTodoItem="$emit('deleteTodoItem', item.id)"
      v-for="item in items"
      :key="item"
      :todoItem="item"
    ></app-list-item>
  </ul>
</template>

<script>
import AppListItem from './AppListItem.vue'
export default {
  components: {
    AppListItem
  },
  props: {
    items: {
      type: Array,
      required: true
    }
  }
}
</script>

<style scoped>
.q-list {
  list-style: none;
}
</style>
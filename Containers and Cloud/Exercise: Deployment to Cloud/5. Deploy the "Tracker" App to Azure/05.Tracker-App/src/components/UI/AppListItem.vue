<template>
  <li class="q-list-item">
    <app-flex-container fluid>
      <app-flex-column :smCols="8" :mdCols="8" :lgCols="8" :xlCols="8">
        <h4
          class="q-list-item__title"
          :class="{ 'q-list-item__title--done': todoItem.done }"
        >{{ todoItem.title }}</h4>
        <p
          class="q-list-item__description"
          :class="{ 'q-list-item__description--done': todoItem.done }"
        >{{ todoItem.description }}</p>
      </app-flex-column>
      <app-flex-column class="q-flex-center" :smCols="4" :mdCols="4" :lgCols="4" :xlCols="4">
        <app-button
          fluid
          :variant="todoItem.done ? 'warning' : 'success'"
          @click="$emit('checkTodo')"
        >
          <i v-if="!todoItem.done" class="fas fa-check"></i>
          <i v-else class="fas fa-undo"></i>
        </app-button>
        <app-button v-if="todoItem.done" fluid variant="error" @click="$emit('deleteTodoItem')">
          <i class="far fa-trash-alt"></i>
        </app-button>
      </app-flex-column>
    </app-flex-container>
  </li>
</template>

<script>
import AppFlexContainer from '../Layout/AppFlexContainer.vue'
import AppFlexColumn from '../Layout/AppFlexColumn.vue'
import AppButton from '../Form/AppButton.vue'

export default {
  components: {
    AppFlexContainer,
    AppFlexColumn,
    AppButton
  },
  props: {
    todoItem: {
      type: Object,
      properties: {
        title: {
          type: String, required: true
        },
        description: {
          type: String, required: true
        },
        done: {
          type: Boolean, required: true
        }
      }
    }
  }
}
</script>

<style scoped>
.q-list-item {
  margin: var(--gap-sm) 0;
  padding: var(--gap-md) 0;
  background-color: var(--background-color-tartiary);
  border-radius: var(--gap-xxs);
  border: 1px solid var(--accent-color-primary);
  color: var(--text-color-secondary);
}

.q-list-item__title {
  font-size: var(--text-size-lg);
}
.q-list-item__title,
.q-list-item__description {
  margin: var(--gap-sm) 0;
}

.q-list-item__title--done {
  text-decoration: line-through;
}

.q-list-item__description--done {
  opacity: 0.25;
}
</style>
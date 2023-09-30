<template>
  <form class="q-todo-form" @submit="onFormSubmit">
    <app-input-group border title="Keep track of your daily duties">
      <app-flex-container>
        <app-flex-column>
          <app-input
            :required="true"
            v-model="todoModel.title"
            label="Enter a title ..."
            labelPrefix="Please "
          ></app-input>
          <app-text-area
            v-model="todoModel.description"
            label="Enter a description ..."
            labelPrefix="Please "
          ></app-text-area>
          <app-button class="q-button--fluid" type="submit" label="Add todo"></app-button>
          <app-button
            class="q-button--fluid"
            @click="onFormReset"
            type="button"
            variant="link"
            label="Reset Form"
          ></app-button>
        </app-flex-column>
      </app-flex-container>
    </app-input-group>
  </form>
  <app-list
    @deleteTodoItem="onDeleteTodoItem($event)"
    @checkTodo="onCheckTodo($event)"
    :items="todoListSortedByDone"
  ></app-list>
</template>

<script>
import { reactive } from 'vue'
import AppFlexContainer from '../components/Layout/AppFlexContainer.vue'
import AppFlexColumn from '../components/Layout/AppFlexColumn.vue'
import AppInput from '../components/Form/AppInput.vue'
import AppTextArea from '../components/Form/AppTextArea.vue'
import AppButton from '../components/Form/AppButton.vue'
import AppList from '../components/UI/AppList.vue'
import AppInputGroup from '../components/Form/AppInputGroup.vue'
import useTodos from '../../store/todo';

export default {
  setup() {
    const todoModel = reactive({
      title: '',
      description: '',
      done: false
    })
    const { getters: { todoListSortedByDone }, actions: { addTodoItem, updateTodoDone, deleteTodoItem } } = useTodos();

    const onFormSubmit = (ev) => {
      ev.preventDefault();
      addTodoItem(todoModel);
      onFormReset();
    }

    const onFormReset = () => {
      todoModel.title = '';
      todoModel.description = '';
    }

    const onCheckTodo = (todoId) => updateTodoDone(todoId)

    const onDeleteTodoItem = (todoId) => deleteTodoItem(todoId)

    return { onFormSubmit, onFormReset, onCheckTodo, onDeleteTodoItem, todoListSortedByDone, todoModel }
  },
  components: {
    AppInput,
    AppButton,
    AppFlexContainer,
    AppFlexColumn,
    AppTextArea,
    AppList,
    AppInputGroup
  }
}
</script>

<style scoped>
.q-todo-form {
  padding: var(--gap-max) 0;
}

@media (max-width: 768px) {
  .q-button--fluid {
    width: 100%;
  }
}
</style>
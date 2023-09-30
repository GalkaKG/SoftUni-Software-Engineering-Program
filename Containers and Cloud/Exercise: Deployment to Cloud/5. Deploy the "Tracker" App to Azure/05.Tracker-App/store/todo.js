import { ref, computed } from 'vue';
import uuid from '../use/uuid';

import {
  SET_ACTIVE_TODO,
  ADD_TODO,
  DELETE_TODO,
  UPDATE_TODO,
} from './todo.types.js';

export default function useTodos() {
  const commit = (type, payload) => {
    return mutations[type](payload);
  };

  const state = {
    todoList: ref([
      {
        id: uuid(),
        title: 'Learn Vue.js',
        description:
          'Learn the basic concepts, such as components, directives and reactivity.',
        done: true,
      },
      {
        id: uuid(),
        title: 'Learn Docker 🐋',
        description:
          'Take the first step to get the basics of containerized applications',
        done: true,
      },
      {
        id: uuid(),
        title: 'Vue + Docker = 🚀',
        description:
          'Learn how to create, manage, run and deploy a Vue app with Docker containers.',
        done: false,
      },
    ]),
    todoActive: ref({}),
  };

  const getters = {
    todoList: computed(() => state.todoList.value),
    todoActive: computed(() => state.todoActive.value),
    todoListSortedByDone: computed(() => {
      return state.todoList.value.sort((current, next) => {
        return current.done === next.done ? 0 : current.done ? 1 : -1;
      });
    }),
  };

  const mutations = {
    SET_ACTIVE_TODO: ({ payload }) => {
      state.todoActive.value = { ...payload };
    },
    ADD_TODO: ({ payload }) => {
      state.todoList.value.push({ ...payload });
    },
    DELETE_TODO: ({ id }) => {
      state.todoList.value = state.todoList.value.filter((todo) => {
        return todo.id !== id;
      });
    },
    UPDATE_TODO: ({ payload }) => {
      state.todoList.value.map((todo) => {
        if (todo.id === payload.id) {
          todo = { ...payload };
        }
      });
    },
  };

  const actions = {
    setActiveTodo: (payload) => {
      commit(SET_ACTIVE_TODO, { payload });
    },
    addTodoItem: (payload) => {
      payload.id = uuid();
      commit(ADD_TODO, { payload });
    },
    deleteTodoItem: (id) => {
      commit(DELETE_TODO, { id });
    },
    updateTodoText: (payload) => {
      commit(UPDATE_TODO, { payload });
    },
    updateTodoDone: (id) => {
      let todoItem = state.todoList.value.find((todo) => todo.id === id);
      todoItem.done = !todoItem.done;

      commit(UPDATE_TODO, { payload: todoItem });
    },
  };

  return { actions, getters };
}

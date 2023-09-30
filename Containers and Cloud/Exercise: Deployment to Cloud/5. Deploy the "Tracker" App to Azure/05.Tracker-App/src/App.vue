<template>
  <main>
    <app-navbar></app-navbar>
    <app-flex-container>
      <app-flex-column></app-flex-column>
      <app-flex-column :smCols="12" :mdCols="8" :lgCols="6" :xlCols="4">
        <app-todos />
      </app-flex-column>
      <app-flex-column></app-flex-column>
    </app-flex-container>
  </main>
</template>

<script>
import AppFlexContainer from './components/Layout/AppFlexContainer.vue'
import AppFlexColumn from './components/Layout/AppFlexColumn.vue'
import AppNavbar from './components/UI/AppNavbar.vue'
import AppTodos from './views/AppTodos.vue'


export default {
  components: {
    AppTodos,
    AppNavbar,
    AppFlexContainer,
    AppFlexColumn
  }
}
</script>

<style>
@import url("./assets/css/main.css");

/* Globally valid styles */
a {
  color: var(--accent-color-primary);
}

.q-flex-center {
  display: flex;
  align-items: center;
  justify-content: center;
}
</style>

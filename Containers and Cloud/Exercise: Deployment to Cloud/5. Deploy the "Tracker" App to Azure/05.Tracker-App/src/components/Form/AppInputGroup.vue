<template>
  <section class="q-input-group-wrapper" :class="{
    'q-input-group-border': border,
  }">
    <fieldset class="q-input-group">
      <legend class="q-input-group-legend" v-if="title">{{ title }}</legend>
      <slot />
    </fieldset>
  </section>
</template>

<script>
export default {
  props: {
    title: {
      type: String,
    },
    border: {
      type: Boolean,
      default: false
    }
  }
}
</script>

<style scoped>
.q-input-group-wrapper {
  background-color: var(--background-color-tartiary);
}
.q-input-group-legend {
  width: 100%;
  text-align: center;
  font-size: var(--text-size-lg);
  font-weight: 600;
}

.q-input-group {
  padding: var(--gap-xl) 0;
  color: var(--accent-color-primary);
  width: 100%;
  margin: auto;
  border: none;
}

.q-input-group-border {
  border: 1px solid var(--accent-color-primary);
  border-radius: var(--gap-xs);
}

.q-input-group-border > .q-input-group > .q-input-group-legend {
  color: var(--white-color);
  background-color: var(--accent-color-primary);
  padding: var(--gap-md) var(--gap-lg);
}
</style>
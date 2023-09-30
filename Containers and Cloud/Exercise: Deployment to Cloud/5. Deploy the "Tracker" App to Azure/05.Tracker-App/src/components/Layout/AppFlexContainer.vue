<template>
  <div
    class="q-flex"
    :class="{
      'q-flex-fluid': fluid === true,
      'q-flex-full-page': onepager === true,
    }"
  >
    <slot />
  </div>
</template>

<script>
export default {
  props: {
    fluid: {
      type: Boolean,
      required: false,
      default: false,
    },
    onepager: {
      type: Boolean,
      required: false,
      default: false,
    },
  },
};
</script>

<style scoped>
.q-flex {
  margin: auto;
  width: 95%;
  display: flex;
  flex-wrap: wrap;
}

.q-flex-fluid {
  width: 100%;
}

.q-flex-full-page {
  height: 100vh;
  align-items: center;
  justify-content: center;
}
</style>
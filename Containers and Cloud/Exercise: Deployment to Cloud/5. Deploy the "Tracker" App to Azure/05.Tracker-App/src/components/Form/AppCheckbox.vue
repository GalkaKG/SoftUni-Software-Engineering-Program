<template>
  <input
    type="checkbox"
    class="q-input-base"
    :class="{
      'q-error': !!error,
      'q-input-switch': variant === 'switch',
    }"
    v-bind="$attrs"
    @change="$emit('update:modelValue', $event.target.checked)"
    :checked="modelValue"
    :id="id"
    :required="required"
    :aria-label="label"
    :aria-required="required"
    :aria-checked="modelValue"
    :aria-describedby="error ? `${id}-error` : null"
    :aria-invalid="error ? true : null"
  />
  <label
    v-if="label"
    :for="id"
    class="q-input-label"
    :class="{
      'q-input-label-switch': variant === 'switch',
    }"
  >
    <!-- Switch variant hides the input and replaces it with a custom element -->
    <span v-if="variant === 'switch'" class="q-switch" :class="{ 'q-switch-active': modelValue }">
      <div class="q-switch-toggle" :class="{ 'q-switch-toggle-checked': modelValue }"></div>
    </span>
    <!-- /Switch variant -->
    <span :class="{ 'q-input-label-flex': variant === 'switch' }" v-html="label"></span>
  </label>
  <span class="q-input-required-sign" v-if="required">{{ requiredSign }}</span>
</template>

<script>
import uuid from "../../../use/uuid";


export default {
  setup() {
    const id = uuid();
    return { id }
  },
  props: {
    label: {
      type: String,
      default: "",
    },
    modelValue: {
      type: Boolean,
      default: false,
    },
    variant: {
      type: String,
      default: "checkbox",
      validator(value) {
        return value === "checkbox" || value === "switch";
      },
    },
    error: {
      type: String,
      default: "",
    },
    required: {
      type: Boolean,
      default: false,
    },
    requiredSign: {
      type: String,
      default: "*",
    },
  }
}
</script>

<style scoped>
.q-input-base,
.q-input-label {
  font-size: var(--text-size-sm);
}

.q-input-label {
  color: var(--accent-color-primary);
  font-size: var(--text-size-sm);
  font-weight: 600;
}

.q-input-required-sign {
  color: var(--color-error);
}

.q-input-base {
  background-color: transparent;
  color: var(--text-color-primary);
  caret-color: var(--text-color-primary);
  border: none;
  border-bottom: var(--gap-xxs) solid transparent;
  padding: var(--gap-sm) var(--gap-xs);
  margin: var(--gap-sm);
}

.q-input-base:focus {
  outline: none;
  transition: var(--duration-quickest);
  border-bottom: var(--gap-xxs) solid var(--accent-color-primary);
}

.q-input-base:focus.q-error {
  border-bottom: var(--gap-xxs) solid var(--color-error);
}

.q-input-error-msg {
  font-size: var(--text-xs);
  color: var(--color-error);
}

/* Style for switch toggle */
.q-input-switch {
  display: none;
}

.q-switch {
  transition: all var(--duration-quick);
  background: var(--text-color-primary);
  border: calc(var(--el-size-xxs) * 0.025) solid var(--black-color);
  border-radius: var(--el-size-xxs);
  cursor: pointer;
  height: calc(var(--el-size-xxs) * 0.5);
  position: relative;
  padding: calc(var(--el-size-xxs) * 0.1);
  width: var(--el-size-xxs);
  z-index: 1;
  opacity: var(--opacity-disabled);
  margin-right: var(--gap-sm);
}

.q-switch-active {
  transition: all var(--duration-quick);
  opacity: var(--opacity-enabled);
}

.q-switch .q-switch-toggle {
  position: absolute;
  background-color: var(--accent-color-primary);
  border-radius: 50%;
  top: calc(var(--el-size-xxs) * 0.05);
  left: calc(var(--el-size-xxs) * 0.1);
  height: calc(var(--el-size-xxs) * 0.35);
  width: calc(var(--el-size-xxs) * 0.35);
  transform: translateX(0);
  transition: transform 0.3s ease, background-color 0.5s ease;
}

.q-input-label-switch {
  display: flex;
}

.q-switch-toggle-checked {
  transform: translateX(calc(var(--el-size-xxs) * 0.4)) !important;
}
</style>
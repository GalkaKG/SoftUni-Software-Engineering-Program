<template>
  <label v-if="label" :for="id" class="q-input-label">
    {{ label }}
    <span class="q-input-required-sign" v-if="required">{{ requiredSign }}</span>
  </label>
  <div class="q-text-area-wrapper">
    <pre><span>{{ modelValue }}</span><br /></pre>
    <textarea
      class="q-input-base"
      :class="{
        'q-error': !!error,
      }"
      v-bind="$attrs"
      @input="$emit('update:modelValue', $event.target.value)"
      :value="modelValue"
      :id="id"
      :required="required"
      :placeholder="labelPrefix ? labelPrefix + label.toLowerCase() : label"
      :aria-label="label"
      :aria-required="required"
      :aria-describedby="error ? `${id}-error` : null"
      :aria-invalid="error ? true : null"
    />
  </div>

  <small
    v-if="error"
    class="q-input-error-msg"
    :id="`${id}-error`"
    aria-live="assertive"
  >{{ error }}</small>
</template>

<script>
import uuid from "../../../use/uuid";


export default {
  setup() {
    const id = uuid();
    return { id }
  },
  props: {
    labelPrefix: {
      type: String,
      default: null,
    },
    label: {
      type: String,
    },
    modelValue: {
      type: [String, Number],
    },
    error: {
      type: String,
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
.q-text-area-wrapper {
  position: relative;
}

.q-text-area-wrapper > textarea,
.q-text-area-wrapper > pre {
  height: 100%;
  padding: var(--gap-sm) var(--gap-xs);
  margin: var(--gap-sm) 0;
}

.q-text-area-wrapper > textarea {
  top: -8px;
  left: 0;
  overflow: hidden;
  position: absolute;
  resize: none;
}

.q-text-area-wrapper > pre {
  display: block;
  visibility: hidden;
}

.q-input-base,
.q-input-label {
  width: 100%;
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
  white-space: pre-wrap;
  word-wrap: break-word;
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
</style>
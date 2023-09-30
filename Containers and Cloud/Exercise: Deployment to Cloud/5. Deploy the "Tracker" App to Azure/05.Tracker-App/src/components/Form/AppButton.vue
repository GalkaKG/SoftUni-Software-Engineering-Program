<template>
  <button
    v-ripple
    class="q-button-base"
    :id="id"
    :disabled="loading"
    :aria-disabled="loading"
    :aria-busy="loading"
    :class="{
      'q-button-u-full-width': fluid === true,
      'q-button-u-disabled': loading,
      'q-button-v-primary': variant === 'primary',
      'q-button-v-secondary': variant === 'secondary',
      'q-button-v-info': variant === 'info',
      'q-button-v-success': variant === 'success',
      'q-button-v-warning': variant === 'warning',
      'q-button-v-error': variant === 'error',
      'q-button-v-link': variant === 'link',
      'q-button-s-small': size === 'small',
      'q-button-s-medium': size === 'medium',
      'q-button-s-large': size === 'large',
      'q-button-s-xlarge': size === 'xlarge',
    }"
  >
    <i v-if="loading">
      <div class="loader"></div>
    </i>
    <span v-else>
      <slot />
      {{ label }}
    </span>
  </button>
</template>

<script>
import uuid from "../../../use/uuid";

export default {
  setup() {

    const id = uuid();
    return { id }
  },
  props: {
    loading: {
      type: Boolean,
      default: false,
    },
    label: {
      type: String,
      required: true,
      default: "",
    },
    fluid: {
      type: Boolean,
      default: false,
    },
    variant: {
      type: String,
      required: false,
      default: "primary",
      validator(value) {
        const isPrimary = value === "primary";
        const isSecondary = value === "secondary";
        const isInfo = value === "info";
        const isSuccess = value === "success";
        const isWarning = value === "warning";
        const isError = value === "error";
        const isDark = value === "dark";
        const isBright = value === "bright";
        return (
          isPrimary ||
          isSecondary ||
          isInfo ||
          isSuccess ||
          isWarning ||
          isError ||
          isDark ||
          isBright
        );
      },
    },
    size: {
      type: String,
      default: "medium",
      validator(value) {
        const isSmall = value === "small";
        const isMedium = value === "medium";
        const isLarge = value === "large";
        const isXlarge = value === "xlarge";
        return isSmall || isMedium || isLarge || isXlarge;
      },
    },
  }
}

</script>

<style scoped>
.q-button-base {
  border: none;
  border-radius: 0 var(--gap-sm) 0 var(--gap-sm);
  cursor: pointer;
  margin: var(--gap-sm) var(--gap-sm) var(--gap-sm) 0;
  text-align: center;
  font-weight: 600;
}

/* Util classes for the button */
.q-button-u-fluid {
  width: 100%;
  margin: 0;
}

.q-button-base.q-button-u-full-width {
  display: block;
  width: 100%;
}

.q-button-u-disabled {
  opacity: var(--opacity-disabled);
}

/* Variant classes */
.q-button-v-primary {
  color: var(--white-color);
  background-color: var(--accent-color-primary);
}

.q-button-v-secondary {
  background-color: var(--accent-color-secondary);
}

.q-button-v-info {
  background-color: var(--color-info);
  color: var(--white-color);
}

.q-button-v-success {
  background-color: var(--color-success);
  color: var(--white-color);
}

.q-button-v-warning {
  background-color: var(--color-warning);
  color: var(--white-color);
}

.q-button-v-error {
  background-color: var(--color-error);
  color: var(--white-color);
}

.q-button-v-primary .loader,
.q-button-v-secondary .loader {
  border-top: 2px solid var(--background-color-tartiary);
}

.q-button-v-info .loader,
.q-button-v-success .loader,
.q-button-v-warning .loader,
.q-button-v-error .loader {
  border-top: 2px solid var(--white-color);
}

.q-button-v-link {
  background-color: transparent !important;
  padding: var(--gap-sm);
  color: var(--accent-color-primary) !important;
  font-size: var(--text-size-sm);
  width: fit-content;
}

.q-button-v-link:hover {
  text-decoration: underline;
}

/* Sizing classes */
.q-button-s-small {
  padding: var(--gap-sm) var(--gap-lg);
  font-size: var(--text-size-xs);
}

.q-button-s-small .loader {
  height: var(--text-size-xs);
}

.q-button-s-medium {
  padding: var(--gap-sm) var(--gap-xl);
  font-size: var(--text-size-sm);
}

.q-button-s-medium .loader {
  width: var(--text-size-sm);
  height: var(--text-size-sm);
}

.q-button-s-large {
  padding: var(--gap-md) var(--gap-xxl);
  font-size: var(--text-size-md);
  height: var(--el-size-xxs);
}

.q-button-s-large .loader {
  width: var(--text-size-md);
  height: var(--text-size-md);
}

.q-button-s-xlarge {
  padding: var(--gap-md) var(--gap-xxl);
  font-size: var(--text-size-lg);
  height: var(--el-size-xs);
  width: var(--el-size-xl);
}

.q-button-s-xlarge .loader {
  width: var(--text-size-lg);
  height: var(--text-size-lg);
}

/* Text color classes */
.q-button-c-text-bright {
  color: var(--white-color) !important;
}

.q-button-c-text-dark {
  color: var(--black-color) !important;
}

/* Styles for the loader */
.loader {
  display: block;
  margin: auto;
  padding: var(--gap-xs);
  border-radius: 50%;
  border-right: 2px solid transparent;
  animation: fullRotation var(--duration-semi) linear infinite;
}
@keyframes fullRotation {
  to {
    transform: rotate(360deg);
  }
}
</style>
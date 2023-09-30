<template>
  <div>
    <input @change="toggleTheme" :id="themeButtonId" type="checkbox" class="q-switch-checkbox" />
    <label class="q-switch-label" :class="{ 'q-switch-disabled': disabled }" :for="themeButtonId">
      <span>🌙</span>
      <span>☀️</span>
      <div
        tabindex="0"
        class="q-toggle"
        :class="{
          'q-toggle-checked': userTheme === 'dark-theme',
        }"
      ></div>
    </label>
  </div>
</template>

<script>
import uuid from "../../../use/uuid.js";
import { ref, onMounted } from "vue";

export default {
  setup(props) {
    const themeButtonId = uuid();
    let userTheme = ref("");
    const toggleTheme = () => {
      if (!props.disabled) {
        const activeTheme = localStorage.getItem("user-theme");
        if (activeTheme === "light-theme") {
          setTheme("dark-theme");
        } else {
          setTheme("light-theme");
        }
      }
    };

    const setTheme = (theme) => {
      localStorage.setItem("user-theme", theme);
      userTheme.value = theme;
      document.documentElement.className = theme;
    };

    const getMediaPreference = () => {
      const hasDarkPreference = window.matchMedia(
        "(prefers-color-scheme: dark)"
      ).matches;
      if (hasDarkPreference) {
        return "dark-theme";
      }
    };

    onMounted(() => {
      if (props.initWithPreference) {
        setTheme(getMediaPreference());
      } else {
        setTheme(localStorage.getItem("user-theme"));
      }
    });

    return { themeButtonId, userTheme, toggleTheme };
  },
  props: {
    initWithPreference: {
      type: Boolean,
      default: true,
    },
    disabled: {
      type: Boolean,
      default: false,
    },
  },
};
</script>

<style scoped>
.q-switch-checkbox {
  display: none;
}

.q-switch-label {
  align-items: center;
  background: var(--text-color-primary);
  border: calc(var(--el-size-xs) * 0.025) solid var(--accent-color-primary);
  border-radius: var(--el-size-xs);
  cursor: pointer;
  display: flex;
  font-size: calc(var(--el-size-xs) * 0.3);
  height: calc(var(--el-size-xs) * 0.45);
  position: relative;
  padding: calc(var(--el-size-xs) * 0.1);
  transition: background 0.5s ease;
  justify-content: space-between;
  width: var(--el-size-xs);
  z-index: 1;
}

.q-switch-label .q-toggle {
  position: absolute;
  background-color: var(--accent-color-primary);
  border-radius: 50%;
  top: calc(var(--el-size-xs) * 0.025);
  left: calc(var(--el-size-xs) * 0.1);
  height: calc(var(--el-size-xs) * 0.35);
  width: calc(var(--el-size-xs) * 0.35);
  transform: translateX(0);
  transition: transform 0.3s cubic-bezier(0.39, 0.58, 0.57, 1),
    background-color 0.5s ease;
  outline: none;
}

.q-switch-disabled {
  opacity: var(--opacity-disabled);
}

.q-toggle-checked {
  transform: translateX(calc(var(--el-size-xs) * 0.425)) !important;
}
</style>
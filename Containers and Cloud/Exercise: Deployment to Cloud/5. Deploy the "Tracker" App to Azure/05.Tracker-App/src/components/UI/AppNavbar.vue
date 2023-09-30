<template>
  <nav class="q-navbar">
    <img
      class="q-navbar-logo"
      width="50"
      height="40"
      src="../../assets/icon_q-bit.png"
      alt="the q-bit logo of this website"
    />

    <section>
      <app-dropdown label="About">
        <section class="q-navbar-about">
          <h3 class="q-navbar-about__title">
            <i class="fas fa-info-circle"></i> About this app
          </h3>
          <p class="q-navbar-about__paragraph">This simple todo-app is part of the article</p>
          <blockquote>
            <a
              target="_blank"
              href="https://blog.q-bit.me/a-step-by-step-guide-for-developing-and-deploying-a-vue-js-app-with-docker-part-two/"
            >A step-by-step guide to develop and deploy Vue apps with docker, part two</a>
          </blockquote>
          <p class="q-navbar-about__paragraph">
            If you've skipped it, you should read the
            <a
              target="_blank"
              href="https://blog.q-bit.me/how-to-develop-and-deploy-a-vue-js-app-with-docker-part-one/"
            >first article</a> before you jump straight into this one.
          </p>
          <small>Made with 💚	and Vue.js</small>
        </section>
      </app-dropdown>
      <app-theme-button class="q-navbar-item"></app-theme-button>
    </section>
  </nav>
</template>

<script>
import AppThemeButton from "../Theme/AppThemeButton.vue";
import AppDropdown from './AppDropdown.vue';

export default {
  components: {
    AppThemeButton,
    AppDropdown,
  },
};
</script>

<style scoped>
.q-navbar {
  display: flex;
  justify-content: space-between;
  color: var(--white-color);
  background-color: var(--accent-color-primary);
  padding: var(--gap-sm);
}

.q-navbar-logo {
  font-weight: 600;
  font-size: var(--text-size-md);
}

.q-navbar-logo {
  background-color: white;
  border-radius: 0 var(--gap-sm) 0 var(--gap-sm);
}

.q-navbar-logo,
.q-navbar-item {
  display: inline-block;
  padding: var(--gap-sm) var(--gap-md);
}

.q-navbar-about {
  padding: var(--gap-sm) var(--gap-md);
}

.q-navbar-about__title {
  font-size: var(--text-size-lg);
}
.q-navbar-about__title,
.q-navbar-about__paragraph {
  line-height: var(--gap-xl);
  margin: var(--gap-sm) 0;
}
</style>
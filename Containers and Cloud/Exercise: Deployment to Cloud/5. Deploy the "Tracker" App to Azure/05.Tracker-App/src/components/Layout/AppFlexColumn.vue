<template>
  <div
    :class="{
      'q-flex-col': hasSizedColumns,
      'q-flex-col-auto': hasNoColumns,

      'q-flex-col-1': cols === 1,
      'q-flex-col-2': cols === 2,
      'q-flex-col-3': cols === 3,
      'q-flex-col-4': cols === 4,
      'q-flex-col-5': cols === 5,
      'q-flex-col-6': cols === 6,
      'q-flex-col-7': cols === 7,
      'q-flex-col-8': cols === 8,
      'q-flex-col-9': cols === 9,
      'q-flex-col-10': cols === 10,
      'q-flex-col-11': cols === 11,
      'q-flex-col-12': cols === 12,

      'q-flex-col-sm-1': smCols === 1,
      'q-flex-col-sm-2': smCols === 2,
      'q-flex-col-sm-3': smCols === 3,
      'q-flex-col-sm-4': smCols === 4,
      'q-flex-col-sm-5': smCols === 5,
      'q-flex-col-sm-6': smCols === 6,
      'q-flex-col-sm-7': smCols === 7,
      'q-flex-col-sm-8': smCols === 8,
      'q-flex-col-sm-9': smCols === 9,
      'q-flex-col-sm-10': smCols === 10,
      'q-flex-col-sm-11': smCols === 11,
      'q-flex-col-sm-12': smCols === 12,

      'q-flex-col-md-1': mdCols === 1,
      'q-flex-col-md-2': mdCols === 2,
      'q-flex-col-md-3': mdCols === 3,
      'q-flex-col-md-4': mdCols === 4,
      'q-flex-col-md-5': mdCols === 5,
      'q-flex-col-md-6': mdCols === 6,
      'q-flex-col-md-7': mdCols === 7,
      'q-flex-col-md-8': mdCols === 8,
      'q-flex-col-md-9': mdCols === 9,
      'q-flex-col-md-10': mdCols === 10,
      'q-flex-col-md-11': mdCols === 11,
      'q-flex-col-md-12': mdCols === 12,

      'q-flex-col-lg-1': lgCols === 1,
      'q-flex-col-lg-2': lgCols === 2,
      'q-flex-col-lg-3': lgCols === 3,
      'q-flex-col-lg-4': lgCols === 4,
      'q-flex-col-lg-5': lgCols === 5,
      'q-flex-col-lg-6': lgCols === 6,
      'q-flex-col-lg-7': lgCols === 7,
      'q-flex-col-lg-8': lgCols === 8,
      'q-flex-col-lg-9': lgCols === 9,
      'q-flex-col-lg-10': lgCols === 10,
      'q-flex-col-lg-11': lgCols === 11,
      'q-flex-col-lg-12': lgCols === 12,

      'q-flex-col-xl-1': xlCols === 1,
      'q-flex-col-xl-2': xlCols === 2,
      'q-flex-col-xl-3': xlCols === 3,
      'q-flex-col-xl-4': xlCols === 4,
      'q-flex-col-xl-5': xlCols === 5,
      'q-flex-col-xl-6': xlCols === 6,
      'q-flex-col-xl-7': xlCols === 7,
      'q-flex-col-xl-8': xlCols === 8,
      'q-flex-col-xl-9': xlCols === 9,
      'q-flex-col-xl-10': xlCols === 10,
      'q-flex-col-xl-11': xlCols === 11,
      'q-flex-col-xl-12': xlCols === 12,
    }"
  >
    <slot />
  </div>
</template>

<script>
export default {
  computed: {
    // Used to determine whether to apply auto sizing
    hasNoColumns() {
      return (
        !this.cols &&
        !this.smCols &&
        !this.mdCols &&
        !this.lgCols &&
        !this.xlCols
      );
    },

    // Used to determine whether to apply padding
    hasSizedColumns() {
      return (
        (this.cols && this.cols > 0) ||
        (this.smCols && this.smCols > 0) ||
        (this.mdCols && this.mdCols > 0) ||
        (this.lgCols && this.lgCols > 0) ||
        (this.xlCols && this.xlCols > 0)
      );
    },
  },
  props: {
    cols: {
      type: Number,
      required: false,
      default: undefined,
      validator(value) {
        return (value >= 0 && value <= 12) || undefined;
      },
    },

    smCols: {
      type: Number,
      required: false,
      default: undefined,
      validator(value) {
        return (value >= 0 && value <= 12) || undefined;
      },
    },

    mdCols: {
      type: Number,
      required: false,
      default: undefined,
      validator(value) {
        return (value >= 0 && value <= 12) || undefined;
      },
    },

    lgCols: {
      type: Number,
      required: false,
      default: undefined,
      validator(value) {
        return (value >= 0 && value <= 12) || undefined;
      },
    },

    xlCols: {
      type: Number,
      required: false,
      default: undefined,
      validator(value) {
        return (value >= 0 && value <= 12) || undefined;
      },
    },
  },
};
</script>

<style scoped>
/* Column styles were strongly influenced by bootstrap CSS */
.q-flex-col {
  padding-left: var(--gap-xl);
  padding-right: var(--gap-xl);
}

.q-flex-col-auto {
  flex: 1 0 0%;
}

.q-flex-col-1 {
  width: 8.33333%;
}
.q-flex-col-2 {
  width: 16.66667%;
}
.q-flex-col-3 {
  width: 25%;
}
.q-flex-col-4 {
  width: 33.33333%;
}
.q-flex-col-5 {
  width: 41.66667%;
}
.q-flex-col-6 {
  width: 50%;
}
.q-flex-col-7 {
  width: 58.33333%;
}
.q-flex-col-8 {
  width: 66.66667%;
}
.q-flex-col-9 {
  width: 75%;
}
.q-flex-col-10 {
  width: 83.33333%;
}
.q-flex-col-11 {
  width: 91.66667%;
}
.q-flex-col-12 {
  width: 100%;
}

/* sm */
@media (max-width: 768px) {
  .q-flex-col-sm-1 {
    width: 8.33%;
  }
  .q-flex-col-sm-2 {
    width: 16.67%;
  }
  .q-flex-col-sm-3 {
    width: 25%;
  }
  .q-flex-col-sm-4 {
    width: 33.33%;
  }
  .q-flex-col-sm-5 {
    width: 41.67%;
  }
  .q-flex-col-sm-6 {
    width: 50%;
  }
  .q-flex-col-sm-7 {
    width: 58.33%;
  }
  .q-flex-col-sm-8 {
    width: 66.66%;
  }
  .q-flex-col-sm-9 {
    width: 75%;
  }
  .q-flex-col-sm-10 {
    width: 83.33%;
  }
  .q-flex-col-sm-11 {
    width: 91.67%;
  }
  .q-flex-col-sm-12 {
    width: 100%;
  }
}

/* md */
@media (max-width: 992px) and (min-width: 768px) {
  .q-flex-col-md-1 {
    width: 8.33%;
  }
  .q-flex-col-md-2 {
    width: 16.67%;
  }
  .q-flex-col-md-3 {
    width: 25%;
  }
  .q-flex-col-md-4 {
    width: 33.33%;
  }
  .q-flex-col-md-5 {
    width: 41.67%;
  }
  .q-flex-col-md-6 {
    width: 50%;
  }
  .q-flex-col-md-7 {
    width: 58.33%;
  }
  .q-flex-col-md-8 {
    width: 66.66%;
  }
  .q-flex-col-md-9 {
    width: 75%;
  }
  .q-flex-col-md-10 {
    width: 83.33%;
  }
  .q-flex-col-md-11 {
    width: 91.67%;
  }
  .q-flex-col-md-12 {
    width: 100%;
  }
}

/* lg */
@media (max-width: 1200px) and (min-width: 992px) {
  .q-flex-col-lg-1 {
    width: 8.33%;
  }
  .q-flex-col-lg-2 {
    width: 16.67%;
  }
  .q-flex-col-lg-3 {
    width: 25%;
  }
  .q-flex-col-lg-4 {
    width: 33.33%;
  }
  .q-flex-col-lg-5 {
    width: 41.67%;
  }
  .q-flex-col-lg-6 {
    width: 50%;
  }
  .q-flex-col-lg-7 {
    width: 58.33%;
  }
  .q-flex-col-lg-8 {
    width: 66.66%;
  }
  .q-flex-col-lg-9 {
    width: 75%;
  }
  .q-flex-col-lg-10 {
    width: 83.33%;
  }
  .q-flex-col-lg-11 {
    width: 91.67%;
  }
  .q-flex-col-lg-12 {
    width: 100%;
  }
}

/* xl */
@media (min-width: 1200px) {
  .q-flex-col-xl-1 {
    width: 8.33%;
  }
  .q-flex-col-xl-2 {
    width: 16.67%;
  }
  .q-flex-col-xl-3 {
    width: 25%;
  }
  .q-flex-col-xl-4 {
    width: 33.33%;
  }
  .q-flex-col-xl-5 {
    width: 41.67%;
  }
  .q-flex-col-xl-6 {
    width: 50%;
  }
  .q-flex-col-xl-7 {
    width: 58.33%;
  }
  .q-flex-col-xl-8 {
    width: 66.66%;
  }
  .q-flex-col-xl-9 {
    width: 75%;
  }
  .q-flex-col-xl-10 {
    width: 83.33%;
  }
  .q-flex-col-xl-11 {
    width: 91.67%;
  }
  .q-flex-col-xl-12 {
    width: 100%;
  }
}
</style>
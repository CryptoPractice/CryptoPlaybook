<template>
  <span
    class="tile text-mono text-bold anim-fade-in fast"
    :presence="tileState"
  >
    <slot />
  </span>
</template>

<script>
export default {
  props: {
    tileState: {
      type: String,
      default: 'empty',
    },
  },
}
</script>

<style lag="scss">
.tile {
  display: inline-flex;
  justify-content: center;
  align-items: center;
  box-sizing: border-box;
  user-select: none;
  line-height: 1;
  margin: 1px;
  padding: 1px 2px;
  text-transform: uppercase;
}

.tile[presence="empty"] {
  box-shadow: inset 0px 0px 0px 1px var(--color-fg-subtle);
}

.tile[presence="correct"] {
  background-color: var(--color-success-emphasis) !important;
  color: var(--color-fg-on-emphasis) !important;
}

.tile[presence="present"] {
  background-color: var(--color-attention-emphasis) !important;
  color: var(--color-fg-on-emphasis) !important;
}

.tile[presence="absent"] {
  background-color: var(--color-neutral-emphasis) !important;
  color: var(--color-fg-on-emphasis) !important;
}
</style>

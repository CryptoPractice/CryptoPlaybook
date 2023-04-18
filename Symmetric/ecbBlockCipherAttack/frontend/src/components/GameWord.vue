<template>
  <div>
    <GameTile
      v-for="(wordlet, i) in word"
      :key="i"
      :tile-state="wordlet.presence"
    >
      {{ wordlet.letter }}
    </GameTile>
  </div>
</template>

<script>
import GameTile from './GameTile.vue'

export default {
  components: {
    GameTile,
  },
  props: {
    word: {
      type: Object,
      required: true,
    },
  },
}
</script>

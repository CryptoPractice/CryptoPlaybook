<template>
  <div class="d-inline-flex flex-items-center flex-column">
    <GameWord
      v-for="(word, index) of allWords"
      :key="index"
      :word="word"
    />
  </div>
</template>

<script>
import GameWord from './GameWord.vue'
const TOTAL_CHAR = 64
const TOTAL_GUESSES = 10
export default {
  components: {
    GameWord,
  },
  props: {
    allGuesses: {
      type: Array,
      default: () => [],
    },
  },
  computed: {
    emptyWord () {
      return Array(TOTAL_CHAR).fill({
        letter: '\xA0',
        presence: 'empty',
      })
    },
    allWords () {
      return this.allGuesses.concat(
        Array(TOTAL_GUESSES - this.allGuesses.length).fill(this.emptyWord),
      )
    },
  },
  methods: {},
}
</script>

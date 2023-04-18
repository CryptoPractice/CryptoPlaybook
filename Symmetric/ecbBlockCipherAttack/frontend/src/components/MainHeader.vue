<template>
  <header class="Header">
    <div class="Header-item Header-item--full">
      <span class="h3">Encryptdle</span>
    </div>
    <div class="Header-item">
      <GameModal
        v-model="showShare"
        class="Header-item-modal"
      >
        <template #outsideButton>
          Share
        </template>
        <template #modalTitle>
          <h3 class="Box-title">
            Share your Results
          </h3>
        </template>
        <template #modalBody>
          <div
            v-if="isGameOver"
            class="form-group"
          >
            <div class="form-group-body">
              <textarea
                v-model="shareResults"
                class="form-control"
                readonly
              />
            </div>
          </div>
          <p v-else>
            Share your results after the game is over!
          </p>
        </template>
        <template #modalButton>
          👌
        </template>
      </GameModal>
    </div>
    <div class="Header-item">
      <GameModal
        v-model="showHelp"
        class="Header-item-modal"
      >
        <template #outsideButton>
          ❓
        </template>
        <template #modalTitle>
          <h3 class="Box-title">
            How To Play
          </h3>
        </template>
        <template #modalBody>
          <p>
            Guess the <strong>ENCRYPTDLE</strong> string in 10 tries.
          </p>
          <p>
            Each guess is sent to the server to be encrypted and compared with the real answer's encrypted version.
          </p>
          <p>
            Each guess must be a string between 1 and 32 characters in length.
            Hit the Submit button to submit.
          </p>
          <p>
            After each guess, the color of the tiles will change to show how close your guess was to the word.
          </p>
          <hr>
          <p>
            <strong>Examples</strong>
          </p>
          <p>
            <GameTile tile-state="correct">
              A
            </GameTile>
            <br>The character <strong>A</strong> is in the string and in the correct spot.
          </p>
          <p>
            <GameTile tile-state="present">
              B
            </GameTile>
            <br>The character <strong>B</strong> is in the string but in the wrong spot.
          </p>
          <p>
            <GameTile tile-state="absent">
              C
            </GameTile>
            <br>The character <strong>C</strong> is not in the string in any spot.
          </p>
        </template>
        <template #modalButton>
          👌
        </template>
      </GameModal>
    </div>
    <div class="Header-item">
      <button
        type="button"
        class="btn"
        @click="toggleDark()"
      >
        {{ isDark ? "🌙" : "☀" }}
      </button>
    </div>
  </header>
</template>

<script setup>
import { useDark, useStorage, useToggle } from '@vueuse/core'
import { computed, onMounted, ref, watch } from 'vue'
import GameModal from './GameModal.vue'
import GameTile from './GameTile.vue'

const props = defineProps({
  isWin: {
    type: Boolean,
    default: false,
  },
  isGameOver: {
    type: Boolean,
    default: false,
  },
})
const isDark = useDark({ attribute: 'data-color-mode' })
const toggleDark = useToggle(isDark)
const showShare = ref(false)
const showHelp = ref(false)

onMounted(() => {
  if (props.isGameOver) {
    showShare.value = true
  }
})

watch(
  () => props.isGameOver,
  () => {
    showShare.value = true
  },
)

function generateShare () {
  const guesses = useStorage('gameGuesses', [])
  let shareString = 'Encryptdle '
  if (props.isWin) {
    shareString += `${guesses.value.length}/10\n`
  } else {
    shareString += 'x/10\n'
  }

  const absent = isDark.value ? '⬛' : '⬜'
  return guesses.value.reduce((prev, current) => {
    return (
      prev
      + current.reduce((p, c) => {
        let tile = absent
        if (c.presence === 'correct') {
          tile = '🟩'
        } else if (c.presence === 'present') {
          tile = '🟨'
        }

        return p + tile
      }, '\n')
    )
  }, shareString)
}
const shareResults = computed(() => (props.isGameOver ? generateShare() : ''))
</script>

<style>
.Header-item-modal {
  color: var(--color-fg-default);
}
</style>

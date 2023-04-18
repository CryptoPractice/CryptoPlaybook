<template>
  <body>
    <MainHeader
      :is-win="isWin"
      :is-game-over="isGameOver"
    />
    <main class="main d-flex flex-items-center flex-justify-center">
      <div class="board d-inline-flex flex-column flex-justify-between">
        <div />
        <GameBoard :all-guesses="guesses" />
        <form
          class="pb-4"
          @submit="submit"
        >
          <p
            v-if="formError"
            class="note color-fg-danger"
          >
            {{ formError }}
          </p>
          <p class="note">
            Guess is between 1 to 32 characters
          </p>
          <div class="form-group-body">
            <div class="input-group">
              <input
                v-model="guess"
                class="form-control input-lg"
                type="text"
                placeholder="Guess"
                aria-label="Guess"
                :disabled="isGameOver"
                @input="validate"
              >
              <span class="input-group-button">
                <button
                  class="btn"
                  type="submit"
                  aria-label="submit"
                  :aria-disabled="!isButtonEnabled ? 'true' : 'false'"
                  :disabled="!isButtonEnabled"
                >
                  <span v-if="!isLoading">Submit</span>
                  <span
                    v-else
                    class="AnimatedEllipsis"
                  />
                </button>
              </span>
            </div>
          </div>
        </form>
      </div>
    </main>
  </body>
</template>

<script setup>
import { $fetch } from 'ohmyfetch'
import { computed, ref } from 'vue'
import { useStorage } from '@vueuse/core'
import MainHeader from './components/MainHeader.vue'
import GameBoard from './components/GameBoard.vue'

const guesses = useStorage('gameGuesses', [])
const isWin = computed(() => {
  if (guesses.value.length > 0) {
    return guesses.value[guesses.value.length - 1].reduce(
      (prev, curr) => prev && curr.presence === 'correct',
      true,
    )
  } else {
    return false
  }
})
const isLoading = ref(false)
const guess = ref('')
const formError = ref('')

async function submit (e) {
  e.preventDefault()
  formError.value = ''
  isLoading.value = true
  try {
    const result = await $fetch(`/api/compare?guess=${guess.value}`, {method: 'POST'})
    guesses.value.push(result)
  } catch (error) {
    if (error?.data?.detail[0]?.msg) {
      formError.value = error.data.detail[0].msg
    } else {
      formError.value = error.message
    }
  }
  isLoading.value = false
}

const isInputValid = ref(false)

function validate () {
  if (guess.value.length >= 1 && guess.value.length <= 32) {
    isInputValid.value = true
  } else {
    isInputValid.value = false
  }
}
const isGameOver = computed(() => guesses.value.length >= 10 || isWin.value)
const isButtonEnabled = computed(
  () => !isWin.value && isInputValid.value && !isGameOver.value,
)
</script>

<style lang="scss">
@import "@primer/css/index.scss";

.main {
  height: calc(100vh - 70px);
  width: 100vw;
}

.board {
  height: 100%;
}
</style>

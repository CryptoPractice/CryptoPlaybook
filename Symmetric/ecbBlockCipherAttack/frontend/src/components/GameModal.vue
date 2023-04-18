<template>
  <div>
    <button
      type="button"
      class="btn"
      @click="toggleModal(true)"
    >
      <slot name="outsideButton" />
    </button>
    <div>
      <div
        v-if="modelValue"
        class="modal-overlay-bg"
        @click="toggleModal(false)"
      />
      <div
        v-if="modelValue"
        class="modal Box Box--overlay d-flex flex-column anim-fade-in fast"
      >
        <div class="Box-header">
          <slot name="modalTitle" />
        </div>
        <div class="Box-body">
          <slot name="modalBody" />
        </div>
        <div class="Box-footer">
          <button
            type="button"
            class="btn btn-block"
            @click="toggleModal(false)"
          >
            <slot name="modalButton" />
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  modelValue: {
    type: Boolean,
    default: () => false,
  },
})
const emit = defineEmits(['update:modelValue'])
const modalVisible = computed({
  get: () => props.modelValue,
  set: value => emit('update:modelValue', value),
})

function toggleModal (b) {
  modalVisible.value = b
}
</script>

<style>
.modal-overlay-bg {
  position: fixed;
  left: 0;
  top: 0;
  height: 100vh;
  width: 100vw;
  opacity: 75%;
  z-index: 100;
  background: black;
}

.modal {
  position: fixed;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
  z-index: 200;
}
</style>

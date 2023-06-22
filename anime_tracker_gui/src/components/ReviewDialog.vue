<template>
  <q-dialog
    ref="dialogRef"
    persistent
    @hide="onDialogHide"
  >
    <q-card
      class="q-dialog-plugin full-width"
      style="max-width:400px"
    >
      <q-card-section>
        <div class="text-h6 text-secondary text-weight-bolder">
          {{ anime }}'s Review
        </div>
      </q-card-section>
      <q-card-section>
        <div class="text-body1">
          {{ review }}
        </div>
      </q-card-section>
      <q-card-actions align="right">
        <q-btn
          color="secondary"
          label="Done"
          @click="onDialogOK"
        />
      </q-card-actions>
    </q-card>
  </q-dialog>
</template>

<script setup>
import { useDialogPluginComponent } from 'quasar'
// import { archivesApi } from 'src/boot/axios'
// import { onMounted, ref } from 'vue'
// import { useStore } from 'vuex'
// import useUtility from '../common/composables/useUtility'

// eslint-disable-next-line no-unused-vars
const emits = defineEmits([...useDialogPluginComponent.emits])
// eslint-disable-next-line no-unused-vars
const props = defineProps({
  review: {
    required: true,
    type: String
  },
  anime: {
    default: '',
    type: String
  }
})
const {
  dialogRef, onDialogHide, onDialogOK
  // onDialogCancel
} = useDialogPluginComponent()
// const { errorNotif, successNotif } = useUtility()

// const store = useStore()
</script>

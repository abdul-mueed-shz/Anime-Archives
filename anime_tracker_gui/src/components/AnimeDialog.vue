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
      <div v-if="type==='review'">
        <q-card-section>
          <div class="text-h6 text-secondary text-weight-bolder">
            {{ info.anime+"'s" }} Review
          </div>
        </q-card-section>
        <q-card-section>
          <div class="text-body1">
            {{ info.review }}
          </div>
        </q-card-section>
      </div>
      <q-card-section v-else-if="type==='add_review'">
        <div class="text-h6 text-secondary q-pb-sm text-weight-bolder">
          Add review
        </div>
        <div class="flex flex-center">
          <q-input
            class="full-width"
            label="Write a review..."
            type="textarea"
            outlined
            v-model="addReviewForm.review"
          />
          <q-rating
            class="q-mt-sm"
            size="2em"
            :max="10"
            color="primary"
            v-model="addReviewForm.rating"
          />
        </div>
      </q-card-section>
      <q-card-actions
        align="right"
        class="q-pb-md"
      >
        <q-btn
          :color="okayButton[type].color"
          label="Done"
          @click="okayButton[type].action"
          class="border-radius__8px"
        />
        <q-btn
          v-if="type==='add_review'"
          color="secondary"
          label="Skip"
          @click="()=>onDialogOK()"
          flat
          class="border-radius__8px"
        />
      </q-card-actions>
    </q-card>
  </q-dialog>
</template>

<script setup>
import { useDialogPluginComponent } from 'quasar'
import { ref } from 'vue'
// import { archivesApi } from 'src/boot/axios'
// import { onMounted, ref } from 'vue'
// import { useStore } from 'vuex'
// import useUtility from '../common/composables/useUtility'

// eslint-disable-next-line no-unused-vars
const emits = defineEmits([...useDialogPluginComponent.emits])
// eslint-disable-next-line no-unused-vars
const props = defineProps({
  type: {
    required: true,
    type: String
  },
  info: {
    required: false,
    default: null,
    type: Object
  }
})

const {
  dialogRef, onDialogHide, onDialogOK
  // onDialogCancel
} = useDialogPluginComponent()
// const { errorNotif, successNotif } = useUtility()

// const store = useStore()
const addReviewForm = ref({
  review: null,
  rating: null
})
const okayButton = {
  review: {
    color: 'secondary',
    action: onDialogOK
  },
  add_review: {
    color: 'positive',
    action: () => {
      onDialogOK(addReviewForm.value)
    }
  }
}

</script>

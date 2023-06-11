<template>
  <div class="fullscreen bg-primary text-white text-center q-pa-md flex flex-center">
    <div>
      <div style="font-size: 30vh">
        {{ MAP.ERRORS.INTERPOLATIONS.FOUR_O_FOUR.STATUS_CODE }}
      </div>
      <div
        class="text-h2 error__font"
      >
        {{ MAP.ERRORS.INTERPOLATIONS.FOUR_O_FOUR.MESSAGES.NOTHING_HERE }}
      </div>

      <q-btn
        class="q-mt-xl error__btn"
        color="white"
        text-color="grey-9"
        rounded
        unelevated
        :to="ROUTE_CONSTS.HOME.PATH"
        :label="MAP.COMMON.LABELS.ROUTE_TO_HOME"
        no-caps
      />
    </div>
  </div>
</template>

<script setup>
import useComputes from 'src/common/composables/useComputes'
import { ROUTE_CONSTS } from 'src/common/constants/routes'

const { MAP } = useComputes()
</script>
<style scoped lang="scss">
.error__font{
  opacity:.4
}
.error__btn{
  width: 34rem;
}
</style>

<template>
  <q-page
    padding
  >
    <div class="column">
      <div class="row q-ma-md flex-center">
        <q-tabs
          inline-label
          outside-arrows
          mobile-arrows
          class="nav-tabs"
        >
          <q-tab
            icon="home"
            name="toprated"
            :label="MAP.HOME.LABELS.TOP_RATED"
            @click="scrollToElement(toprated)"
          />
          <q-tab
            icon="person"
            name="watched"
            :label="MAP.HOME.LABELS.RECENT"
            @click="scrollToElement(recent)"
          />
          <q-tab
            icon="person"
            name="upcoming"
            :label="MAP.HOME.LABELS.UPCOMING"
            @click="scrollToElement(upcomin)"
          />
        </q-tabs>
      </div>
      <section class="q-mb-lg">
        <div
          class="flex flex-center text-h6 text-weight-bold q-mb-md section-label"
          ref="toprated"
        >
          {{ MAP.HOME.INTERPOLATIONS.TOP_RATED }}
        </div>
        <CardSlider api="top/anime" />
      </section>
      <section class="q-mb-lg">
        <div
          class="flex flex-center text-h6 text-weight-bold q-mb-md section-label"
          ref="upcomin"
        >
          {{ MAP.HOME.INTERPOLATIONS.UPCOMING }}
        </div>
        <CardSlider api="seasons/upcoming" />
      </section>
      <section class="q-mb-lg">
        <div
          class="flex flex-center text-h6 text-weight-bold q-mb-md section-label"
          ref="recent"
        >
          {{ MAP.HOME.INTERPOLATIONS.RECENT }}
        </div>
        <CardSlider api="seasons/now" />
      </section>
    </div>
  </q-page>
</template>

<script setup>
import CardSlider from '../components/CardSlider.vue'
import useComputes from 'src/common/composables/useComputes'

import { scroll } from 'quasar'
import { onMounted, ref } from 'vue'
import { archivesApi } from 'src/boot/axios'

const { getScrollTarget, setVerticalScrollPosition } = scroll

const { MAP } = useComputes()

const upcomin = ref(null)
const toprated = ref(null)
const recent = ref(null)

function scrollToElement (el) {
  // @description takes an element object
  const target = getScrollTarget(el)
  const offset = el.offsetTop
  const duration = 500
  setVerticalScrollPosition(target, offset, duration)
}

onMounted(() => {
  archivesApi.get('watchlist/get-playlists/')
})

</script>

<style lang="scss" scoped>
.nav-tabs{
  max-width:50vw;
}
.section-label{
  letter-spacing:0.2em
}
</style>

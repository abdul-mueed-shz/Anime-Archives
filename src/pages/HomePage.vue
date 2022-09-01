<!-- eslint-disable no-unused-vars -->
<template>
  <q-page
    padding
    class="bg-black text-white"
  >
    <div class="column">
      <div class="row q-ma-md flex-center">
        <q-tabs
          inline-label
          outside-arrows
          mobile-arrows
          style="width:80vw"
        >
          <q-tab
            icon="home"
            name="toprated"
            label="Top Rated"
            @click="scrollToElement(toprated)"
          />
          <q-tab
            icon="person"
            name="watched"
            label="Most Watched"
            @click="scrollToElement(recent)"
          />
          <q-tab
            icon="person"
            name="upcoming"
            label="Upcoming"
            @click="scrollToElement(upcomin)"
          />
        </q-tabs>
      </div>
      <div class="q-mb-lg">
        <div
          class="flex flex-center text-h6 text-weight-bold"
          style="letter-spacing:0.2em"
          ref="toprated"
        >
          Top Rated
        </div>
        <CardSlider api="https://api.jikan.moe/v4/top/anime" />
      </div>
      <div class="q-mb-lg">
        <div
          class="flex flex-center text-h6 text-weight-bold"
          style="letter-spacing:0.2em"
          ref="recent"
        >
          Recent Release
        </div>
        <CardSlider api="https://api.jikan.moe/v4/seasons/now" />
      </div>
      <div class="q-mb-lg">
        <div
          class="flex flex-center text-h6 text-weight-bold"
          style="letter-spacing:0.2em"
          ref="upcomin"
        >
          Upcoming Hype
        </div>
        <CardSlider api="https://api.jikan.moe/v4/seasons/upcoming" />
      </div>
    </div>
  </q-page>
</template>

<script setup>
import CardSlider from '../components/CardSlider.vue'
import { scroll } from 'quasar'
import { ref } from 'vue'
const { getScrollTarget, setVerticalScrollPosition } = scroll
const upcomin = ref(null)
const toprated = ref(null)
const recent = ref(null)
// takes an element object
function scrollToElement (el) {
  const target = getScrollTarget(el)
  const offset = el.offsetTop
  const duration = 500
  setVerticalScrollPosition(target, offset, duration)
}
</script>

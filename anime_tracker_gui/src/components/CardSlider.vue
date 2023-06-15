<template>
  <div class="row">
    <div class="flex flex-center">
      <q-btn
        round
        color="primary"
        icon="arrow_left"
        class="q-mr-sm gt-xs"
        @click="animateScroll('left')"
      />
    </div>
    <div class="col">
      <q-scroll-area
        ref="scrollAreaRef"
        :bar-style="animeSectionConfs.scrollerBarStyle"
        :thumb-style="animeSectionConfs.scrollerThumbStyle"
        class="anime__section-scrollarea"
      >
        <div class="row no-wrap">
          <div
            v-for="anime in animeList.value"
            :key="anime"
            class="q-pa-sm anime__card-width"
          >
            <q-card
              :class="{'card-border':!$q.dark.isActive}"
              class="shdaow-24 full-height my-background card-confs cursor-pointer"
              @click="goToPage(anime.mal_id)"
            >
              <q-card-section>
                <q-img
                  class="anime__card-img"
                  :src="anime.images.jpg.large_image_url"
                />
              </q-card-section>
              <q-separator
                class="bg-grey-6"
                inset
              />
              <q-card-section>
                <div class="text-h6">
                  {{ anime.title_english }}
                </div>
                <div class="text-body2 ellipsis-3-lines">
                  {{ anime.synopsis }}
                </div>
                <br>
                <div class="text-subtitle">
                  {{ MAP.DETAILS.INTERPOLATIONS.RELEASE_YEAR }}{{ MAP.DETAILS.INTERPOLATIONS.SEPARATOR }} <strong>{{ anime.year }}</strong>
                </div>
              </q-card-section>
            </q-card>
          </div>
        </div>
      </q-scroll-area>
    </div>
    <div class="flex flex-center">
      <q-btn
        round
        color="primary"
        class="q-ml-sm gt-xs"
        icon="arrow_right"
        @click="animateScroll('right')"
      />
    </div>
  </div>
</template>

<script setup>
import { ref, reactive } from 'vue'
import { useRouter } from 'vue-router'
import { jikanApi } from 'src/boot/axios'
import { ROUTE_CONSTS } from 'src/common/constants/routes'
import useComputes from 'src/common/composables/useComputes'

const router = useRouter()
const { MAP } = useComputes()
const props = defineProps({
  api: {
    type: String,
    default: ''
  }
})

let position = 0
const scrollAreaRef = ref(null)
const animeList = reactive({
  value: []
})
const animeSectionConfs = reactive({
  scrollerBarStyle: { backgroundColor: 'teal', opacity: '0.1' },
  scrollerThumbStyle: { background: 'teal', opacity: '0.9' }
})

jikanApi.get(props.api)
  .then(res => { animeList.value = res.data.data })
  .catch(err => console.error(err))

function goToPage (animeId) {
  router.push(`${ROUTE_CONSTS.DETAILS.PATH}${animeId}`)
}
function animateScroll (direction) {
  const pos = scrollAreaRef.value.getScrollPercentage().left
  if (direction === 'right' && pos < 1) {
    position += 1000
  } else if (direction === 'left' && pos > 0) {
    position -= 1000
  }
  scrollAreaRef.value.setScrollPosition('horizontal', position, 300)
}
</script>

<style lang="scss">
.anime__section-scrollarea{
  height: 500px;
}
.anime__card-width{
  width: 300px
}
.anime__card-img{
  height: 170px;
  object-fit: cover;
}

</style>

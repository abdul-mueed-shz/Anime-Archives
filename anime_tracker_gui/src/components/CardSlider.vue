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
        :bar-style="{backgroundColor:'teal',opacity:'0.1'}"
        :thumb-style="{background:'teal',opacity:'0.9'}"
        style="height: 500px;"
      >
        <div class="row no-wrap">
          <div
            v-for="anime in animeList.value"
            :key="anime"
            style="width: 300px"
            class="q-pa-sm"
          >
            <q-card
              @click="goToPage(anime.mal_id)"
              class="full-height my-background card-confs"
            >
              <q-card-section>
                <q-img
                  style="
                  height: 170px;
                  object-fit: cover;
                  "
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
                  Release Year: <strong>{{ anime.year }}</strong>
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
import axios from 'axios'
import { useRouter } from 'vue-router'

const router = useRouter()
let position = 0
const props = defineProps({
  api: {
    type: String, default: ''
  }
}
)
const animeList = reactive({
  value: []
})
axios.get(props.api)
  .then(res => { animeList.value = res.data.data })
  .catch(err => console.error(err))

function goToPage (animeId) {
  router.push(`/card/${animeId}`)
}
const scrollAreaRef = ref(null)
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
  .my-background{
    background-color: #1b1b1b;
  }
  .my-background:hover{
    background-color: $primary;
  }

  </style>

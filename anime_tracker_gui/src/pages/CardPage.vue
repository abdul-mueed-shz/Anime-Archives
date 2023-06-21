<template>
  <q-page
    :class="{'padding_6rem':$q.screen.gt.md,}"
    padding
  >
    <section
      class="row"
      :class="{'q-gutter-x-md':$q.screen.gt.sm,}"
    >
      <q-card
        :class="lightCardBorder"
        class="col-12 col-md-3 q-pa-md card-confs q-mt-sm"
      >
        <q-img
          :src="animeInformation.value.images?.jpg?.large_image_url ?? APP_CONSTS.PLACEHOLDERS.CARD_PAGE.ANIME_IMG"
          class="anime-display-picture"
        />
        <div class="div q-mt-md">
          <strong>{{ MAP.DETAILS.INTERPOLATIONS.SCORE }}{{ MAP.DETAILS.INTERPOLATIONS.SEPARATOR }} </strong>{{ animeInformation.value.score }}
        </div>
        <div class="div">
          <strong>{{ MAP.DETAILS.INTERPOLATIONS.YEAR }}{{ MAP.DETAILS.INTERPOLATIONS.SEPARATOR }} </strong>{{ animeInformation.value.year }}
        </div>
        <div class="div">
          <strong>{{ MAP.DETAILS.INTERPOLATIONS.RANK }}{{ MAP.DETAILS.INTERPOLATIONS.SEPARATOR }} </strong>{{ animeInformation.value.rank }}
        </div>
        <div class="div">
          <strong>{{ MAP.DETAILS.INTERPOLATIONS.AIRING }}{{ MAP.DETAILS.INTERPOLATIONS.SEPARATOR }} </strong>{{ animeInformation.value.airing }}
        </div>
        <div class="div">
          <strong>{{ MAP.DETAILS.INTERPOLATIONS.AIRED }}{{ MAP.DETAILS.INTERPOLATIONS.SEPARATOR }}</strong> {{ MAP.DETAILS.INTERPOLATIONS.FROM }} {{ aired.from }} {{ MAP.DETAILS.INTERPOLATIONS.TO }} {{ aired.to }}
        </div>
        <div class="div">
          <strong>{{ MAP.DETAILS.INTERPOLATIONS.SEASON }}{{ MAP.DETAILS.INTERPOLATIONS.SEPARATOR }} </strong>{{ animeInformation.value.season }}
        </div>
        <div class="row">
          <strong>{{ MAP.DETAILS.INTERPOLATIONS.GENRE }}{{ MAP.DETAILS.INTERPOLATIONS.SEPARATOR }}</strong>
          <div
            v-for="genre in animeInformation.value.genres"
            :key="genre.mal_id"
            class="row"
          >
            {{ genre.name }},
          </div>
        </div>
        <div class="row">
          <strong>{{ MAP.DETAILS.INTERPOLATIONS.STUDIOS }}{{ MAP.DETAILS.INTERPOLATIONS.SEPARATOR }}</strong>
          <div
            v-for="studio in animeInformation.value.studios"
            :key="studio.mal_id"
            class="row"
          >
            {{ studio.name }},
          </div>
        </div>
        <div class="div">
          <strong>{{ MAP.DETAILS.INTERPOLATIONS.FAV }}{{ MAP.DETAILS.INTERPOLATIONS.SEPARATOR }} </strong>{{ animeInformation.value.favorites }}
        </div>
      </q-card>
      <div class="col-12 col-md q-mt-sm">
        <q-card
          :class="lightCardBorder"
          class="full-height q-pa-sm  q-my-xs overflow-auto card-confs anime-description"
        >
          <q-card-section class="flex flex-center text-h6 text-weight-bolder">
            {{ animeInformation.value.title_english }}
          </q-card-section>
          <q-card-section class="flex flex-center text-body2">
            {{ animeInformation.value.synopsis }}
          </q-card-section>
        </q-card>
      </div>
      <q-card
        :class="lightCardBorder"
        class="col-12 col-md-3 q-pa-md card-confs q-mt-md"
      >
        <q-video
          :src="animeInformation.value.trailer?.embed_url ?? APP_CONSTS.PLACEHOLDERS.CARD_PAGE.ÁNIME_TRAILER"
          class="anime-trailer"
        />
        <q-card class="q-ma-md">
          <q-card-actions align="center">
            <q-btn
              label="Add to watchlist"
              icon="add"
              color="primary"
              class="border-radius__8px"
              @click="addToWatchlist"
            />
          </q-card-actions>
          <div v-if="false">
            <q-separator
              inset
              color="grey-6"
              class="q-mt-md"
            />
            <q-card-section class="text-bold">
              {{ MAP.DETAILS.INTERPOLATIONS.RECOMMENDATIONS }}
            </q-card-section>
            <q-separator
              inset
              color="grey-6"
            />
            <q-card-section>
              <div class="column">
                <q-btn
                  dense
                  label="Gintama"
                  color="secondary"
                  class="q-mb-sm border-radius__8px"
                  outline
                />
                <q-btn
                  dense
                  label="Gintama"
                  color="secondary"
                  class="q-mb-sm border-radius__8px"
                  outline
                />
                <q-btn
                  dense
                  label="Gintama"
                  color="secondary"
                  class="q-mb-sm border-radius__8px"
                  outline
                />
              </div>
            </q-card-section>
          </div>
        </q-card>
      </q-card>
    </section>
  </q-page>
</template>

<script setup>
import useComputes from 'src/common/composables/useComputes'
import useUtility from 'src/common/composables/useUtility'
import { jikanApi } from 'src/boot/axios'
import { computed, reactive, ref } from 'vue'
import { useRoute } from 'vue-router'
import { APP_CONSTS } from '../common/constants/app'
import { useStore } from 'vuex'
import { useQuasar } from 'quasar'
import WatchlistDialog from 'src/components/WatchlistDialog.vue'

const store = useStore()
const $q = useQuasar()
const animeId = useRoute().params.id
const { MAP, isDarkMode } = useComputes()
const { errorNotif } = useUtility()
const lightCardBorder = { 'card-border': !isDarkMode.value }

const animeInformation = reactive({
  value: {}
})

const aired = reactive({
  from: undefined,
  to: undefined
})
const watchlistDialogRef = ref(null)

const isLoggedIn = computed(() => store.getters['auth/isLoggedIn'])

const addToWatchlist = () => {
  if (isLoggedIn.value) {
    watchlistDialogRef.value = $q.dialog({
      component: WatchlistDialog,
      componentProps: {}
    }).onOk((res) => {
      console.log(res)
    })
  }
}

jikanApi.get(`anime/${animeId}/full`)
  .then(
    result => {
      animeInformation.value = result.data.data
      aired.from = new Date(animeInformation.value.aired.from)
      aired.to = new Date(animeInformation.value.aired.to)
      aired.from = aired.from.getUTCFullYear() + '/' + (aired.from.getUTCMonth() + 1) + '/' + aired.from.getUTCDate()
      aired.to = aired.to.getUTCFullYear() + '/' + (aired.to.getUTCMonth() + 1) + '/' + aired.to.getUTCDate()
    }
  )
  .catch(error => errorNotif(error))
</script>

<style scoped lang="scss">
.border-radius__8px{
  border-radius: 8px;
}
.anime-display-picture{
  max-height:350px;
  object-fit:contain
}
.anime-description{
  max-height:95vh
}
.anime-trailer{
  // max-width:fit-content;
  object-fit: contain;
  margin-left:auto;
  margin-right:auto;
}
</style>

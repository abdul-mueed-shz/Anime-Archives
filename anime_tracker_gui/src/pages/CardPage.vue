<template>
  <q-page class="row text-white bg-black">
    <q-card class="col-12 col-sm-3 bg-grey-10 q-ma-sm q-pa-md">
      <q-img
        :src="animeInformation.value.images?.jpg?.large_image_url ?? 'https://picsum.photos/1920/1080'"
        style="max-height:350px"
      />
      <div class="div q-mt-md">
        <strong>Score: </strong>{{ animeInformation.value.score }}
      </div>
      <div class="div">
        <strong>Year: </strong>{{ animeInformation.value.year }}
      </div>
      <div class="div">
        <strong>Rank: </strong>{{ animeInformation.value.rank }}
      </div>
      <div class="div">
        <strong>Airing: </strong>{{ animeInformation.value.airing }}
      </div>
      <div class="div">
        <strong>Aired:</strong> from {{ aired.from }} to {{ aired.to }}
      </div>
      <div class="div">
        <strong>Season: </strong>{{ animeInformation.value.season }}
      </div>
      <div class="row">
        <strong>Genre:</strong>
        <div
          v-for="genre in animeInformation.value.genres"
          :key="genre.mal_id"
          class="row"
        >
          {{ genre.name }},
        </div>
      </div>
      <div class="row">
        <strong>Studios:</strong>
        <div
          v-for="studio in animeInformation.value.studios"
          :key="studio.mal_id"
          class="row"
        >
          {{ studio.name }},
        </div>
      </div>
      <div class="div">
        <strong>Favorites: </strong>{{ animeInformation.value.favorites }}
      </div>
    </q-card>
    <div class="col-12 col-sm">
      <q-card
        class=" col-12 col-sm bg-dark full-height q-pa-sm q-mx-xs q-my-xs overflow-auto"
        style="max-height:95vh"
      >
        <q-card-section class="flex flex-center text-h6 text-weight-bolder">
          {{ animeInformation.value.title_english }}
        </q-card-section>
        <q-card-section class="flex flex-center text-body2">
          {{ animeInformation.value.synopsis }}
        </q-card-section>
      </q-card>
    </div>
    <q-card class="col-12 col-sm-3 bg-grey-10 q-ma-sm q-pa-md">
      <q-video
        :src="animeInformation.value.trailer?.embed_url ?? 'https://www.youtube.com/embed?v=Xi_xB3a2NZg'"
        style="max-width:fit-content; margin-left:auto; margin-right:auto;"
      />
      <q-card class="bg-grey-9 q-ma-md">
        <q-card-section class="text-bold">
          Suggestions
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
              color="primary"
              class="q-mb-sm"
            />
            <q-btn
              dense
              label="Gintama"
              color="primary"
              class="q-mb-sm"
            />
            <q-btn
              dense
              label="Gintama"
              color="primary"
              class="q-mb-sm"
            />
          </div>
        </q-card-section>
      </q-card>
    </q-card>
  </q-page>
</template>

<script setup>
import axios from 'axios'
import { reactive } from 'vue'
import { useRoute } from 'vue-router'

const animeId = useRoute().params.id
const animeInformation = reactive({
  value: {}
})
const aired = reactive({
  from: undefined,
  to: undefined
})
axios.get(`https://api.jikan.moe/v4/anime/${animeId}/full`)
  .then(
    result => {
      animeInformation.value = result.data.data
      aired.from = new Date(animeInformation.value.aired.from)
      aired.to = new Date(animeInformation.value.aired.to)
      aired.from = aired.from.getUTCFullYear() + '/' + (aired.from.getUTCMonth() + 1) + '/' + aired.from.getUTCDate()
      aired.to = aired.to.getUTCFullYear() + '/' + (aired.to.getUTCMonth() + 1) + '/' + aired.to.getUTCDate()
      console.log(animeInformation.value)
    }
  )
  .catch(error => console.log(error))
</script>

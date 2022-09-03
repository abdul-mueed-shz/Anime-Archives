<template>
  <q-layout
    view="hHh Lpr lff"
  >
    <q-header class="bg-black">
      <q-toolbar>
        <q-btn
          flat
          dense
          round
          icon="menu"
          aria-label="Menu"
          @click="toggleLeftDrawer"
        />

        <q-toolbar-title
          @click="$router.push('/')"
          class="text-primary text-bold my-clickable"
        >
          Anime Tracker Application
        </q-toolbar-title>
        <div>
          <q-select
            class="q-ml-md q-pa-sm"
            dark
            square
            dense
            outlined
            v-model="selectedQuery"
            placeholder="Search"
            use-input
            hide-dropdown-icon
            input-debounce="500"
            :options="options"
            option-label="title_english"
            @filter="filterFn"
            @update:model-value="goToPage(selectedQuery.mal_id)"
          >
            <template #no-option>
              <q-item>
                <q-item-section class="text-grey">
                  No results
                </q-item-section>
              </q-item>
            </template>
            <template #prepend>
              <q-icon name="search" />
            </template>
          </q-select>
        </div>
      </q-toolbar>
    </q-header>

    <q-drawer
      v-model="leftDrawerOpen"
      :show-if-above="false"
      class="bg-dark"
    />

    <q-page-container>
      <router-view :key="$route.fullPath" />
    </q-page-container>

    <q-footer class="bg-black q-pt-sm">
      <div class=" flex flex-center q-pa-xs">
        <q-btn
          round
          flat
          size="xs"
          class="q-mr-sm"
        >
          <q-avatar>
            <q-img
              style="width:40px"
              src="../assets/lkdn.png"
            />
          </q-avatar>
        </q-btn>
        <q-btn
          round
          flat
          size="xs"
          class="q-mr-sm"
        >
          <q-avatar>
            <q-img src="../assets/insta.png" />
          </q-avatar>
        </q-btn>
        <q-btn
          round
          flat
          size="xs"
          class="q-mr-sm"
        >
          <q-avatar>
            <q-img src="../assets/fbwhite.png" />
          </q-avatar>
        </q-btn>
        <q-btn
          round
          flat
          size="xs"
          class="q-mr-sm"
        >
          <q-avatar>
            <q-img src="../assets/github.png" />
          </q-avatar>
        </q-btn>
      </div>
      <div class="flex flex-center">
        <div class="text-h6">
          Copied with <span class="text-primary">&hearts;</span> by <strong>Abdul Mueed</strong>
        </div>
      </div>
    </q-footer>
  </q-layout>
</template>

<script setup>
import axios from 'axios'
import { ref } from 'vue'
import { useRouter } from 'vue-router'
const router = useRouter()
const leftDrawerOpen = ref(false)
const selectedQuery = ref('')
const stringOptions = []
const options = ref(stringOptions)
function filterFn (query, update, abort) {
  if (query.length < 2) {
    abort()
    return
  }
  update(() => {
    const needle = query.toLowerCase()
    axios.get(`https://api.jikan.moe/v4/anime?q=${needle}`)
      .then(result => { options.value = result.data.data.filter((val) => { return val.title_english != null }) })
      .catch(error => console.log(error))
  })
}
function goToPage (animeId) {
  router.push(`/card/${animeId}`)
  selectedQuery.value = ''
}
function toggleLeftDrawer () {
  leftDrawerOpen.value = !leftDrawerOpen.value
}

</script>

<style>
  .my-clickable{
    cursor: pointer;
  }
</style>

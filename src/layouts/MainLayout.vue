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
          @click="$router.push('/home')"
          class="text-primary text-bold my-clickable"
        >
          Anime Akaibu
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
            @filter="filterFn"
            @update:model-value="goToPage(selectedQuery.mal_id)"
          >
            <template #option="scope">
              <q-item v-bind="scope.itemProps">
                <q-item-section avatar>
                  <q-img :src="scope.opt.images.jpg.image_url" />
                </q-item-section>
                <q-item-section>
                  <q-item-label>{{ scope.opt.title_english }}</q-item-label>
                  <q-item-label caption>
                    {{ scope.opt.type }} <br>
                    {{ scope.opt.score }} <br>
                    {{ scope.opt.status }} <br>
                    {{ scope.opt.year }} <br>
                  </q-item-label>
                </q-item-section>
              </q-item>
            </template>
            <template #no-option>
              <div class="flex flex-center q-pa-md">
                <q-spinner-pie
                  size="md"
                  color="primary"
                />
              </div>
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
          href="https://www.linkedin.com/in/abdul-mueed-shahbaz-8455b618a/"
          target="_blank"
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
          href="https://www.instagram.com/al_mo_eed/"
          target="_blank"
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
          href="https://www.facebook.com/moeedrajpootx/"
          target="_blank"
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
          href="https://github.com/Abdul-Mueed-Shahbaz"
          target="_blank"
        >
          <q-avatar>
            <q-img src="../assets/github.png" />
          </q-avatar>
        </q-btn>
      </div>
      <div class="flex flex-center q-my-sm">
        <div class="text-caption">
          <q-icon
            size="xs"
            color="white"
            name="mail"
          />
          <a
            style="text-decoration:none; color:white;"
            class="q-ml-xs "
            href="mailto: abdulmueedshahbaz@gmail.com"
          >abdulmueedshahbaz@gmail.com</a>
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

<style lang="scss">

  .my-clickable{
    cursor: pointer;
  }
    /* width */
    ::-webkit-scrollbar {
    width: 11px;
    background-color: black;
  }

  /* Track */
  ::-webkit-scrollbar-track {
    box-shadow: inset 0 0 5px rgb(26, 26, 26);
    border-radius: 5.5px;
  }

  /* Handle */
  ::-webkit-scrollbar-thumb {
    background: $primary;
    border-radius: 6px;
  }

  /* Handle on hover */
  ::-webkit-scrollbar-thumb:hover {
    background: #a50000;
  }
</style>

<template>
  <q-layout view="hHh Lpr lff">
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
          class="text-primary text-bold"
        >
          <div
            class="my-clickable"
            @click="$router.push(ROUTE_CONSTS.HOME.PATH)"
          >
            {{ MAP.COMMON.INTERPOLATIONS.APP_TITLE }}
          </div>
        </q-toolbar-title>
        <div class="row items-center q-pt-xs">
          <div>
            <q-select
              class="q-pa-sm"
              dark
              rounded
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
          <div>
            <q-avatar
              class="cursor-pointer"
              icon="person"
              color="primary"
              size="md"
              @click="$router.push(ROUTE_CONSTS.LOGIN.PATH)"
            >
              <q-tooltip>
                {{ MAP.COMMON.TOOLTIPS.LOGIN }}
              </q-tooltip>
            </q-avatar>
          </div>
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
          :href="APP_CONSTS.CREATOR_INFO.LNKDN"
          :target="APP_CONSTS.CREATOR_INFO.TARGET_ACTION"
        >
          <q-avatar>
            <q-img
              class="creator-info__img"
              src="../assets/lkdn.png"
            />
          </q-avatar>
        </q-btn>
        <q-btn
          round
          flat
          size="xs"
          class="q-mr-sm"
          :href="APP_CONSTS.CREATOR_INFO.INSTA"
          :target="APP_CONSTS.CREATOR_INFO.TARGET_ACTION"
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
          :href="APP_CONSTS.CREATOR_INFO.FB"
          :target="APP_CONSTS.CREATOR_INFO.TARGET_ACTION"
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
          :href="APP_CONSTS.CREATOR_INFO.GITHUB"
          :target="APP_CONSTS.CREATOR_INFO.TARGET_ACTION"
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
            class="q-ml-xs creator-info__email-anchor"
            :href="`mailto: ${APP_CONSTS.CREATOR_INFO.EMAIL}`"
          >{{ MAP.COMMON.INTERPOLATIONS.EMAIL }}</a>
        </div>
      </div>
    </q-footer>
  </q-layout>
</template>

<script setup>
import { jikanApi } from 'src/boot/axios'
import useComputes from 'src/common/composables/useComputes'
import { APP_CONSTS } from 'src/common/constants/app'
import { ROUTE_CONSTS } from 'src/common/constants/routes'
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

const { MAP } = useComputes()

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
    jikanApi.get('anime', {
      params: {
        q: needle
      }
    })
      .then(result => { options.value = result.data.data.filter((val) => { return val.title_english != null }) })
      .catch(error => console.error(error))
  })
}
function goToPage (animeId) {
  router.push(`${ROUTE_CONSTS.DETAILS.PATH}${animeId}`)
  selectedQuery.value = ''
}
function toggleLeftDrawer () {
  leftDrawerOpen.value = !leftDrawerOpen.value
}

</script>

<style lang="scss">
.creator-info__email-anchor{
  text-decoration:none; color:white;
}
.creator-info__img{
  width:40px
}
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

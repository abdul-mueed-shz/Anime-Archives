<template>
  <q-layout view="hHh Lpr lff">
    <q-header>
      <q-toolbar :class="{'bg-dark':$q.dark.isActive}">
        <q-btn
          flat
          dense
          round
          icon="menu"
          aria-label="Menu"
          @click="drawer = !drawer"
        />

        <q-toolbar-title
          class="text-bold"
        >
          <div
            class="my-clickable"
            @click="$router.push(ROUTE_CONSTS.HOME.PATH)"
          >
            {{ MAP.COMMON.INTERPOLATIONS.APP_TITLE }}
          </div>
        </q-toolbar-title>
        <div class="row items-center q-pt-xs">
          <div :style="{display: $q.screen.lt.sm? 'none': null }">
            <q-select
              ref="animeSearchRef"
              class="q-pa-sm"
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
                <q-icon
                  color="white"
                  name="search"
                />
              </template>
            </q-select>
          </div>
          <div :style="{display: $q.screen.lt.sm? 'inline': 'none' }">
            <q-btn
              flat
              dense
              icon="search"
              round
              @click="check"
            />
          </div>
          <div>
            <q-btn
              v-if="authDetails.tokens.access"
              color="secondary"
              icon="person"
              size="sm"
              round
            >
              <q-menu>
                <div
                  style="width:400px"
                  class="row no-wrap q-pa-md"
                  :class="{'card-border':!$q.dark.isActive}"
                >
                  <div class="column">
                    <div class="text-h6 text-primary text-weight-medium">
                      Account Details
                    </div>
                    <div class="row">
                      <div class="text-primary text-weight-bolder q-pr-xs">
                        Email:
                      </div>
                      <div>
                        {{ authDetails.userProfile.email }}
                      </div>
                    </div>
                    <div class="row">
                      <div class="text-primary text-weight-bolder q-pr-xs">
                        DOB:
                      </div>
                      <div>
                        {{ authDetails.userProfile.date_of_birth }}
                      </div>
                    </div>
                  </div>

                  <q-separator
                    vertical
                    inset
                    class="q-mx-lg"
                  />

                  <div class="column items-center">
                    <!-- <q-avatar size="72px">
                      <img src="https://cdn.quasar.dev/img/avatar4.jpg">
                    </q-avatar> -->

                    <div class="text-subtitle1 text-weight-bolder ellipsis">
                      Username
                    </div>
                    <div class="text-subtitle1 q-mb-xs ellipsis">
                      {{ authDetails.userProfile.user_name }}
                    </div>

                    <q-btn
                      color="primary"
                      label="Logout"
                      push
                      size="sm"
                      @click="logout"
                      v-close-popup
                    />
                  </div>
                </div>
              </q-menu>
            </q-btn>
            <q-btn
              v-else
              class="cursor-pointer"
              icon="login"
              flat
              round
              @click="$router.push(ROUTE_CONSTS.LOGIN.PATH)"
            >
              <q-tooltip>
                {{ MAP.COMMON.TOOLTIPS.LOGIN }}
              </q-tooltip>
            </q-btn>
          </div>
        </div>
      </q-toolbar>
    </q-header>

    <q-drawer
      v-model="drawer"
      show-if-above
      :class="{'light-border-right':!$q.dark.isActive}"
      :mini="!drawer || miniState"
      @click.capture="drawerClick"
      :width="200"
      :breakpoint="500"
    >
      <q-scroll-area
        class="fit"
        :horizontal-thumb-style="{ opacity: 0 }"
      >
        <q-list padding>
          <q-item
            clickable
            v-ripple
            @click="$router.replace(ROUTE_CONSTS.HOME.PATH)"
          >
            <q-item-section avatar>
              <q-icon name="dashboard" />
            </q-item-section>

            <q-item-section>
              Dashboard
            </q-item-section>
          </q-item>
          <q-item
            clickable
            v-ripple
          >
            <q-item-section avatar>
              <q-icon name="account_circle" />
            </q-item-section>

            <q-item-section>
              Account
            </q-item-section>
          </q-item>
          <q-item
            clickable
            v-ripple
          >
            <q-item-section avatar>
              <q-icon name="wallpaper" />
            </q-item-section>

            <q-item-section>
              Wall
            </q-item-section>
          </q-item>
          <q-item
            clickable
            v-ripple
            @click="$router.push(ROUTE_CONSTS.WATCHLIST.PATH)"
          >
            <q-item-section avatar>
              <q-icon name="view_list" />
            </q-item-section>

            <q-item-section>
              Watchlist
            </q-item-section>
          </q-item>
          <q-item
            clickable
            v-ripple
          >
            <q-item-section avatar>
              <q-icon name="groups" />
            </q-item-section>

            <q-item-section>
              Friends
            </q-item-section>
          </q-item>
          <q-item
            clickable
            v-ripple
          >
            <q-item-section avatar>
              <q-icon name="settings" />
            </q-item-section>

            <q-item-section>
              Settings
            </q-item-section>
          </q-item>
        </q-list>
      </q-scroll-area>

      <!--
          in this case, we use a button (can be anything)
          so that user can switch back
          to mini-mode
        -->
      <div
        class="q-mini-drawer-hide absolute"
        style="top: 15px; right: -17px"
      >
        <q-btn
          dense
          round
          unelevated
          color="secondary"
          icon="chevron_left"
          @click="miniState = true"
        />
      </div>
    </q-drawer>

    <q-page-container>
      <router-view :key="$route.fullPath" />
    </q-page-container>

    <q-footer class="q-pt-sm">
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
import useUtility from 'src/common/composables/useUtility'
import { APP_CONSTS } from 'src/common/constants/app'
import { ROUTE_CONSTS } from 'src/common/constants/routes'
import { computed, ref } from 'vue'
import { useRouter } from 'vue-router'
import { useStore } from 'vuex'
import { useQuasar } from 'quasar'

const drawer = ref(false)
const miniState = ref(false)

function drawerClick (e) {
  if (miniState.value) {
    miniState.value = false
    e.stopPropagation()
  }
}

const router = useRouter()
const store = useStore()
const $q = useQuasar()

$q.dark.set(true)

const authDetails = computed(() => store.getters['auth/getAuthDetails'])

const { MAP } = useComputes()

const animeSearchRef = ref(null)
const selectedQuery = ref('')
const stringOptions = []
const options = ref(stringOptions)

const {
  successNotif,
  errorNotif
} = useUtility()

function logout () {
  store.dispatch('auth/logout').then(res => {
    successNotif(res.message)
  }).catch(err => errorNotif(err))
}

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
  // background-color: black;
}

/* Track */
::-webkit-scrollbar-track {
  // box-shadow: inset 0 0 5px rgb(26, 26, 26);
  border-radius: 5.5px;
}

/* Handle */
::-webkit-scrollbar-thumb {
  background: $primary;
  border-radius: 6px;
}

/* Handle on hover */
::-webkit-scrollbar-thumb:hover {
  background: $secondary;
}
</style>

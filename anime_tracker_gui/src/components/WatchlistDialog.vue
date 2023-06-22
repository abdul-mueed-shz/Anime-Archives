<template>
  <q-dialog
    ref="dialogRef"
    @hide="onDialogHide"
    persistent
  >
    <q-card
      class="q-dialog-plugin full-width"
    >
      <q-card-section v-if="!userWatchListRows || !userWatchListRows.length">
        <div class="q-pa-md">
          <q-markup-table>
            <thead>
              <tr>
                <th
                  class="text-left"
                  style="width: 150px"
                >
                  <q-skeleton
                    animation="blink"
                    type="text"
                  />
                </th>
                <th class="text-right">
                  <q-skeleton
                    animation="blink"
                    type="text"
                  />
                </th>
                <th class="text-right">
                  <q-skeleton
                    animation="blink"
                    type="text"
                  />
                </th>
                <th class="text-right">
                  <q-skeleton
                    animation="blink"
                    type="text"
                  />
                </th>
                <th class="text-right">
                  <q-skeleton
                    animation="blink"
                    type="text"
                  />
                </th>
                <th class="text-right">
                  <q-skeleton
                    animation="blink"
                    type="text"
                  />
                </th>
              </tr>
            </thead>

            <tbody>
              <tr
                v-for="n in 5"
                :key="n"
              >
                <td class="text-left">
                  <q-skeleton
                    animation="blink"
                    type="text"
                    width="85px"
                  />
                </td>
                <td class="text-right">
                  <q-skeleton
                    animation="blink"
                    type="text"
                    width="50px"
                  />
                </td>
                <td class="text-right">
                  <q-skeleton
                    animation="blink"
                    type="text"
                    width="35px"
                  />
                </td>
                <td class="text-right">
                  <q-skeleton
                    animation="blink"
                    type="text"
                    width="65px"
                  />
                </td>
                <td class="text-right">
                  <q-skeleton
                    animation="blink"
                    type="text"
                    width="25px"
                  />
                </td>
                <td class="text-right">
                  <q-skeleton
                    animation="blink"
                    type="text"
                    width="85px"
                  />
                </td>
              </tr>
            </tbody>
          </q-markup-table>
        </div>
      </q-card-section>
      <q-card-section v-else>
        <q-table
          selection="multiple"
          v-model:selected="selected"
          class="my-sticky-virtscroll-table q-ml-lg"
          style="height: 450px;"
          :rows="userWatchListRows"
          :columns="userWatchListColumns"
          flat
          bordered
          dense
          title-class="text-secondary text-weight-bolder"
          row-key="id"
          virtual-scroll
          :rows-per-page-options="[0]"
        >
          <template #top>
            <span class="text-secondary text-h6 text-weight-bolder">
              Watchlists
            </span>
            <q-space />
            <q-form @submit.prevent="createWatchlist">
              <div
                v-if="!addWatchlist"
              >
                <q-btn
                  icon="add"
                  color="positive"
                  size="sm"
                  round
                  @click="addWatchlist = !addWatchlist"
                >
                  <q-tooltip>
                    Create Wathlist
                  </q-tooltip>
                </q-btn>
              </div>
              <q-card
                v-if="addWatchlist"
                class="row q-pa-sm"
                bordered
              >
                <div class="column">
                  <div
                    class="text-weight-medium q-pb-xs"
                    style="font-size: smaller;"
                  >
                    <span class="text-negative">*</span>
                    Add Watchlist Name
                  </div>
                  <q-input
                    dense
                    label="Name"
                    outlined
                    v-model="watchlistData.name"
                    lazy-rules="ondemand"
                    :rules="[ val => val || 'Watchlist name is required']"
                    no-error-icon
                  />
                </div>
                <div class="column q-gutter-y-xs q-pl-sm q-pt-md">
                  <q-btn
                    type="submit"
                    label="Submit"
                    size="sm"
                    color="primary"
                    rounded
                    style="max-width:6rem"
                    @click="createWatchlist(watchlistData)"
                  />
                  <q-btn
                    size="sm"
                    rounded
                    label="Cancel"
                    color="negative"
                    style="max-width:6rem"
                    @click="addWatchlist = false"
                  >
                    <q-tooltip>
                      Cancel
                    </q-tooltip>
                  </q-btn>
                </div>
              </q-card>
            </q-form>
          </template>
          <template #header="props">
            <q-tr :props="props">
              <q-th
                key="selected"
                :props="props"
              >
                <q-checkbox
                  v-model="props.selected"
                  color="primary"
                />
              </q-th>
              <q-th
                v-for="col in props.cols.slice(1)"
                :key="col.name"
                :props="props"
              >
                <span
                  class="text-weight-bolder text-secondary"
                >{{ col.label }}</span>
              </q-th>
            </q-tr>
          </template>

          <template #body="props">
            <q-tr
              :props="props"
              @click="props.selected = true"
            >
              <q-td>
                <q-checkbox
                  v-model="props.selected"
                  color="primary"
                />
              </q-td>
              <q-td
                key="name"
                :props="props"
              >
                {{ props.row.name }}
              </q-td>
              <q-td
                key="anime_list"
                :props="props"
              >
                <q-btn
                  color="secondary"
                  flat
                  @click="props.expand = !props.expand"
                  :icon="props.expand ? 'expand_less' : 'list'"
                >
                  <q-tooltip v-if="!props.expand">
                    Anime list
                  </q-tooltip>
                </q-btn>
              </q-td>
              <q-td
                key="delete_Watchlist"
                :props="props"
              >
                <q-btn
                  icon="delete"
                  color="negative"
                  flat
                  @click="deleteWatchlist(props.row.id)"
                >
                  <q-tooltip>
                    Delete Watchlist
                  </q-tooltip>
                </q-btn>
              </q-td>
            </q-tr>
            <q-tr
              v-show="props.expand"
              :props="props"
            >
              <q-td colspan="100%">
                <q-table
                  style="border: 1px dotted grey;border-radius: 8px;"
                  :rows="props.row.anime_list"
                  :columns="animeListColumns"
                  dense
                  row-key="id"
                  virtual-scroll
                  :rows-per-page-options="[0]"
                >
                  <template #top>
                    <span
                      class="text-secondary text-weight-bolder"
                      style="font-size: medium;"
                    >
                      Anime List
                    </span>
                  </template>
                  <template #body="animeProps">
                    <q-tr :props="animeProps">
                      <q-td
                        key="anime"
                        :props="animeProps"
                      >
                        {{ animeProps.row.anime.name }}
                      </q-td>
                      <q-td
                        key="rating"
                        :props="animeProps"
                      >
                        {{ animeProps.row.rating }}
                      </q-td>
                      <q-td
                        key="review"
                        :props="animeProps"
                      >
                        <div v-if="animeProps.row.review">
                          <!-- <span>
                            {{ animeProps.row.review }}
                          </span> -->
                          <q-btn
                            icon="open_in_full"
                            color="secondary"
                            flat
                            size="sm"
                            @click="openReviewDialog(animeProps.row.review, animeProps.row.anime.name)"
                          />
                        </div>
                        <span
                          v-else
                          class="text-italic text-negative"
                        >
                          N/A
                        </span>
                      </q-td>
                      <q-td
                        key="delete"
                        :props="animeProps"
                      >
                        <q-btn
                          icon="delete"
                          color="negative"
                          flat
                          @click="deleteAnime(animeProps.row.id)"
                        >
                          <q-tooltip>
                            Delete Anime
                          </q-tooltip>
                        </q-btn>
                      </q-td>
                    </q-tr>
                  </template>
                </q-table>
              </q-td>
            </q-tr>
          </template>
        </q-table>
        <!-- v-model:pagination="pagination" -->
      </q-card-section>
      <q-card-actions align="right">
        <q-btn
          color="primary"
          label="OK"
          @click="onDialogOK"
        />
        <q-btn
          color="primary"
          label="Cancel"
          @click="onDialogCancel"
        />
      </q-card-actions>
    </q-card>
  </q-dialog>
</template>

<script setup>
import { useDialogPluginComponent, useQuasar } from 'quasar'
import { archivesApi } from 'src/boot/axios'
import { onMounted, ref } from 'vue'
import { useStore } from 'vuex'
import useUtility from '../common/composables/useUtility'
import ReviewDialog from './ReviewDialog.vue'

// eslint-disable-next-line no-unused-vars
const emits = defineEmits([...useDialogPluginComponent.emits])
const { dialogRef, onDialogHide, onDialogOK, onDialogCancel } = useDialogPluginComponent()
const { errorNotif, successNotif } = useUtility()

const store = useStore()
const $q = useQuasar()

const userWatchListRows = ref(null)

const userWatchListColumns = [
  {
    name: 'selected',
    label: 'Selected',
    align: 'left'
  },
  {
    name: 'name',
    required: true,
    label: 'Name',
    align: 'left',
    field: row => row.name,
    format: val => `${val}`,
    sortable: true
  },
  {
    name: 'anime_list',
    required: true,
    label: 'Anime List',
    align: 'left'
  },
  {
    name: 'delete_Watchlist',
    required: true,
    label: 'Delete',
    align: 'center'
  }
]
const animeListColumns = [
  {
    name: 'anime',
    required: true,
    label: 'Anime',
    align: 'left',
    field: row => row.anime.name,
    format: val => `${val}`,
    sortable: true
  },
  {
    name: 'rating',
    required: true,
    label: 'Rating',
    field: row => row.rating,
    format: val => `${val}`,
    sortable: true,
    align: 'left'
  },
  {
    name: 'review',
    required: true,
    label: 'Review',
    field: row => row.review,
    format: val => `${val ?? 'NA'}`,
    align: 'center'
  },
  {
    name: 'delete',
    label: 'Delete',
    align: 'center'
  }
]

const addWatchlist = ref(false)
const watchlistData = ref({
  name: null
})

const reviewDialogRef = ref(null)
const selected = ref([])

onMounted(() => {
  store.dispatch('auth/getUserWatchlists').then(res => {
    userWatchListRows.value = res
  })
})
const createWatchlist = (data) => {
  if (!watchlistData.value.name) { return }
  archivesApi.post('watchlist/', data).then(() => {
    successNotif('Successfully created the watchlist')
    addWatchlist.value = false
    store.dispatch('auth/getUserWatchlists').then(res => {
      userWatchListRows.value = res
    })
  }).catch(() => errorNotif('Unable to create the watchlist'))
}
const deleteWatchlist = (watchlistId) => {
  archivesApi.delete(`watchlist/${watchlistId}`).then(() => {
    successNotif('Successfully deleted the watchlist')
    store.dispatch('auth/getUserWatchlists').then(res => {
      userWatchListRows.value = res
    })
  }).catch(() => errorNotif('Unable to delete the watchlist'))
}
const deleteAnime = (watchlistAnimeId) => {
  archivesApi.delete(`watchlist-anime/${watchlistAnimeId}`).then(() => {
    successNotif('Successfully removed the anime from the watchlist')
    store.dispatch('auth/getUserWatchlists').then(res => {
      userWatchListRows.value = res
    })
  }).catch(() => errorNotif('Unable to removed the anime from the watchlist'))
}
const openReviewDialog = (review, anime) => {
  reviewDialogRef.value = $q.dialog({
    component: ReviewDialog,
    componentProps: {
      review, anime
    }
  }).onOk((res) => {
    console.log(res)
  })
}
</script>

<template>
  <q-dialog
    ref="dialogRef"
    @hide="onDialogHide"
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
          style="height: 400px"
          :rows="userWatchListRows"
          :columns="userWatchListColumns"
          flat
          bordered
          title="Watchlists"
          row-key="id"
          virtual-scroll
          :rows-per-page-options="[0]"
        >
          <template #header="props">
            <q-tr :props="props">
              <q-th
                v-for="col in props.cols"
                :key="col.name"
                :props="props"
              >
                {{ col.label }}
              </q-th>
            </q-tr>
          </template>

          <template #body="props">
            <q-tr :props="props">
              <q-td
                key="name"
                :props="props"
              >
                {{ props.row.name }}
              </q-td>
              <q-td
                key="is_active"
                :props="props"
              >
                <q-toggle :model-value="props.row.is_active" />
              </q-td>
              <q-td
                key="anime_list"
                :props="props"
              >
                <q-btn icon="list" />
              </q-td>
              <!-- <q-td
                v-for="col in props.cols"
                :key="col.name"
                :props="props"
              >
                {{ col.value }}
              </q-td> -->
              <!-- <q-td auto-width>
                <q-btn
                  size="sm"
                  color="accent"
                  round
                  dense
                  @click="props.expand = !props.expand"
                  :icon="props.expand ? 'remove' : 'add'"
                />
              </q-td> -->
            </q-tr>
            <q-tr
              v-show="props.expand"
              :props="props"
            >
              <q-td colspan="100%">
                <div class="text-left">
                  This is expand slot for row above: {{ props.row.name }}.
                </div>
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
import { useDialogPluginComponent } from 'quasar'
import { onMounted, ref } from 'vue'
import { useStore } from 'vuex'

// eslint-disable-next-line no-unused-vars
const emits = defineEmits([...useDialogPluginComponent.emits])
const { dialogRef, onDialogHide, onDialogOK, onDialogCancel } = useDialogPluginComponent()

const store = useStore()

const userWatchListRows = ref(null)

const userWatchListColumns = [
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
    name: 'is_active',
    required: true,
    label: 'Active',
    align: 'left',
    field: row => row.is_active,
    format: val => `${val}`,
    sortable: true
  },
  {
    name: 'anime_list',
    required: true,
    label: 'Anime List',
    align: 'left'
  }
]

onMounted(() => {
  store.dispatch('auth/getUserWatchlists').then(res => {
    userWatchListRows.value = res
  })
})

</script>

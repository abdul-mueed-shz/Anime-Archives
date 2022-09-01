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

        <q-toolbar-title class="text-primary text-bold">
          Anime Tracker Application
        </q-toolbar-title>

        <div>
          <!--  -->
          <q-input
            placeholder="Search"
            dark
            square
            dense
            filled
            v-model="text"
            input-class="text"
            class="q-ml-md"
          >
            <template #append>
              <q-icon
                v-if="text === ''"
                name="search"
              />
              <q-icon
                v-else
                name="clear"
                class="cursor-pointer"
                @click="text = ''"
              />
            </template>
          </q-input>
        </div>
      </q-toolbar>
    </q-header>

    <q-drawer
      v-model="leftDrawerOpen"
      :show-if-above="false"
      class="bg-dark"
    />

    <q-page-container>
      <router-view />
    </q-page-container>

    <q-footer class="bg-black">
      <div class=" flex flex-center q-pa-xs">
        <!-- <div class="q-mr-sm">
          &copy;socials:
        </div> -->
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
import { ref } from 'vue'

const leftDrawerOpen = ref(false)
const text = ref('')
function toggleLeftDrawer () {
  leftDrawerOpen.value = !leftDrawerOpen.value
}

</script>

<template>
  <q-page class="row bg-black">
    <div class="col-12 col-sm-8 flex-center flex q-pa-lg">
      <div
        class="full-width "
        style="max-width:400px"
      >
        <q-form @submit.prevent="SignIn">
          <q-card class="bg-dark">
            <q-card-section class="text-h4 text-weight-bold text-primary">
              Login
            </q-card-section>
            <q-card-section>
              <q-input
                dense
                dark
                label="Email"
                type="text"
                v-model="email"
                :rules="[ val => val && val.length > 0 || 'Email is required']"
                class="q-mb-md"
              >
                <template #prepend>
                  <q-icon name="mail" />
                </template>
              </q-input>
              <q-input
                dense
                dark
                label="Password"
                v-model="password"
                :rules="[ val => val && val.length > 0 || 'Email is required']"
                type="password"
                class="q-mb-md"
              >
                <template #prepend>
                  <q-icon name="lock" />
                </template>
              </q-input>
              <router-link
                class="flex justify-end text-white"
                to=""
              >
                Forgot Password
              </router-link>
            </q-card-section>
            <q-card-actions>
              <q-btn
                color="primary"
                class="full-width q-mb-sm"
                label="Login"
                type="submit"
              />
            </q-card-actions>
          </q-card>
        </q-form>
      </div>
    </div>
    <div class="gt-xs col-sm-4 bg-primary">
      <div class="full-height column flex-center">
        <q-img
          class="full-width"
          style="max-width:150px"
          src="../assets/anime2.png"
        />
        <div class="text-h5 text-white text-weight-bold q-mb-xl text-no-wrap">
          <span class="text-weight-bolder text-h4 text-secondary">W</span>elcome Senpai
        </div>
      </div>
    </div>
  </q-page>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
const email = ref('')
const password = ref('')

const $router = useRouter()
function SignIn () {
  $router.push('/home')
}
</script>

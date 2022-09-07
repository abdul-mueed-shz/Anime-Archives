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
                :rules="[ val => val && val.length > 8 || 'Password is required with a length of 8 characters']"
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
import Utility from 'src/composables/Utility'
const email = ref('')
const password = ref('')

const $router = useRouter()
function SignIn () {
  // eslint-disable-next-line no-useless-escape
  const regEx = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
  if (regEx.test(email.value)) {
    Utility.notify('Logged In', 'primary', 500, 'bottom')
    Utility.storage({ email: email.value, password: password.value })
    $router.push('/home')
    return
  }
  Utility.notify('Invalid Email', 'negative', 500, 'bottom')
}
</script>

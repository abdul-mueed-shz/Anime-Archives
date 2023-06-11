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
                lazy-rules="ondemand"
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
                lazy-rules="ondemand"
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
          <span class="text-weight-bolder text-h4 text-secondary">W</span>elcome to Akaibu
        </div>
      </div>
    </div>
  </q-page>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import useUtility from '../common/composables/useUtility'
import { ROUTE_CONSTS } from 'src/common/constants/routes'
import { APP_CONSTS } from 'src/common/constants/app'
import useComputes from 'src/common/composables/useComputes'

const $router = useRouter()

const { MAP } = useComputes()
const { successNotif, storage, errorNotif } = useUtility()

const email = ref(null)
const password = ref(null)

function SignIn () {
  if (APP_CONSTS.REGEX.VALID_EMAIL_CHECK.test(email.value)) {
    successNotif(MAP.value.AUTH.MESSAGES.LOGGED_IN)
    storage({ email: email.value, password: password.value })
    $router.push(ROUTE_CONSTS.HOME.PATH)
    return
  }
  errorNotif(MAP.value.ERRORS.AUTH.INVALID_EMAIL)
}
</script>

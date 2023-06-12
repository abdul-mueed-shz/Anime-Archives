<template>
  <q-page class="row bg-black">
    <div class="col-12 col-sm-8 flex-center flex q-pa-lg">
      <div
        class="full-width "
        style="max-width:400px"
      >
        <q-form @submit.prevent="authenticate">
          <q-card class="bg-dark">
            <q-card-section class="text-h4 text-weight-bold text-primary">
              <div v-if="auth.selectedAction===auth.login">
                Login
              </div>
              <div v-else-if="auth.selectedAction===auth.signup">
                Sign Up
              </div>
            </q-card-section>
            <q-card-section>
              <q-input
                v-if="auth.selectedAction===auth.signup"
                dense
                dark
                label="User Name"
                v-model="authForm.userName"
                clearable
                lazy-rules="ondemand"
                :rules="[ val => val && val.length > 0 || 'Username is required']"
              >
                <template #prepend>
                  <q-icon name="person" />
                </template>
              </q-input>
              <q-input
                dense
                dark
                label="Email"
                type="text"
                v-model="authForm.email"
                clearable
                lazy-rules="ondemand"
                :rules="[ val => val && val.length > 0 || 'Email is required']"
              >
                <template #prepend>
                  <q-icon name="mail" />
                </template>
              </q-input>
              <q-input
                v-if="auth.selectedAction===auth.signup"
                dense
                dark
                label="Date of Birth"
                v-model="authForm.dob"
                clearable
                readonly
                lazy-rules="ondemand"
                :rules="[ val => val && val.length > 0 || 'Date of Birth is required']"
              >
                <template #prepend>
                  <q-icon name="calendar_today" />
                </template>
                <template #append>
                  <q-icon
                    name="calendar_month"
                    class="cursor-pointer"
                  >
                    <q-popup-proxy
                      cover
                      :breakpoint="600"
                    >
                      <q-date
                        landscape
                        v-model="authForm.dob"
                      />
                    </q-popup-proxy>
                  </q-icon>
                </template>
              </q-input>
              <q-input
                dense
                dark
                label="Password"
                v-model="authForm.password"
                clearable
                lazy-rules="ondemand"
                :rules="[ val => val && val.length > 8 || 'Password is required with a length of 8 characters']"
                type="password"
              >
                <template #prepend>
                  <q-icon name="lock" />
                </template>
              </q-input>
              <q-input
                v-if="auth.selectedAction===auth.signup"
                dense
                dark
                label="Re-enter Password"
                v-model="authForm.password2"
                clearable
                lazy-rules="ondemand"
                :rules="[ val => val && val.length > 8 || 'Password Confirmation is required with a length of 8 characters']"
                type="password"
              >
                <template #prepend>
                  <q-icon name="lock" />
                </template>
              </q-input>

              <div class="flex justify-end text-white cursor-pointer">
                <div
                  v-if="auth.selectedAction===auth.login"
                  class="q-pr-xs q-pb-xs"
                >
                  Don't have an account?
                </div>
                <strong
                  @click="()=>auth.selectedAction=!auth.selectedAction"
                  style="text-decoration: underline;"
                ><span v-if="auth.selectedAction===auth.login">Sign Up</span><span v-else-if="auth.selectedAction===auth.signup"><q-icon
                  round
                  name="arrow_back"
                  color="primary"
                  size="md"
                >
                  <q-tooltip>
                    Login
                  </q-tooltip>
                </q-icon></span></strong>
              </div>
              <router-link
                v-if="auth.selectedAction===auth.login"
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
                :label="auth.selectedAction===auth.signup?'Sign Up': 'Login'"
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
const {
  // successNotif,
  // storage,
  errorNotif
} = useUtility()

const authForm = ref({
  email: null,
  password: null,
  password2: null,
  userName: null,
  dob: null
})

const auth = ref({
  login: false,
  signup: true,
  selectedAction: false
})

function authenticate () {
  if (APP_CONSTS.REGEX.VALID_EMAIL_CHECK.test(authForm.value.email)) {
    // successNotif(MAP.value.AUTH.MESSAGES.LOGGED_IN)
    // storage({ email: authForm.value.email, password: authForm.value.password })
    $router.push(ROUTE_CONSTS.HOME.PATH)
    return
  }
  errorNotif(MAP.value.ERRORS.AUTH.INVALID_EMAIL)
}
</script>

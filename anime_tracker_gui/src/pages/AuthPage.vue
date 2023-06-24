<template>
  <q-page class="row ">
    <div class="col-12 col-sm-8 flex-center flex q-pa-lg">
      <div
        class="full-width "
        style="max-width:400px"
      >
        <q-form @submit.prevent="authenticate">
          <q-card class="card-border">
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
                label="User Name"
                v-model="authForm.user_name"
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
                label="Date of Birth"
                v-model="authForm.date_of_birth"
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
                        v-model="authForm.date_of_birth"
                      />
                    </q-popup-proxy>
                  </q-icon>
                </template>
              </q-input>
              <q-input
                dense
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

              <div class="flex justify-end  cursor-pointer">
                <div
                  v-if="auth.selectedAction===auth.login"
                  class="q-pr-xs q-pb-xs"
                >
                  Don't have an account?
                </div>
                <strong
                  @click="()=>auth.selectedAction=!auth.selectedAction"
                  style="text-decoration: underline;"
                ><span v-if="auth.selectedAction===auth.login">Sign Up</span><span v-else-if="auth.selectedAction===auth.signup"><q-btn
                  round
                  icon="arrow_back"
                  color="primary"
                  size="md"
                >
                  <q-tooltip>
                    Login
                  </q-tooltip>
                </q-btn></span></strong>
              </div>
              <router-link
                v-if="auth.selectedAction===auth.login"
                class="flex justify-end "
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
        <div class="text-h5  text-weight-bold q-mb-xl text-no-wrap">
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
import { useStore } from 'vuex'

const $router = useRouter()
const store = useStore()

const { MAP } = useComputes()
const {
  successNotif,
  errorNotif
} = useUtility()

const authForm = ref({
  email: null,
  password: null,
  password2: null,
  user_name: null,
  date_of_birth: null
})

const auth = ref({
  login: false,
  signup: true,
  selectedAction: false
})
function authenticate () {
  if (!APP_CONSTS.REGEX.VALID_EMAIL_CHECK.test(authForm.value.email)) {
    return errorNotif(MAP.value.ERRORS.AUTH.INVALID_EMAIL)
  }
  const payload = structuredClone(authForm.value)
  if (auth.value.selectedAction === auth.value.signup) {
    payload.date_of_birth = payload.date_of_birth.replace(/\//g, '-')
    store.dispatch('auth/register', payload).then(() => {
      auth.value.selectedAction = auth.value.login
      successNotif('Successfully registered')
    }).catch(() => errorNotif('Something went wrong'))
    return
  }
  delete payload.date_of_birth
  delete payload.user_name
  delete payload.password2
  store.dispatch('auth/login', payload).then(res => {
    successNotif(res.message)
    $router.push(ROUTE_CONSTS.HOME.PATH)
  }).catch(() => errorNotif('Something went wrong'))
}
</script>

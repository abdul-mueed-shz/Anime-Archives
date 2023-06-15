import { boot } from 'quasar/wrappers'
import axios from 'axios'

// Be careful when using SSR for cross-request state pollution
// due to creating a Singleton instance here;
// If any client changes this (global) instance, it might be a
// good idea to move this instance creation inside of the
// "export default () => {}" function below (which runs individually
// for each client)
const appVer = 'api/v1/'

const archivesBaseUrl = (process.env.DEV ? 'http://127.0.0.1:8002/' : '') + appVer // TODO: ADD PRODUCTION LINK WHEN BACKEND IS HOSTED

const jikanApi = axios.create({ baseURL: 'https://api.jikan.moe/v4/' })

const archivesApi = axios.create({ baseURL: archivesBaseUrl })

export default boot(({ app, store }) => {
  // for use inside Vue files (Options API) through this.$axios and this.$api
  archivesApi.interceptors.request.use((config) => {
    const accessToken = store.getters['auth/getAuthDetails'].tokens?.access
    if (accessToken) {
      config.headers.Authorization = `Bearer ${accessToken}`
    }
    return config
  }, (error) => {
    throw new Error(error)
  })

  app.config.globalProperties.$axios = axios
  // ^ ^ ^ this will allow you to use this.$axios (for Vue Options API form)
  //       so you won't necessarily have to import axios in each vue file

  app.config.globalProperties.$jikanApi = jikanApi
  app.config.globalProperties.$archivesApi = archivesApi
  // ^ ^ ^ this will allow you to use this.$api (for Vue Options API form)
  //       so you can easily perform requests against your app's API
})

export { jikanApi, archivesApi }

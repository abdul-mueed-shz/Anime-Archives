import { archivesApi } from 'src/boot/axios'

export const setAuthDetails = ({ commit }, data) => { commit('setAuthDetails', data) }

export const setAuthProperty = ({ commit }, data) => { commit('setAuthProperty', data) }

export const register = async ({ commit }, payload) => {
  try {
    const response = await archivesApi.post('/user/register/', payload)
    return response.data.body
  } catch (err) {
    throw new Error(err.response.data.body.detail)
  }
}
export const login = async ({ commit }, payload) => {
  try {
    const response = await archivesApi.post('/user/login/', payload)
    commit('setAuthDetails', response.data.body)
    return response.data.body
  } catch (err) {
    throw new Error(err.response.data.body.detail)
  }
}
export const logout = async ({ commit }, payload) => {
  try {
    const response = await archivesApi.post('/user/logout/')
    commit('clearAuthDetails')
    return response.data.body
  } catch (err) {
    throw new Error(err.response.data.body.detail)
  }
}
export const getUserWatchlists = async ({ commit }) => {
  try {
    const response = await archivesApi.get('watchlist/get-playlists/')
    return response.data.body
  } catch (err) {
    throw new Error(err.response.data.body.detail)
  }
}

export const setAuthDetails = (state, details) => {
  state.authDetails.tokens.access = details.access
  state.authDetails.tokens.refresh = details.refresh
  state.authDetails.userProfile = details.user
}

export const setAuthProperty = (state, data) => { state.authDetails[data.key] = data.value }
export const clearAuthDetails = (state) => {
  state.authDetails = {
    userProfile: {},
    tokens: {
      access: null,
      refresh: null
    }
  }
}

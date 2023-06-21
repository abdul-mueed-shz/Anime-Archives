export const getAuthDetails = (state) => state.authDetails

export const isLoggedIn = (state) => !!state.authDetails.tokens.access

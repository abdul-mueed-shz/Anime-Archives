export const ROUTE_CONSTS = Object.freeze({
  HOME: { NAME: '', PATH: '/', COMPONENT_PATH: 'src/pages/HomePage.vue' },
  LOGIN: { NAME: 'auth', PATH: '/auth', COMPONENT_PATH: 'src/pages/AuthPage.vue' },
  DETAILS: { NAME: 'details', PATH: '/details/', COMPONENT_PATH: 'src/pages/CardPage.vue' },
  ERROR: { NAME: 'error', PATH: '/:catchAll(.*)*', COMPONENT_PATH: 'pages/ErrorNotFound.vue' }
})

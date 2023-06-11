import { ROUTE_CONSTS } from 'src/common/constants/routes'

const routes = [
  {
    path: ROUTE_CONSTS.HOME.PATH,
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('src/pages/HomePage.vue') }
    ]
  },
  {
    path: ROUTE_CONSTS.LOGIN.PATH,
    component: () => import('layouts/BlankLayout.vue'),
    children: [
      { path: '', component: () => import('src/pages/LoginPage.vue') }
    ]
  },
  {
    path: ROUTE_CONSTS.DETAILS.PATH + ':id',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('src/pages/CardPage.vue') }
    ]
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: ROUTE_CONSTS.ERROR.PATH,
    component: () => import('pages/ErrorNotFound.vue')
  }
]

export default routes

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, RightViewSet, RoleViewSet, UserRoleViewSet
from rest_framework_simplejwt import views as jwt_views

router = DefaultRouter()
router.register(r'user', UserViewSet, basename='user')
router.register(r'right', RightViewSet, basename='right')
router.register(r'role', RoleViewSet, basename='role')
router.register(r'user-role', UserRoleViewSet, basename='user-role')

urlpatterns = [
    path('', include(router.urls), ),
    path('user/token-refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]

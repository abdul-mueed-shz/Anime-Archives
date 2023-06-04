from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet
from rest_framework_simplejwt import views as jwt_views

router = DefaultRouter()
router.register(r'user', UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls), ),
    path('user/token-refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]

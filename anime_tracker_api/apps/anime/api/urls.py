from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.anime.api.views import AnimeViewSet

router = DefaultRouter()
router.register(r'anime', AnimeViewSet, basename='anime')

urlpatterns = [
    path('', include(router.urls))
]

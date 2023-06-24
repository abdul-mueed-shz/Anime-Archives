from rest_framework.routers import DefaultRouter
from django.urls import path, include

from .views import WatchListViewSet, WatchlistAnimeViewSet

router = DefaultRouter()
router.register(r'watchlist', WatchListViewSet, basename='watchlist')
router.register(r'watchlist-anime', WatchlistAnimeViewSet, basename='watchlist-anime')
urlpatterns = [
    path('', include(router.urls), ),
]

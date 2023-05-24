from rest_framework.routers import DefaultRouter
from django.urls import path, include

from .views import WatchListViewSet

router = DefaultRouter()
router.register(r'watchlist', WatchListViewSet, basename='watchlist')
urlpatterns = [
    path('', include(router.urls), ),
]

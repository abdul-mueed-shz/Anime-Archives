from django.contrib import admin
from django.urls import path, include

API_PREFIX = 'api/v1/'

urlpatterns = [
    path('admin/', admin.site.urls),
    path(API_PREFIX, include('apps.watchlist.api.urls')),
]

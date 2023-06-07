from django.contrib import admin
from django.urls import path, include

API_PREFIX = 'api/v1/'

urlpatterns = [
    path(API_PREFIX + 'chat/', include('apps.common.api.urls')),
    path(API_PREFIX + 'admin/', admin.site.urls),
    path(API_PREFIX, include('apps.watchlist.api.urls')),
    path(API_PREFIX, include('apps.user.api.urls')),
    path(API_PREFIX, include('apps.posts.api.urls')),
]

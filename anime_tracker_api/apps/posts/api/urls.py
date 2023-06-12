from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.posts.views import PostViewset, index

router = DefaultRouter()
router.register("post", PostViewset, basename="post")

urlpatterns = [
    path('', include(router.urls)),
    path('posts-view', view=index)
]

from django.urls import path

from apps.common.api.views import JoinRoom

urlpatterns = [
    path('join-room/', JoinRoom.as_view()),
]

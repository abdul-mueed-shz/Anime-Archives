from django.urls import re_path

from .consumers import ChatConsumer, PostConsumer

websocket_urlpatterns = [
    # path('ws/<str:room_name>/', ChatConsumer.as_asgi()),
    re_path(r'^ws/$', PostConsumer.as_asgi())
]

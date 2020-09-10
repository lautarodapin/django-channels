from django.urls import re_path, path

from . import consumers
from channels.layers import get_channel_layer
websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatConsumer),
    path('ws/usuarios/', consumers.UserConsumer)
]
channel_layer = get_channel_layer()
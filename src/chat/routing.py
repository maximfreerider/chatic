from .consumers import ChatConsumer, AsyncChatConsumer
from django.urls import re_path

websocket_urls = [
    re_path(r'^ws/chat/$', ChatConsumer),
    re_path(r'^ws/async_chat/<murr_chat_name>/$', AsyncChatConsumer),
]

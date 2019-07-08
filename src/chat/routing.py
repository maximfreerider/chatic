from .consumers import ChatComsumer
from django.urls import path, re_path

websocket_urls = [
    re_path(r'^ws/chat/$', ChatComsumer),
]

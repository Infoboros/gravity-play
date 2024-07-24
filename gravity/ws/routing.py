from channels.routing import URLRouter
from django.urls import re_path
from ws.consumers.client import AsyncChatConsumer
websockets = URLRouter([
    re_path(r'ws/client/$', AsyncChatConsumer.as_asgi()),
])

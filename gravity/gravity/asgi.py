import os

from channels.routing import ProtocolTypeRouter
from django.core.asgi import get_asgi_application

from ws.routing import websockets

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gravity.settings')
application = ProtocolTypeRouter({
   "http": get_asgi_application(),
   "websocket": websockets,
})

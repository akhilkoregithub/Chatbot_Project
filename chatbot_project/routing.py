from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from chatbot_app import consumers

application = ProtocolTypeRouter({
    'websocket': URLRouter([
        path('ws/caht/<int:conversation_id>/',
             consumers.ChatConsumer.as_asgi()),
    ]),
})

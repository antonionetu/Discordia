from django.urls import path

from config.consumers import ChatConsumer

ws_urlpatterns = [
    path('ws/chat/<str:room_name>/', ChatConsumer.as_asgi())
]

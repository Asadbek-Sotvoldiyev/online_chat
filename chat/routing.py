from django.urls import re_path
from .consumers import ChatComsumer, ProfileListConsumer

websocket_urlpatterns = [
    re_path(r"ws/chat/(?P<name>\w+)/$", ChatComsumer.as_asgi()),
    re_path(r"ws/users/$", ProfileListConsumer.as_asgi()),
]
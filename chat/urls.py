from django.urls import path
from .views import index, chat_user

urlpatterns = [
    path('', index, name="home"),
    path('user/<str:username>/', chat_user, name="chat_user"),
]
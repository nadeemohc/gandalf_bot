from django.urls import path
from .views import index, chat_with_gandalf, reset_chat

urlpatterns = [
    path('', index, name='index'),
    path('chat/', chat_with_gandalf, name='chat_with_gandalf'),
    path('reset/', reset_chat, name='reset_chat'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('chat/<int:conversation_id>', views.chat_view, name='chat'),
]

# chat/urls.py
from django.urls import path
from .signals import *
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('user/usuarios/', views.UserView.as_view(), name='user-list'),
    path('<str:room_name>/', views.room, name='room'),

]

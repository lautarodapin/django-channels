# chat/views.py
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.models import User
def index(request):
    return render(request, 'chat/index.html')

def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name': room_name
    })


class UserView(TemplateView):
    template_name = "chat/user_notifier.html"
    
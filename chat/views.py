from django.shortcuts import render
from .models import Room, Message


def room(request, room_name):
    _room, _ = Room.objects.get_or_create(name=room_name)
    messages = Message.objects.filter(room=_room)

    return render(request, 'index.html', {
        'room_name': room_name,
        'messages': messages
    })

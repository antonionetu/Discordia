from threading import Thread

from chat.models import *


class CreateMessageThread(Thread):
    def __init__(self, room_name, author, content):
        self.room_name = room_name
        self.author = author
        self.content = content
        Thread.__init__(self)

    def run(self):
        message = Message.objects.create(
            room=Room.objects.get(name=self.room_name),
            author=self.author,
            content=self.content
        )
        message.save()

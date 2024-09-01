import json

from channels.generic.websocket import AsyncWebsocketConsumer

from chat.Threads.create_message import CreateMessageThread


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f"chat_{self.room_name}"

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()


    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )


    async def receive(self, text_data):
        message = json.loads(text_data)
        content = message['message']
        author = message['author']
        chat_name = message['chat_name']

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': content,
                'author': author
            }
        )

        CreateMessageThread(
            room_name=chat_name,
            author=author,
            content=content
        ).start()


    async def chat_message(self, event):
        content = event['message']
        author = event['author']

        await self.send(text_data=json.dumps({
            'message': content,
            'author': author
        }))

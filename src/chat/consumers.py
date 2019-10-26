from channels.generic.websocket import (WebsocketConsumer, AsyncJsonWebsocketConsumer)
from asgiref.sync import async_to_sync
import json


class AsyncChatConsumer(AsyncJsonWebsocketConsumer):

    async def connect(self):
        self.murr_chat_name = self.scope['url_route']['kwargs']['murr_chat']
        await async_to_sync(self.channel_layer.group_add)(self.murr_chat_name, self.channel_name)
        await self.accept()

    def disconnect(self, code):
        pass
        pass

    async def receive_json(self, content, **kwargs):
        # content["!"] = 1
        await self.send_json(content=content)

    @classmethod
    async def encode_json(cls, content):
        return await super().encode_json(content)

    @classmethod
    async def decode_json(cls, text_data):
        return await super().decode_json(text_data)


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        print("It`s connected!")

    def receive(self, text_data=None, bytes_data=None):
        if text_data:
            print("u have new message")
        else:
            print("nothing")
        json_data = json.loads(text_data)
        # message = json_data['data']
        self.send(text_data=json.dumps({
            'data': "hello from backend!!!"
        }))

    def disconnect(self, code):
        pass
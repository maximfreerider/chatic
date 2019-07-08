from channels.generic.websocket import AsyncWebsocketConsumer
import json

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.accept("subprotocol")

    async reciever(self, text_data = None, bytes_data = None):
        await self.send(text_data="Hello from channels")
        await self.send(bytes_data="Hello from Channels")

    async def disconnect(self):
        await self.close()


        

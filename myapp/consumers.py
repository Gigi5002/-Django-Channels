from channels.generic.websocket import AsyncWebsocketConsumer
import json
import asyncio
from random import randint

class WSConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

        for i in range(1000):
            await self.send(json.dumps({'message': randint(1, 100)}))
            await asyncio.sleep(1)

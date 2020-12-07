import asyncio
import websockets
import requests

ws_url = "ws://localhost:8000/socket/"


class Network():
    def __init__(self):
        self.websocket = websockets.connect(ws_url)

    def send(self, data):
        # await self.websocket.send(data)
        requests.put(url='localhost:8080')

    def recv(self):
        return None

    async def command_receiver(self, alarm):
        while True:
            msg = await self.websocket.recv()
            if 'arm' in msg:
                alarm.armed = msg['arm']
            if 'alarm' in msg:
                if not msg['alarm']:
                    alarm.alarm = False
            await self.websocket.send({'done': True})


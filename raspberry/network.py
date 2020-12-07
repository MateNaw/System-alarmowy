import asyncio
import websockets

ws_url = "ws://localhost:8000/measurement/"


class Network:
    ws_url = "ws://localhost:8000/measurement/"
    def __init__(self):
        # async with websockets.connect(self.ws_url) as websocket:
        print('networkin module')
        websocket = websockets.connect(self.ws_url)
        print(websocket)
        self.websocket = websocket

    async def send(self, data):
        await self.websocket.send(data)

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

ws_url = "ws://localhost:8000/measurement/"


class Network:
    ws_url = "ws://localhost:8000/measurement/"
    def __init__(self):
        # async with websockets.connect(self.ws_url) as websocket:
        print('networkin module')
        websocket = websockets.connect(self.ws_url)
        print(websocket)
        self.websocket = websocket

    async def send(self, data):
        await self.websocket.send(data)

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

||||||| merged common ancestors
=======
import asyncio
import websockets

ws_url = "ws://localhost:8000/measurement/"

class Network():
    def __init__(self):
        async with websockets.connect(ws_url) as websocket:
            self.websocket = websocket

    def send(self, data):
        await self.websocket.send(data)

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
>>>>>>> main

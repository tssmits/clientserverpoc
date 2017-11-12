#!/usr/bin/env python

import asyncio
import websockets

async def hello(websocket, path):
    while True:
        name = "Multatuli"
        greeting = "Hello {}!".format(name)
        await websocket.send(greeting)
        # print("> {}".format(greeting))
        await asyncio.sleep(1)

start_server = websockets.serve(hello, 'localhost', 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

#!/usr/bin/env python3

import serial
import asyncio
import websockets
import time
from threading import Thread
import os
import sys
import random

CLIENTS = set()

def initEmitMessage():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(emitMessage())
    loop.close()

async def emitMessage():
    try:
        while True:
            print("Socketen lever")
            await broadcast("Socketen lever")
            time.sleep(1)
    except:
        print("dude..")

async def broadcast(message):
    for websocket in CLIENTS.copy():
        try:
            await websocket.send(message)
        except websockets.ConnectionClosed:
            pass

async def handleRestart(websocket):
    while True:
        message = await websocket.recv()
        print(f"Received: {message}")
        os.execv(sys.executable, ['python3'] + [sys.argv[0]])

async def handler(websocket, path):
    CLIENTS.add(websocket)
    print("connection established")

    emitBPMThread = Thread(target=initEmitMessage)
    emitBPMThread.start()

    await handleRestart(websocket)

    try:
        async for _ in websocket:
            pass
    except websockets.ConnectionClosed:
        pass  # Handle the client disconnect gracefully
    finally:
        print("Connection closed")
        CLIENTS.remove(websocket)

async def main():
    print("Starting server")
    async with websockets.serve(handler, "localhost", 1337):
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())

print("Server finished")
GPIO.cleanup() # Clean up

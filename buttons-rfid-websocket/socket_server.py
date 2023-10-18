#!/usr/bin/env python

import asyncio
import websockets
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

ids = {
    "584189222903" : "kort 1", #Sindre
    "37481287347" : "m2",
    "584188004692" : "m3",
    }

b1_pin = 8
b2_pin = 10
b3_pin = 12
bounce_time = 1000





reader = SimpleMFRC522()

async def read_rfid(callback):
    while True:
        id, text = reader.read_no_block()
        if id:
            await callback(id)
            print(id)
            #print(text)
            await asyncio.sleep(3)
        await asyncio.sleep(0.25)

CLIENTS = set()

def button1_callback(channel):
    print("Button 1 was pushed", channel)
    asyncio.run(broadcast("b1"))

def button2_callback(channel):
    print("Button 2 was pushed", channel)
    asyncio.run(broadcast("b2"))

def button3_callback(channel):
    print("Button 3 was pushed", channel)
    asyncio.run(broadcast("b3"))

async def rfid_callback(id):
    print(f"Received ID: {id}")
    res=f"{id}"
    if str(id) in ids:
        res=ids[str(id)]
    print(res)
    #await broadcast(f"{res}")
    await broadcast("b3")


print("Starting RFID reader")
asyncio.get_event_loop().create_task(read_rfid(rfid_callback))
#asyncio.run(read_rfid(rfid_callback))

async def send_message(message):
    for connection in websocket_connections:
        await connection.send(message)

async def broadcast(message):
    for websocket in CLIENTS.copy():
        try:
            await websocket.send(message)
        except websockets.ConnectionClosed:
            pass

print("Setting up IO pins")
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(b1_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(b1_pin,GPIO.RISING,callback=button1_callback, bouncetime = bounce_time) 

GPIO.setup(b2_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) 
GPIO.add_event_detect(b2_pin,GPIO.RISING,callback=button2_callback, bouncetime = bounce_time)

GPIO.setup(b3_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) 
GPIO.add_event_detect(b3_pin,GPIO.RISING,callback=button3_callback, bouncetime = bounce_time)

# create handler for each connection
async def handler(websocket, path):
    print("connection established")
    data = await websocket.recv()
    print(f"Received: {data}")
    reply = f"Data recieved as:  {data}!"
    
    await websocket.send(reply)
    CLIENTS.add(websocket)
    try:
        await websocket.wait_closed()
    finally:
        CLIENTS.remove(websocket)
    

print("Starting server")
start_server = websockets.serve(handler, "localhost", 8000)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

print("Server finished")
GPIO.cleanup() # Clean up


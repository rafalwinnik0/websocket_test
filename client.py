import asyncio
import websockets

async def hello():
    url = "ws://localhost:8765"
    async with websockets.connect(url) as websocket:
        name = input("What's your name?")
        await websocket.send(name)
        print(f">>> {name}")

        greeting = await websocket.recv()
        print(f"<<< {greeting}")

asyncio.run(hello())

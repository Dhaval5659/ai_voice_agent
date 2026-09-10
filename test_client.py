import asyncio
import websockets

async def test():
    uri = "ws://127.0.0.1:8000/ws/voice"
    async with websockets.connect(uri) as websocket:
        for i, audio_file in enumerate(["intro_for_hospital.m4a", "followup.m4a"]):
            with open(audio_file, "rb") as f:
                await websocket.send(f.read())
            print(f"Sent message {i+1}, waiting for reply...")

            reply_audio = await websocket.recv()
            with open(f"server_reply_{i+1}.mp3", "wb") as f:
                f.write(reply_audio)
            print(f"Received reply {i+1}")

asyncio.run(test())
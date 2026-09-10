from fastapi import FastAPI, WebSocket
from fastapi.staticfiles import StaticFiles
from bot import run_bot

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.websocket("/ws/voice")
async def voice_endpoint(websocket: WebSocket):
    await websocket.accept()
    await run_bot(websocket)
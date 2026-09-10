import { PipecatClient } from "@pipecat-ai/client-js";
import { WebSocketTransport, ProtobufFrameSerializer } from "@pipecat-ai/websocket-transport";

const statusEl = document.getElementById("status");
const connectBtn = document.getElementById("connectBtn");
const disconnectBtn = document.getElementById("disconnectBtn");

const pcClient = new PipecatClient({
  transport: new WebSocketTransport({
    serializer: new ProtobufFrameSerializer(),
    recorderSampleRate: 16000,
    playerSampleRate: 24000,
  }),
  enableMic: true,
  callbacks: {
    onConnected: () => {
      statusEl.innerText = "Connected — speak now";
      connectBtn.disabled = true;
      disconnectBtn.disabled = false;
    },
    onDisconnected: () => {
      statusEl.innerText = "Disconnected";
      connectBtn.disabled = false;
      disconnectBtn.disabled = true;
    },
    onBotReady: () => {
      statusEl.innerText = "Bot ready — speak now";
    },
    onError: (err) => {
      console.error("Pipecat error:", err);
      statusEl.innerText = `Error: ${err.message || err}`;
    },
  },
});

connectBtn.onclick = async () => {
  statusEl.innerText = "Connecting...";
  try {
    await pcClient.connect({ wsUrl: "ws://localhost:8000/ws/voice" });
  } catch (err) {
    console.error("Connection failed:", err);
    statusEl.innerText = "Connection failed";
  }
};

disconnectBtn.onclick = async () => {
  await pcClient.disconnect();
};
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

SYSTEM_PROMPT = (
    "You are a helpful voice assistant for a hospital. "
    "Answer briefly and naturally, like a real phone conversation. "
    "Keep responses under 2-3 sentences since this will be spoken aloud."
)

def get_llm_reply(user_text: str) -> str:
    chat = client.chats.create(
        model="gemini-flash-latest",
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_PROMPT,
        ),
    )
    response = chat.send_message(user_text)
    return response.text

if __name__ == "__main__":
    reply = get_llm_reply("What are your hospital timings and which cities are you in?")
    print("LLM reply:", reply)


import os
import sys
from deepgram import DeepgramClient
from dotenv import load_dotenv

load_dotenv()

# Initialize client with your API key
deepgram = DeepgramClient()

def transcribe_file(audio_path: str) -> str:
    with open(audio_path, "rb") as audio_file:
        buffer_data = audio_file.read()

    response = deepgram.listen.v1.media.transcribe_file(
        request=buffer_data,
        model="nova-3",
        smart_format=True,
        language="en",
    )

    transcript = response.results.channels[0].alternatives[0].transcript
    return transcript

if __name__ == "__main__":
    text = transcribe_file("intro_for_hospital.m4a")
    print("Transcript:", text)
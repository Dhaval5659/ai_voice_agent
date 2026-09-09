from dotenv import load_dotenv
from deepgram import DeepgramClient

load_dotenv()

deepgram = DeepgramClient()

def text_to_speech(text: str, output_path: str = "reply_audio.mp3") -> str:
    response = deepgram.speak.v1.audio.generate(
        text=text,
        model="aura-2-thalia-en",  # a natural-sounding English voice
    )

    with open(output_path, "wb") as audio_file:
        for chunk in response:
            audio_file.write(chunk)

    return output_path

if __name__ == "__main__":
    path = text_to_speech("Hello! Our hospital is open from 9 AM to 8 PM, and we have branches in Ahmedabad and Surat.")
    print("Saved audio to:", path)

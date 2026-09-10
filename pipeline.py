from dotenv import load_dotenv
from transcribe import transcribe_file
from llm_reply import get_llm_reply
from tts_reply import text_to_speech

load_dotenv()

def run_pipeline(audio_input_path: str):
    user_text = transcribe_file(audio_input_path)
    print("User said:", user_text)

    reply_text = get_llm_reply(user_text)
    print("Bot reply:", reply_text)

    output_path = text_to_speech(reply_text)
    print("Bot audio saved to:", output_path)

if __name__ == "__main__":
    run_pipeline("intro_for_hospital.m4a")

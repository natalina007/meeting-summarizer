import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

client = Groq(api_key=api_key)

AUDIO_FILE_PATH = "MeetingSummarizerAudio1.m4a"

# 1. Transcribe audio with Whisper
print("1. Transcribing audio...")
with open(AUDIO_FILE_PATH, "rb") as file:
    transcription = client.audio.transcriptions.create(
        file=(file.name, file.read()),
        model="whisper-large-v3",
    )

transcript = transcription.text
print("\n--- TRANSCRIPT ---")
print(transcript)

# 2. Summarize transcript with LLM
print("\n2. Generating summary and action items...")
prompt = f"""
Analyze the following meeting transcript. Provide:
1. Executive Summary
2. Key Decisions Made
3. Action Items (formatted as: - [ ] **Owner**: Task - Deadline)

Transcript:
{transcript}
"""

response = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[{"role": "user", "content": prompt}],
)

print("\n--- SUMMARY & ACTION ITEMS ---")
print(response.choices[0].message.content)
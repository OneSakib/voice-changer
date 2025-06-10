import whisper
from googletrans import Translator
from gtts import gTTS
import os
import tempfile

# Input video file
VIDEO_INPUT = "hindi_video.mp4"
ENGLISH_AUDIO_OUTPUT = "english_audio.mp3"
FINAL_VIDEO_OUTPUT = "translated_video.mp4"

# Step 1: Transcribe Hindi audio from video
print("🔤 Transcribing audio...")
model = whisper.load_model("medium")
result = model.transcribe(VIDEO_INPUT, language="hi")
hindi_text = result["text"]
print(">>>>>>>>>>>>HIDNI", hindi_text)

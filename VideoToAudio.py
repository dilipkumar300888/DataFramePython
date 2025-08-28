import whisper
from moviepy.editor import VideoFileClip

video_path = "D:\\PythonProjects\\Dataframe\\WhatsApp Video 2025-08-26 at 02.33.00_926b6f45.mp4"

video_clip = VideoFileClip(video_path)
audio_path = "temp_audio.wav"
video_clip.audio.write_audiofile(audio_path)

# Step 2: Load Whisper model (use 'base', 'small', 'medium', 'large')
model = whisper.load_model("small")  # 'small' is faster, 'large' is more accurate

# Step 3: Transcribe audio to text
print("Transcribing... please wait.")
result = model.transcribe(audio_path, fp16=False)

# Step 4: Save transcript
with open("webex_transcript.txt", "w", encoding="utf-8") as f:
    f.write(result["text"])

print("✅ Transcription completed! Saved to webex_transcript.txt")
print("\n Adding a new Line")
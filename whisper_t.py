import openai
from tkinter import filedialog
from config import API_KEY

openai.api_key = API_KEY


# Transcribe the audio
def transcribe_audio(file_path):
    with open(file_path, "rb") as audio_file:
        transcript = openai.Audio.transcribe("whisper-1", audio_file)
    return transcript["text"]


filepath = filedialog.askopenfilename(initialdir="~", title="Select file", filetypes=(("wav files", "*.wav"),
                                                                                      ("all files", "*.*")))
transcription = transcribe_audio(filepath)
print(transcription)

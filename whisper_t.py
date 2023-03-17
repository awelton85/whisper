import openai
from tkinter import filedialog
from config import API_KEY


openai.api_key = API_KEY
filepath = filedialog.askopenfilename(initialdir="/home/", title="Select file", filetypes=(("wav files", "*.wav"),
                                                                                           ("all files", "*.*")))


# Transcribe the audio
def transcribe_audio(file_path):
    with open(file_path, "rb") as audio_file:
        transcript = openai.Audio.transcribe("whisper-1", audio_file)
    return transcript["text"]


transcription = transcribe_audio(filepath)
print(transcription)

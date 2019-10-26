
import speech_recognition as sr
from os import path
from pydub import AudioSegment

# # files                                                                         
# src = "transcript.mp3"
# # dst = "test.wav"

# # convert wav to mp3                                                            
# sound = AudioSegment.from_mp3('../audio_messages/1.mp3')
# sound.export('../audio_messages/1.wav', format="wav")


AUDIO_FILE = '../audio_messages/3.flac'

r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
    
    audio = r.record(source)  # read

try:
    message = r.recognize_google(audio, language='ru-RU')
except:
    print('Something went wrong!')

print('You said: '+message)


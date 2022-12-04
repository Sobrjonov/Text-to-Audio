# pip install playsound
from playsound import playsound
# pip install gtts
from gtts import gTTS

audio_file = "speech.mp3"
text_to_convert = "Hello Abdulloh!"
language = "en"
speech = gTTS(text=text_to_convert, lang=language, slow=False)

speech.save(audio_file)
playsound(audio_file)

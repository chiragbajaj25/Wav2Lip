import os
from gtts import gTTS
from pydub import AudioSegment

audio_name = "seargent"
# Replace with your text
mytext = "Drill Seargeant: Gump! What’s your sole purpose in this army? \
          Gump: To do whatever you tell me Drill Seargeant. \
          Drill Seargeant: Goddamnit Gump, you’re a goddamn genius. That’s the most outstanding answer I’ve ever heard. You must have a goddamn IQ of 160. You are goddamn gifted Private Gump."
language = 'en'

def txt_audio(text=mytext, audio_name=audio_name):
    myobj = gTTS(text=text, lang=language,tld='co.in', slow=False)

    audio_path = f"/content/gdrive/MyDrive/NFT_Art/Audio/{audio_name}.mp3"
    wav_audio_path = f"/content/gdrive/MyDrive/NFT_Art/Audio/{audio_name}.wav"
    myobj.save(audio_path)
    sound = AudioSegment.from_mp3(audio_path)
    sound.export(wav_audio_path, format="wav")
    return wav_audio_path
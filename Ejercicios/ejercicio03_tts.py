from gtts import gTTS
import os

mytext = "Hola, vengo del espacio exterior a invadir el planeta"
audio = gTTS(text=mytext, lang="es", slow=False)
audio.save("example.mp3")

os.system("start example.mp3")
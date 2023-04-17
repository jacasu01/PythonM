from gtts import gTTS
import os

nombre = input("Introduce tu nombre:")
edad = input("Introduce tu edad:")

texto = f"Te llamas {nombre} y tienes {edad} años"
audio = gTTS(text=texto, lang="es", slow=False)
audio.save("saludo.mp3")

os.system("start saludo.mp3")
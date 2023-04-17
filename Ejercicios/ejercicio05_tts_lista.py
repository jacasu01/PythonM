from gtts import gTTS
import os
import time

lista = ["Lunes","Martes","Miércoles","Jueves","Viernes"]

for item in lista:
    audio = gTTS(text=item, lang="es", slow=False)
    audio.save("item.mp3")
    os.system("start item.mp3")
    time.sleep(3)

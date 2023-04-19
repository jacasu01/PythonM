from gtts import gTTS
import os

def leer_receta(nombre_receta):
    nombre_fichero = "./recetas/" + nombre_receta + ".txt"
    fichero = open(nombre_fichero, encoding="utf-8", mode="r")
    info = fichero.read()
    fichero.close()
    return info

def hacer_locucion(texto):
    audio = gTTS(text=texto, lang="es", slow=False)
    audio.save("locucion.mp3")
    os.system("start locucion.mp3")

receta = (input("¿Qué desea usted?")).upper()
match receta:
    case 'PAELLA':
        hacer_locucion(leer_receta('paella'))
    case 'ESTOFADO':
        hacer_locucion(leer_receta('estofado'))
    case 'DESCANSO':
        hacer_locucion(leer_receta('descanso'))
    case _:
        hacer_locucion("No tengo esa receta")


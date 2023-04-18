def censor(palabra):
    palabras_prohibidas = ("mameluco","monopatín","hereje")
    if palabra in palabras_prohibidas:
        return "***"
    return palabra

texto = "El hereje agarró el monopatín y se lo prestó al mameluco"
lista_palabras = texto.split()

palabras_finales = [censor(palabra) for palabra in lista_palabras]
#Reconstruimos el str a partir de los elementos de la lista
palabras_finales=" ".join(palabras_finales)
print(palabras_finales)
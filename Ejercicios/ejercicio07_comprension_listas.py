lista = ["arbol.jpg","seta.png","arbusto.gif"]
"""
#Construcción de una nueva lista con los nombres de fichero sin extensión
lista_nueva = []
for planta in lista:
    nombre = planta[0:-4]
    lista_nueva.append(nombre)
"""
lista_nueva = [planta[0:-4] for planta in lista]
print(lista_nueva)

lista_mayusculas = [planta.upper() for planta in lista]
print(lista_mayusculas)

#De los elementos de lista sustituir las letras a por el símbolo @ 
lista_arrobas = [planta.replace("a","@") for planta in lista]
print(lista_arrobas)

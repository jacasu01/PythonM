lista = [0,1,2,3,4,5,6,7,8,9]
sublista = lista[0:4]#4 elementos a partir del primero 0,1,2,3
sublista = lista[2:4]#2 elementos a partir del tercero 2,3
sublista = lista[0:10:1]# Toda la lista
sublista = lista[0:10:2]# [0, 2, 4, 6, 8]
sublista = lista[::]#Desde el primero hasta el último, de uno en uno
sublista = lista[5:]#Desde el 5 hasta el final
sublista = lista[:4]#[0, 1, 2, 3]
sublista = lista[:-1]#Todos menos el último
sublista = lista[1:-1]#Todos menos el primero y el último
sublista = lista[::-1]
print(sublista)
lista = ["arbol.jpg","seta.png","arbusto.gif"]
#lista_nueva = []#Nueva lista - opción 1
lista_nueva = list()#Nueva lista - opción 2
for planta in lista:
    nombre = planta[0:-4]
    lista_nueva.append(nombre)
print(lista_nueva)
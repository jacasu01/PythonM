capitales = ['A Coruña', 'Lugo', 'Ourense', 'Pontevedra', 'Santiago']
poblaciones = [246056, 97903, 104488, 82853]
informacion = zip(capitales, poblaciones)
#Recorremos el zip con un for (si lo recorremos, se consume el zip y 'desaparece')
#for capital, poblacion in informacion:
#    print(capital, poblacion)
#Transformamos el zip a una lista
lista_ciudades = list(informacion)
print(lista_ciudades)

capitales = ['A Coruña', 'Lugo', 'Ourense', 'Pontevedra', 'Santiago']
poblaciones = [246056, 97903, 104488, 82853]
informacion = zip(capitales, poblaciones, strict=True)#Provocará un error si las listas tienen tamaños distintos
lista_ciudades = list(informacion)
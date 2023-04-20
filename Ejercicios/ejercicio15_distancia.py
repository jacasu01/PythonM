import Levenshtein

dias = ["Luns","Martes","Mercores","Xoves","Venres","Sábado","Domingo"]

dia = input("Introduce un día de la semana:")
dia = dia.capitalize()
if dia in dias:
    print("OK",dia)
else:
    # Quiero obtener esto: [(3,"Luns"),(4,"Martes"),(4,"Mercores")]
    #Versión for
    '''
    distancias = []
    for d in dias:
        distancia = Levenshtein.distance(dia, d)
        distancias.append( (distancia, d) )
    '''
    #Versión comprensión de listas
    distancias = [(Levenshtein.distance(dia, d), d) for d in dias]
    print("A lo mejor querías decir",min(distancias)[1])



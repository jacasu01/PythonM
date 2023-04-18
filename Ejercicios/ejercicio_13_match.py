def leer_receta(nombre_receta):
    nombre_fichero = "./recetas/" + nombre_receta + ".txt"
    fichero = open(nombre_fichero, encoding="utf-8", mode="r")
    info = fichero.read()
    fichero.close()
    return info


receta = (input("¿Qué desea usted?")).upper()
match receta:
    case 'PAELLA':
        print(leer_receta('paella'))
    case 'ESTOFADO':
        print(leer_receta('estofado'))
    case _:
        print("No tengo esa receta")

#En la versión 2.0. utilizaremos funciones.
#En la versión 3.0. el programa habla.
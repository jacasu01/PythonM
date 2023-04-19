import Levenshtein

dias = ["Luns","Martes","Mercores","Xoves","Venres","Sábado","Domingo"]

dia = input("Introduce un día de la semana:")

#Si el día introducido es correcto --> OK
#Si el día introducido no es correcto --> Mostrar el que más se parezca

#AYUDA: Operador in
#AYUDA: Método capitalize de la clase str
"""
palabra1 = "gato"
palabra2 = "gata"
palabra3 = "ratón"

print(Levenshtein.distance(palabra1, palabra2))
print(Levenshtein.distance(palabra1, palabra3))
"""
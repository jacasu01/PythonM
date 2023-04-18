lista = [8,4,3,10,15,25]
#Bucle normal
for elemento in lista:
    print(elemento)

#Bucle con break y else
for elemento in lista:
    print(elemento)
    if elemento==15:
        break #Detiene la ejecución del bucle
else:#Sólo si se recorre la lista entera. Si salimos con break NO
    print("Else")

#Bucle con slicing
for elemento in lista[1::2]:
    print(elemento,end=":")
print()

#Bucle for con range
for i in range(100):
    print(i,end="-")
print()

#Bucle for con range 100 y 0 decreciente
for i in range(100,-1,-1):
    print(i,end="-")
print()
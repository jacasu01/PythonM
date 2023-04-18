ingresos = 25_000
if ingresos<10_000:
    print("Menos de 10.000")
    print("Necesitas mejorar")
elif ingresos<20_000:
    print("Menos de 20.000")
    print("No está mal")
else:
    print("Tienes 20.000 de ingresos o más")

#Operador ternario
edad = 18
#Modo 'normal'
if edad>=18:
    autorizado = True
else:
    autorizado = False
#Modo 'ternaria'
autorizado = True if edad>=18 else False



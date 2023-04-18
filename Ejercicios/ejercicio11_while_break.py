import random
numero_secreto = int(random.random()*10)
encontrado=False
intentos = 0
while encontrado==False:
    numero_candidato = int(input("Introduce un número[0-10):"))
    if numero_candidato==numero_secreto:
        encontrado=True
    else:
        print("El número introducido no es el número secreto")
        intentos+=1
        if intentos==3:
            print("Eres un fraude")
            break #Detiene la ejecución del bucle
else:#Se ejecuta cuando se deja de cumplir la condición del While (pero no cuando hacemos break)
    print("Has acertado, eres un gran adivino")
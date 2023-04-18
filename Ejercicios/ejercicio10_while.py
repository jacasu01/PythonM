import random
numero_secreto = int(random.random()*10)
encontrado=False
while encontrado==False:
    numero_candidato = int(input("Introduce un número[0-10):"))
    if numero_candidato==numero_secreto:
        print("Eres un gran adivino")
        encontrado=True
    else:
        print("Eres un fraude de adivino")
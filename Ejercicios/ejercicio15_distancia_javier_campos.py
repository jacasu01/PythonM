import Levenshtein
from modulo_dias_semana import DIAS

dia = input("Introduce el día de la semana:")
if dia in DIAS:
    print("OK",dia)
else:
    midia = "No sé"
    for item in DIAS:
        if Levenshtein.distance(item.lower(),dia.lower())<2:
            midia = item

    if (midia!="No sé"):
        print(f"Quieres decir {midia}")
    else:
        print(midia)
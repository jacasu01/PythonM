def dividir(d1, d2):
    lista = [0,1,2]
    lista[1] #IndexError si el índice no existe
    diccionario = {0:"Cero",1:"Uno"}
    diccionario[0]#KeyError si la clave no existe
    return d1/d2 #ZeroDivisionError si d2==0

try:
    resultado = dividir(5,0)
    print(resultado)
except:
    print("Error")


try:
    resultado = dividir(5,2)
    print(resultado)
except ZeroDivisionError:
    print("Error: división entre 0")
except IndexError:
    print("Error: índice inexistente")
except:
    print("Error. No sé que pasa, pero pasa algo")


try:
    resultado = dividir(5,0)
    print(resultado)
except ZeroDivisionError as pelota:
    print(pelota)
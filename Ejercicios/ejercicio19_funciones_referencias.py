#x se pasa como parámetro por valor
def funcion1(x:int):
    x+=1

valor = 5
funcion1(valor)
print(valor)

#x se pasa como parámetro por referencia
def funcion2(x:list):
    x.append(8)

lista = []
funcion2(lista)
print(lista)

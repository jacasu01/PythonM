print("ASIGNACIÓN POR VALOR")
x=10
y=x
print(x, y)
x=12
print(x, y)

print("ASIGNACIÓN POR REFERENCIA")
lx = [3,5]
ly = lx
print(lx, ly)
lx.append(8)
print(lx, ly)

print("COPIA DE LISTA")
lx = [3,5]
ly = lx.copy()
print(lx, ly)
lx.append(8)
print(lx, ly)

print("GENERACIÓN DE COPIA DE LISTA con SLICING")
lx = [3,5]
ly = lx[:]
print(lx,ly)
lx.append(8)
print(lx, ly)

print("GENERACIÓN DE COPIA DE LISTA con list")
lx = [3,5]
ly = list(lx)
print(lx,ly)
lx.append(8)
print(lx, ly)
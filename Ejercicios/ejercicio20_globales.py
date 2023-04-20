def funcion1():
    global x #Toma la x del ámbito global
    x=10

x=5
funcion1()
print(x)
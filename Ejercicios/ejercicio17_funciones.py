#Función que no tienes parámetros, no tiene retorno y escribe "Ola"
def saludar():
    print("Ola")

saludar()

#Función que recibe como parámetro un nombre, no tiene retorno y escribe "Ola valor_parametro"
def saludar_con_nombre(nombre : str):
    print("Ola",nombre)

saludar_con_nombre("Javier")

#Función que recibe un nombre y devuelve el texto "Hola valor_del_nombre"
def get_saludo(nombre : str) -> str:
    return f"Ola {nombre}"

print(get_saludo("Domingo"))

#Función que suma dos números y los muestra por pantalla
def sumar(sumando1, sumando2):
    print(sumando1 + sumando2)

sumar(3,4)

#Función que devuelva la suma de dos números. El segundo número es opcional 
# y tendrá un valor por defecto de 0.
def get_suma(sumando1,sumando2=0):
    return sumando1+sumando2

print(get_suma(5,3))
print(get_suma(5))

#Función con un parámetro obligatorio y tres parámetros opcionales
def funcion_opcional(par1, par2=0, par3=0, par4=0):
    print(par1, par2, par3, par4)

funcion_opcional(3)
funcion_opcional(5,1)
funcion_opcional(5,5,5,5)
funcion_opcional(3,par3=8)

#Función que recibe un número indeterminado de parámetros
def funcion_indeterminada(*args):#args es una tupla
    print(type(args))
    for arg in args:
        print(arg,end="-")
    print()


funcion_indeterminada(3)
funcion_indeterminada(3,8)
funcion_indeterminada(3,8,"Hola","Ordenador")
funcion_indeterminada(3,8,True,15.3,"Ola",3,8,10,8)

#Función que recibe un número indeterminado de pares de clave-valor
def funcion_diccionario(**kvargs):
    for k,v in kvargs.items():
        print(k,v)

funcion_diccionario(nombre="David",altura=180,activo=True)




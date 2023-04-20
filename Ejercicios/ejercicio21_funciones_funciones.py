import time

def tarea1():
    print("Realizando tarea 1...")
    time.sleep(1)

def tarea2():
    print("Realizando tarea 2...")
    time.sleep(1)

def tarea3():
    print("Realizando tarea 3...")
    time.sleep(1)

def ejecutador_tareas(funcion):
    funcion()

lista_tareas = []
lista_tareas.append(tarea1)
lista_tareas.append(tarea2)
lista_tareas.append(tarea1)
lista_tareas.append(tarea3)
lista_tareas.append(tarea2)
for tarea in lista_tareas:
    tarea()
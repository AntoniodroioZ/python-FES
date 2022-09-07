import random
from pynput import keyboard as kb
import keyboard
import time
import os

global bandera
bandera = True
global valor
valor = 0
global interrupciones
interrupciones = 0
global tiempo
tiempo = time.time()

def ciclo(bandera1, contador):
    global valor
    global bandera
    global interrupciones
    global tiempo
    valor = contador
    
    tiempoInicio = time.time()
    int(tiempoInicio)

    while bandera1:
        tiempoActual = time.time()
        int(tiempoActual)
        valor+=1
        # os.system("cls")
        print(f"Contador:  {valor}, estado de la bandera: {bandera}, numero de interrupciones: {interrupciones}, si deseas parar oprime S, tiempo actual: {int(tiempoActual)}")
        if valor == random.randint(valor,10000000000000000000000):
            bandera = False
            interrupciones +=1
            print(f"Contador:  {valor}, estado de la bandera: {bandera}, numero de interrupciones: {interrupciones}, tipo de interrupcion: Software")
            break
        if keyboard.is_pressed("s"):
            bandera = False
            interrupciones +=1
            print(f"Contador:  {valor}, estado de la bandera: {bandera}, numero de interrupciones: {interrupciones}, tipo de interrupcion: Hardware")
            break
            
        if  int(tiempoActual) == (int(tiempoInicio) + 10):
            bandera = False
            interrupciones +=1
            print(f"Contador:  {valor}, estado de la bandera: {bandera}, numero de interrupciones: {interrupciones}, tipo de interrupcion: Software (limite de tiempo)")
            break
            
print(f"Contador:  {valor}, estado de la bandera: {bandera}, numero de interrupciones: {interrupciones}")
print('Oprime la tecla "i" para iniciar la ejecución')
while True:
    if keyboard.read_key() == "i":
        print(f"Contador:  {valor}, estado de la bandera: {bandera}, numero de interrupciones: {interrupciones}")
        ciclo(bandera, valor)
    elif keyboard.read_key() != "i":
        print("Tecla invalida")
    if bandera == False:
        print("La ejecución se ha detenido, deseas continuar con la ejecución (Oprime R), deseas reiniciar (Oprime T) o deseas cancelar (Oprime E)")
        if keyboard.is_pressed("R"):
            bandera = True
            ciclo(bandera, valor)
        if keyboard.is_pressed("E"):
            bandera = False
            print(f"Contador:  {valor}, estado de la bandera: {bandera}, numero de interrupciones: {interrupciones}, tipo de interrupcion: Hardware (el usuario ha finalizado)")
            break
        if keyboard.is_pressed("T"):
            bandera = True
            valor = 0
            interrupciones = 0
            ciclo(bandera, valor)
            

import os

op = "1"

calfCalc = 0
datos = []
numDatos = 0
while(op!="2"):
    print("\n1)Agregar dato \n2)Salir \n")
    op= input("Elige una opcion: ")
    if op == '1':
        nombre = input("ingresa el nombre del alumno: ")
        calf = input("Ingresa la calificacion del alumno: ")
        calfCalc = calfCalc + int(calf)
        registro = nombre+","+calf+"\n"
        datos.append(registro)  
        numDatos = len(datos) 
        calfCalc = calfCalc / numDatos
        print("El promedio del grupo es de: ", calfCalc)
    elif op == '2':
        print("Has escogido salir del programa")
    else:
        print("Opcion no valida XD")

print(datos)

archivo = open("datos.csv","a")
archivo.writelines(datos)
contenido = archivo.readlines(datos)
print(contenido)
archivo.close()
import os
  
op = '1'

datos = []

print("Ingrese su usuario y una contraseña de 8 o mas digitos")
while(op!="2"):
    op= input("Elige una opcion: \n 1)Ingresar datos \n 2)Salir del programa\n")
    if op == '1':        
        usuario = input("Ingresa tu usuario: \n")
        contrasenia = input("ingresa tu contraseña: \n")
        tamCon = len(contrasenia)
        if tamCon >= 8:
            print("Contraseña valida")
            registro = usuario+","+contrasenia+"\n"
            datos.append(registro)  
        elif tamCon != 8:
            print("Contraseña invalida")
        else:
            print("Opcion no valida")

    elif op == '2':
        print("Has escogido salir del programa")
    else:
        print("Opcion no valida XD")


archivo= open("registros.csv","a")
#archivo.write() #Una sola cosa o linea
archivo.writelines(datos) #Escribe en mi archivo más de una linea
archivo.close()

a=open("registros.csv","r")
contenido=a.readlines()
a.close()

print(contenido)

# a = open("usuariosYContraseña.csv","r")
# a.writelines(datos)
# contenido=a.readlines()
# tamcontenido = len(contenido)
# for i in range(0,tamcontenido,1):
#     print(contenido[i])
# a.close()

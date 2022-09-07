nombre = input("Ingresa tu nombre de usuario\n")

if(len(nombre)<5 or len(nombre)>15):
    print("El nombre: ", nombre," no es un nombre de usuario valido, intente de nuevo.1")
else:
    if((nombre.isalnum())==True):
        print("Nombre de usuario: ", nombre.upper())
        nombre.isalnum()
    else:
        print("El nombre: ", nombre," no es un nombre de usuario valido, intente de nuevo.2")

# cadena = input("Ingresa una cadena:\n")

# if(len(cadena)>2):
#     print(cadena[0],cadena[1],cadena[2],cadena[-1])
#     print("cadena valida")
# else:
#     print("Cadena no valida, es menor de 3 caracteres.")

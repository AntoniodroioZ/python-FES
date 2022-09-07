#Menu de calculadora

import os #Librería os

op="1"  #Defino a mi variable opción y la mantengo en 1 (cadena)

while(op!="6"):

    os.system("cls") 
    
    """Limpiar mi terminal"""

    print("\n \t \t Bienvenidos a mi calculadora \n" )
    print("\n1)Suma \n 2)Resta \n 3)Multiplicación \n 4)División \n 5)Conversión \n 6)Salir \n")

    op= input("Elige una opción: ")

    if op=="1":
        print("Elegiste suma")
        input("Presiona enter para continuar...")
        dig1=float(input("Ingresa el primer sumando: "))
        dig2=float(input("\n Ingresa el segundo sumando: "))
        suma= dig1+dig2
        print("La suma de ",dig1, "+",dig2, "es: ", suma)
    elif op=="2":
        print("Elegiste resta")
        input("Presiona enter para continuar...")
    elif op=="3":
        print("Elegiste multiplicación")
        input("Presiona enter para continuar...")
    elif op=="4":
        print("Elegiste división")
        input("Presiona enter para continuar...")
    elif op=="5":
        print("Elegiste conversión ")
        input("Presiona enter para continuar...")
        op2="0"
        while op2!="3":
            os.system("cls")
            print("\n \t \t \t Sistema de conversiones \n")
            print("1)Binario a decimal \n 2)Octal a decimal \n 3)Salir")
            op2=input("Elige una opción: ")
            if op2=="1":
                print("Elegiste conversión binario a decimal")
                input("Presiona enter para continuar...")
            elif op2=="2":
                print("Elegiste conversión octal a decimal")
                input("Presiona enter para continuar...")
            elif op2=="3":
                print("Elegiste regresar al menú principal")
                input("Presiona enter para continuar...")
            else:
                print("Opción no válida")
                input("Presiona enter para continuar...")
    elif op=="6":
        print("Elegiste salir")
        input("Presiona enter para continuar...")
    else: 
        print("Opción no valida")
        input("Presiona enter para continuar...")
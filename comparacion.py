print("\t\t\t Programa que te comprara dos numeros enteros")

a= int(input("Dime el primer numero a comparar: \n"))
b = int(input("Dime el segundo numero a comparar: \n"))

def comparacion(a,b):
    if a>b:
        return 1;
    elif a<b:
        return -1
    else:
        return 0

print(comparacion(a,b))

#PRograma que determina si un valor entero es negativo

a = int(input("Ingresa un valor: "))

if a > 0: 
    print(a, "es un numero positivo")
elif a == 0:
    print(a, "es un elemento neutro")
else:
    print(a, "es un numero negativo")
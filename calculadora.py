# Hacer un programa que dados 2 numeros calcule la suma, la resta, 
# la multiplicacion, la division, el modulo y la potencia.

num1 = int(input("Escribe un numero que quieras calcular: "))
num2 = int(input("Escribe otro numero que quieras calcular: "))
# a = int(input("Ingresa el numero que deseas sacar su factorial: \n"))
dig1=int(input("Ingresa el valor a sacar factorial: "))

suma = num1 + num2
print("La suma de los dos numeros es: ", suma)
resta = num1 - num2
print("La resta de los dos numeros es: ", resta)
mul = num1 * num2
print("La multiplicacion de los dos numeros es: ", mul)
if num2 == 0:
    print("La division no puede ser realizada")
    print("La operacion modulo no puede ser realizada")
else:
    div = num1 / num2
    print("La division de los dos numeros es: ", div)
    mod = num1 % num2 
    print("El modulo de los dos numeros es: ", mod)

potencia = num1 ** num2
print("La potencia de los dos numeros es: ", potencia)


def factorial(n):
    if n == 0 or n == 1:
        resultado = 1
    elif n > 0:
        resultado = n*factorial(n-1)
    return resultado
    
print("El factorial de ", dig1, "es ", factorial(dig1))



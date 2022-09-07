#Programa que suma los primeros cien numeros

# n= int(input("Dime el numero hasta el que deseas sumar: \n"))

# suma = n* (n + 1) / 2

# print("La suma de los numeros hasta el ", n "es: ", suma)

# m= int(input("Dime en el numero que deseas empezar a sumar: \n"))
# n= int(input("Dime el numero hasta el que deseas sumar: \n"))

# a = 0

# for i in range(m,n,1):
#     a = a + i

# print("La suma de los numeros desde: ", m, "hasta: ", n, "es: ", a)

# Suma de Gauss usando While
a=0
i=1
while(i<101):
    a = a + i
    i = i + 1

print(a)
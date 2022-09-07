a = int(input("Ingresa el numero que deseas sacar su factorial: \n"))
factorial = a
for i in range(1,a,1):
    factorial = factorial * i

print("Numero factorial con for: ", factorial)
    
factorial = a    
z = 1

while z <= a-1:
    factorial = factorial * z
    z = z + 1

print("Numero factorial con while: ", factorial)


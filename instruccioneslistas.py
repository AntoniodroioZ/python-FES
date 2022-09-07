#Intrucciones con listas

a = [1,3,-3,2]

print(a)
# for i in a:
#     print(i)


a.append(10) #agrega un dato al final de la lista
print(a)
a.insert(0,10) #inserta un dato en lugar indicado
print(a)
# print(max(a))
# print(min(a))
a.remove(10)
print(a)
# a.sort() Orden la lista en ella misma
# print(a)

b=sorted(a) #Ordena la lista en una nueva variable
print(b)

print("El numero de datos de mi lista a es: ", len(a)) #Cuenta la cantidad de datos dentro del arreglo.

print("El lugar que ocupa -3 en la lista es :", (a.index(-3)+1))
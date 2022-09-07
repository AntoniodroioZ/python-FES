import math

# print(math.pi)
# print(math.sin(math.pi/4))
# print(math.cos(math.pi/2))
# print(math.sqrt(4))
# print(math.e)
# print(math.exp(-2))

print("\t\t\t Programa que calcula el area de in circulo")
radio = float(input("¿Cual es el radio de tu circulo? \n"))

def areaCirculo(radio):
    return (radio**2)*math.pi

print("El area del circulo de radio: ", radio, "es ", areaCirculo(radio))
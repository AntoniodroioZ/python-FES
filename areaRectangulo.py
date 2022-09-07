#Calcular el area de un rectangulo

print("\t\t\t Este programa determina el area de un rectangulo \n")
base = float(input("¿Cual es la base? \n"))
altura = float(input("¿Cual es la altura \n"))

def areaReactangulo(area, altura):
    return base*altura

print("El area de un rectangulo de base ", base,"y altura ", altura, "es: ", areaReactangulo(base, altura) )
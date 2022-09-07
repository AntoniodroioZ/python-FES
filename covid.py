archivo = open("bd.csv","r")
contenido = archivo.readlines()

tamContenido = len(contenido)
individuosCOVID = 0
edadIndividuosCOVID = 0

for i in range(0,tamContenido,1):
    dato = contenido[i] 
    posComa = dato.find(",")
    edad = float(dato[:posComa])
    indicador = float(dato[posComa + 1:])
    if indicador >= 0.8:
        individuosCOVID = individuosCOVID + 1
        edadIndividuosCOVID = edadIndividuosCOVID + edad    

if individuosCOVID == 0:
    print("El semaforo se encuentra en verde: ", individuosCOVID," individios con COVID")
elif individuosCOVID >= 1: 
    print("El semaforo se encuentra en amarillo: ", individuosCOVID, " individuos con COVID")
    edadIndividuosCOVID = edadIndividuosCOVID / individuosCOVID
    print("La edad promedio de los individuos con COVID es: ", edadIndividuosCOVID)
elif individuosCOVID <= 30: 
    print("El semaforo se encuentra en amarillo: ", individuosCOVID, " individuos con COVID")
    edadIndividuosCOVID = edadIndividuosCOVID / individuosCOVID
    print("La edad promedio de los individuos con COVID es: ", edadIndividuosCOVID)
elif individuosCOVID >= 31:
    print("El semaforo se encuentra en naranja: ", individuosCOVID, " individuos con COVID")
    edadIndividuosCOVID = edadIndividuosCOVID / individuosCOVID
    print("La edad promedio de los individuos con COVID es: ", edadIndividuosCOVID)
elif individuosCOVID <= 70:
    print("El semaforo se encuentra en naranja: ", individuosCOVID, " individuos con COVID")
    edadIndividuosCOVID = edadIndividuosCOVID / individuosCOVID
    print("La edad promedio de los individuos con COVID es: ", edadIndividuosCOVID)
elif individuosCOVID >= 71:
    print("El semaforo se encuentra en rojo: ", individuosCOVID, " individuos con COVID")
    edadIndividuosCOVID = edadIndividuosCOVID / individuosCOVID
    print("La edad promedio de los individuos con COVID es: ", edadIndividuosCOVID)

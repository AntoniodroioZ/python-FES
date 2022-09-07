numBin = input("Ingresa un numero binario de 4 digitos: \n")

binario1 = numBin[3]
binario2 = numBin[2]
binario3 = numBin[1]
binario4 = numBin[0]

numDec = 0 

if binario1 == '0':
    numDec = numDec + 0
elif binario1 == '1':
    numDec = numDec + 1

if binario2 == '0':
    numDec = numDec + 0
elif binario2 == '1':
    numDec = numDec + 2

if binario3 == '0':
    numDec = numDec + 0
elif binario3 == '1':
    numDec = numDec + 4

if binario4 == '0':
    numDec = numDec + 0
elif binario4 == '1':
    numDec = numDec + 8

print(numDec)
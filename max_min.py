import random
from time import time

print("Ingrese cuantos numeros aleatorios desea obtener")
n = int(input())

maxVal = 0
minVal = 1000
lista = []

tiempoI = time()
for i in range(n):
    lista.append(random.randint(0, 1000))
    if maxVal < lista[i]:
        maxVal = lista[i]
for i in range(n):
    if minVal > lista[i]:
        minVal = lista[i]




print(maxVal)
print(minVal)

tiempo = time()
tiempoT = tiempo - tiempoI
print(tiempoT)
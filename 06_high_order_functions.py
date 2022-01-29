def saludo(fn):
    fn()

def hola():
    print('Hola!')

def adios():
    print('Adios!')

saludo(hola)
saludo(adios)

###########################################
# FILTER
###########################################

mi_lista = [1, 4, 5, 6, 9, 13, 19, 21]

impares = [i for i in mi_lista if i%2 != 0]
print(impares)

impares = list( filter(lambda x : x%2 != 0, mi_lista) )
print(impares) 

###########################################
# MAP
###########################################

mi_lista = [1, 2, 3, 4, 5]
cuadrados = [i**2 for i in mi_lista]
print(cuadrados)

cuadrados = list( map(lambda x: x**2, mi_lista) )
print(cuadrados)

###########################################
# REDUCE
###########################################

mi_lista = [2, 2, 2, 2, 2]
multiplicador = 1
for i in mi_lista:
    multiplicador *= i

print(multiplicador)

from functools import reduce

mi_lista = [2, 2, 2, 2, 2]
multiplicador = reduce( lambda a, b : a*b, mi_lista )
print(multiplicador)
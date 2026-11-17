from functools import reduce

numeros = [1,2,3,4,5,6,7,8,8,10]

# Función map
cuadrados_iterador = map(lambda x: x**2, numeros)
cuadrados = list(cuadrados_iterador)

print(f"Listado de números: {numeros}")
print(f"Cuadrado de los números usando map: {cuadrados}")

# Función filter
pares_iterador = filter(lambda x: x%2 == 0, numeros)
pares = list(pares_iterador)
print(f"Filtrando solo pares usando filter: {pares}")

# Función reduce
suma_total = reduce(lambda a,b: a+b, cuadrados)
print(f"Suma total de números elevados al cuadrado usando reduce: {suma_total}")
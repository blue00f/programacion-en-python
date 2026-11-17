# Comprensión de listas
numeros = [1,2,3,4,5,6,7,8,9,10]
cuadrados = [n**2 for n in numeros]
print(f"Lista original: {numeros}")
print(f"Cuadrados: {cuadrados}")

# Usando una condición
pares = [n for n in numeros if n%2==0]
print(f"\nNúmeros pares: {pares}")

# Filtrando y usando una condición (como si fueran map y filter al mismo tiempo)
cuadrados_de_pares = [n**2 for n in numeros if n%2==0]
print(f"Cuadrados de los pares: {cuadrados_de_pares}")

# Ejemplo con strings
nombres = ["ana", "juan", "pedro", "pablo", "jorge"]
nombres_mayus = [nombre.upper() for nombre in nombres]
print(f"Nombres en mayúsculas: {nombres_mayus}")
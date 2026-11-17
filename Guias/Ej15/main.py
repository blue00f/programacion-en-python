# Expresiones generadoras
gen_cuadrados = (x**2 for x in range(1,6))
print(f"Objeto generador: {gen_cuadrados}") # a diferencia de comprensión de listas, devuelve un objeto generador

# Mostrando los valores bajo demanda
print(f"Primer valor: {next(gen_cuadrados)}")
print(f"Segundo valor: {next(gen_cuadrados)}")

# Mostrando los valores con for
print("Valores restantes en el objeto generador:")
for n in gen_cuadrados:
  print(n)

# tiraría una excepción porque las expresiones generadoras solo se recorren una vez, a diferencia de la compresión de listas
#print(f"Otro valor {next(gen_cuadrados)}")

print(f"\n=== Más ejemplos de expresiones generadoras ===")
sum_cuadrados = sum(x**2 for x in range(1,11))
print(f"La suma de los cuadrados es: {sum_cuadrados}")

numeros = [3,7,12,5,9]
hay_mayores_a_10 = any(x>10 for x in numeros)
print(f"\nNúmeros: {numeros}")
print(f"¿Hay algún número mayor a 10? {hay_mayores_a_10}")

# Expresión generadora propia
def contar_hasta(limite):
  i = 1
  while i <= limite:
    yield i
    i += 1

print("\n=== Creando un generador ===")
mi_generador = contar_hasta(3)
print(f"Tipo de objeto: {type(mi_generador)}")

print(f"primer valor: {next(mi_generador)}")
for n in mi_generador:
  print(f"valor: {n}")
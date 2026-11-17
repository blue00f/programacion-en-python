def cuadrado(x):
  return x**2
def cubo(x):
  return x**3

# Funcion de orden superior que debe recibir una función como parámetro
def procesar_numeros(numeros, funcion):
  resultados = []
  for n in numeros:
    resultados.append(funcion(n))
  return resultados

numeros = [1,2,3,4,5,6,7,8,9,10]
res_cuadrados = procesar_numeros(numeros, cuadrado)
res_cubos = procesar_numeros(numeros, cubo)
res_multiplicados = procesar_numeros(numeros, lambda x: x*10)
print (f"Números: {numeros}")
print(f"Cuadrados: {res_cuadrados}")
print(f"Cubos: {res_cubos}")
print(f"Multiplicados por 10: {res_multiplicados}")
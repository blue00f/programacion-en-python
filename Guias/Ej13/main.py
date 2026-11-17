# Lambda asignada a una variable
sumar = lambda a, b: a + b
res = sumar(5,3)
print(f"Suma usando lambda: {res}")

# Lambda usada para ordenamiento
estudiantes = [
  {"nombre": "Ana", "edad": 22},
  {"nombre": "Raúl", "edad": 25},
  {"nombre": "Sofia", "edad": 18},
  {"nombre": "Guillermo", "edad": 65},
]

# El parámetro key recibe una función que indica qué valor usar para ordenar
estudiantes_por_edad = sorted(estudiantes, key=lambda x: x["edad"])
print("\nEstudiantes ordenados por edad")
for est in estudiantes_por_edad:
  print(f"\t{est["nombre"]} {est["edad"]} años")

# Lambda con un filtro condicional
es_par = lambda x: x%2 == 0
print(f"\n¿El número 4 es par? {es_par(4)}")
print(f"¿El número 7 es par? {es_par(7)}")
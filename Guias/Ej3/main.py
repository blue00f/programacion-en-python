estudiantes = [
    {"nombre": "Ana", "nota": 9.5},
    {"nombre": "Raul", "nota": 3},
    {"nombre": "Carlos", "nota": 6},
    {"nombre": "Lorena", "nota": 8}
]

i = 0
while i < len(estudiantes):
  estudiante = estudiantes[i]
  print(f"Evaluando a {estudiante["nombre"]}...")
  i += 1

print("--- RESULTADOS ---")
for estudiante in estudiantes:
  nombre = estudiante["nombre"]
  nota = estudiante["nota"]
  if nota >= 9.0:
    estado = "Excelente"
  elif nota >= 6.0:
    estado = "Bien"
  else:
    estado = "Desaprobado"
  print(f"\t{nombre}: Nota {nota} -> Estado: {estado}")
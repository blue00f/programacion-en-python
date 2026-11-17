# Uso de cadenas
curso = "Programación en Python"
nombre_limpio = curso.strip().upper()

print(f"Curso: {nombre_limpio}")

# Uso de listas
estudiantes = ["Ana", "Carlos", "Rodolfo", "Pedro"]
estudiantes.append("Lucia")
print(estudiantes)

print(f"El primer estudiante de la lista es: {estudiantes[0]}")

# Uso de diccionarios
detalles_curso = {
  "titulo": nombre_limpio,
  "duracion_semanas": 16,
  "alumnos_inscriptos": estudiantes,
  "disponible": True
}

print("=== Datos del diccionario ===")
print(f"Titulo del curso: {detalles_curso["titulo"]}")
print(f"Duración: {detalles_curso["duracion_semanas"]} semanas")
print(f"Total de alumnos: {detalles_curso["alumnos_inscriptos"]}")

for alumno in detalles_curso["alumnos_inscriptos"]:
  print(f"- {alumno}")
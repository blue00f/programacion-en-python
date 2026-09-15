from modelo import Persona, Empleado, Estudiante, Ayudante

est = Estudiante("Carlos", 101)
print(f"Estudiante: {est.nombre} | Legajo: {est.legajo}")

ayu = Ayudante("Ana", 102, 4000, "Matemática Discreta y Autómatas")
print(f"Ayudante: {ayu.nombre} | Legajo: {ayu.legajo} | Sueldo: ${ayu.sueldo} | Materia: {ayu.materia}")

print("\n--- DEMOSTRACIÓN USANDO issubclass() ---")
print(f"¿Estudiante es una subclase de Persona? {issubclass(Estudiante, Persona)}")
print(f"¿Ayudante es una subclase de Empleado? {issubclass(Ayudante, Empleado)}")
print(f"¿Ayudante es una subclase de Estudiante? {issubclass(Ayudante, Estudiante)}")
print(f"¿Ayudante es una subclase de Persona? {issubclass(Ayudante, Persona)}")
print(f"¿Estudiante es una subclase de Empleado? {issubclass(Estudiante, Empleado)}")

print("\n--- DEMOSTRACIÓN USANDO isinstance() ---")
print(f"¿{est.nombre} es una instancia de Persona? {isinstance(est, Persona)}")
print(f"¿{est.nombre} es una instancia de Estudiante? {isinstance(est, Estudiante)}")
print(f"¿{est.nombre} es una instancia de Ayudante? {isinstance(est, Ayudante)}")
print(f"¿{est.nombre} es una instancia de Empleado? {isinstance(est, Empleado)}")

print(f"\n¿{ayu.nombre} es una instancia de Persona? {isinstance(ayu, Persona)}")
print(f"¿{ayu.nombre} es una instancia de Estudiante? {isinstance(ayu, Estudiante)}")
print(f"¿{ayu.nombre} es una instancia de Ayudante? {isinstance(ayu, Ayudante)}")
print(f"¿{ayu.nombre} es una instancia de Empleado? {isinstance(ayu, Empleado)}")

print("\n--- DEMOSTRACIÓN USANDO MRO ---")
print(f"MRO de {est.nombre}")
for clase in Estudiante.mro():
  print(f" -> {clase.__name__}")

print(f"MRO de {ayu.nombre}")
for clase in Ayudante.mro():
  print(f" -> {clase.__name__}")
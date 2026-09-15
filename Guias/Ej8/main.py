from modelo import Empleado, EmpleadoPorHora, EmpleadoTiempoCompleto

empleados: list[Empleado] = [EmpleadoTiempoCompleto("Ana", 450000), EmpleadoPorHora("Carlos", 80, 2500)]

for e in empleados:
  print(f"Empleado: {e.nombre} | Salario: ${e.calcular_salario()}")

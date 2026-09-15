class Persona:
  def __init__(self, nombre: str):
    self.nombre = nombre
  @property
  def nombre(self) -> str:
    return self._nombre
  @nombre.setter
  def nombre(self, valor: str) -> None:
    self._nombre = valor

class Empleado:
  def __init__(self, sueldo: float):
    self.sueldo = sueldo
  @property
  def sueldo(self) -> float:
    return self._sueldo
  @sueldo.setter
  def sueldo(self, valor: float):
    self._sueldo = valor

class Estudiante(Persona):
  def __init__(self, nombre: str, legajo: int):
    super().__init__(nombre)
    self.legajo = legajo
  @property
  def legajo(self) -> int:
    return self._legajo
  @legajo.setter
  def legajo(self, valor: int) -> None:
    self._legajo = valor

class Ayudante(Estudiante, Empleado):
  def __init__(self, nombre: str, legajo: int, sueldo: float, materia: str):
    Estudiante.__init__(self, nombre, legajo)
    Empleado.__init__(self, sueldo)
    self.materia = materia
  @property
  def materia(self) -> str:
    return self._materia
  @materia.setter
  def materia(self, valor: str) -> None:
    self._materia = valor

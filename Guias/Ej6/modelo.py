class Alumno:
  def __init__(self, nombre: str, apellido: str):
    self.nombre = nombre
    self.apellido = apellido

  @property
  def nombre(self) -> str:
    return self._nombre
  @nombre.setter
  def nombre(self, valor: str) -> None:
    self._nombre = valor
  @property
  def apellido(self) -> str:
    return self._apellido
  @apellido.setter
  def apellido(self, valor: str) -> None:
    self._apellido = valor

  def __str__(self) -> str:
    return f"{self.nombre} {self.apellido}"
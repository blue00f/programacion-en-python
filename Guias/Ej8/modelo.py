from abc import ABC, abstractmethod

class Empleado(ABC):
  def __init__(self, nombre: str):
    self.nombre = nombre
  @property
  def nombre(self) -> str:
    return self._nombre
  @nombre.setter
  def nombre(self, valor: str) -> None:
    self._nombre = valor
  @abstractmethod
  def calcular_salario(self) -> float:
    pass

class EmpleadoTiempoCompleto(Empleado):
  def __init__(self, nombre: str, salario_mensual: float):
    super().__init__(nombre)
    self.salario_mensual = salario_mensual
  @property
  def salario_mensual(self) -> float:
    return self._salario_mensual
  @salario_mensual.setter
  def salario_mensual(self, valor: float) -> None:
    self._salario_mensual = valor
  def calcular_salario(self) -> float:
    return self.salario_mensual

class EmpleadoPorHora(Empleado):
  def __init__(self, nombre: str, horas_trabajadas: float, tarifa_hora: float):
    super().__init__(nombre)
    self.horas_trabajadas = horas_trabajadas
    self.tarifa_hora = tarifa_hora
  @property
  def horas_trabajadas(self) -> float:
    return self._horas_trabajadas
  @horas_trabajadas.setter
  def horas_trabajadas(self, valor: float) -> None:
    self._horas_trabajadas = valor
  @property
  def tarifa_hora(self) -> float:
    return self._tarifa_hora
  @tarifa_hora.setter
  def tarifa_hora(self, valor: float) -> None:
    self._tarifa_hora = valor

  def calcular_salario(self) -> float:
    return self.horas_trabajadas * self.tarifa_hora
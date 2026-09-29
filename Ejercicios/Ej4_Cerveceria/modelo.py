from enum import Enum

class TipoVaso(Enum):
  CHOPP = ("Chopp (3/4 L)", 0.75, False)
  VASO = ("Vaso (1/2 L)", 0.50, False)
  JARRA = ("Jarra (3 L)", 3.00, True)
  def __init__(self, descripcion: str, litros: float, tiene_incremento: bool):
    self.descripcion = descripcion
    self.litros = litros
    self.tiene_incremento = tiene_incremento

class Cerveza:
  def __init__(self, nombre: str, origen: str, precio_por_litro: float):
    self.nombre = nombre
    self.origen = origen
    self.precio_por_litro = precio_por_litro

  @property
  def nombre(self) -> str:
    return self._nombre
  @nombre.setter
  def nombre(self, valor: str) -> None:
    self._nombre = valor
  @property
  def origen(self) -> str:
    return self._origen
  @origen.setter
  def origen(self, valor: str) -> None:
    self._origen = valor

  @property
  def precio_por_litro(self) -> float:
    return self._precio_por_litro
  @precio_por_litro.setter
  def precio_por_litro(self, valor: float) -> None:
    self._precio_por_litro = valor

  def __str__(self) -> str:
    return f"{self.nombre} {self.origen} - ${self.precio_por_litro} Precio por L"

class Barril:
  _contador_id: int = 1
  def __init__(self, cerveza: Cerveza) -> None:
    self._id: int = Barril._contador_id
    Barril._contador_id += 1
    self.cerveza = cerveza
    self._litros_servidos: float = 0.0
    self._recaudacion_total: float = 0.0
  @property
  def id(self) -> int:
      return self._id
  
  @property
  def cerveza(self) -> Cerveza:
    return self._cerveza
  @cerveza.setter
  def cerveza(self, valor: Cerveza) -> None:
    if not isinstance(valor, Cerveza):
        raise TypeError("El barril debe contener un objeto de tipo Cerveza.")
    self._cerveza = valor

  @property
  def litros_servidos(self) -> float:
    return self._litros_servidos
  @property
  def recaudacion_total(self) -> float:
    return self._recaudacion_total
  
  def registrar_servicio(self, litros: float, monto: float) -> None:
    if litros <= 0 or monto <= 0:
      raise ValueError("Los litros y montos servidos deben ser positivos.")
    self._litros_servidos += litros
    self._recaudacion_total += monto

  def __str__(self) -> str:
    return (f"Barril #{self.id} [{self.cerveza.nombre}] - Litros: {self.litros_servidos:.2f}L | Recaudación: ${self.recaudacion_total:.2f}")


class Venta:
  PORCENTAJE_INCREMENTO: float = 0.05
  def __init__(self, barril: Barril, tipo_vaso: TipoVaso):
    self.barril = barril
    self.tipo_vaso = tipo_vaso
    self._litros_vendidos: float = self.tipo_vaso.litros
    self._monto_total: float = self._calcular_monto()
    self.barril.registrar_servicio(self._litros_vendidos, self._monto_total)
  @property
  def barril(self) -> Barril:
    return self._barril

  @barril.setter
  def barril(self, valor: Barril) -> None:
    if not isinstance(valor, Barril):
      raise TypeError("La venta debe estar asociada a un Barril válido.")
    self._barril = valor

  @property
  def tipo_vaso(self) -> TipoVaso:
    return self._tipo_vaso

  @tipo_vaso.setter
  def tipo_vaso(self, valor: TipoVaso) -> None:
    if not isinstance(valor, TipoVaso):
      raise TypeError("El tipo de vaso debe ser una opción válida de TipoVaso.")
    self._tipo_vaso = valor

  @property
  def litros_vendidos(self) -> float:
    return self._litros_vendidos

  @property
  def monto_total(self) -> float:
    return self._monto_total
  def _calcular_monto(self) -> float:
    precio_base_litro = self.barril.cerveza.precio_por_litro
    costo_base = self.tipo_vaso.litros * precio_base_litro
    if self.tipo_vaso.tiene_incremento:
        costo_base += costo_base * Venta.PORCENTAJE_INCREMENTO
    return costo_base

  def __str__(self) -> str:
    return f"Venta: {self.tipo_vaso.descripcion} de {self.barril.cerveza.nombre} (Barril {self.barril.id}) -> Total: ${self.monto_total}"
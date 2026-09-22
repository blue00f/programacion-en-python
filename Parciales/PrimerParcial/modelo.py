class Personaje:
  def __init__(self, vida: int, posicion: int, velocidad: float):
    self.vida = vida
    self.posicion = posicion
    self.velocidad = velocidad
  @property
  def vida(self) -> int:
    return self._vida
  @vida.setter
  def vida(self, valor) -> None:
    self._vida = valor
  @property
  def posicion(self) -> int:
    return self._posicion
  @posicion.setter
  def posicion(self, valor) -> None:
    self._posicion = valor
  @property
  def velocidad(self) -> float:
    return self._velocidad
  @velocidad.setter
  def velocidad(self, valor) -> None:
    self._velocidad = valor
  def recibir_ataque(self, cantidad_recibida: int) -> None:
    self.vida = self.vida - cantidad_recibida
    if self.vida <= 0:
      print("La vida es menor o igual que cero!!!")
  def mover(self, direccion: int, velocidad: float) -> None:
    self.posicion = direccion
    self.velocidad = velocidad

class Soldado(Personaje):
  def __init__(self, vida: int, posicion: int, velocidad: float, ataque: int):
    super().__init__(vida, posicion, velocidad)
    self.ataque = ataque
  @property
  def ataque(self) -> int:
    return self._ataque
  @ataque.setter
  def ataque(self, valor) -> None:
    self._ataque = valor
  def atacar(self, otro_personaje: Personaje) -> None:
    otro_personaje.recibir_ataque(self.ataque)
  def __str__(self):
    return f"Soldado\n-Vida: {self.vida}\n-Posicion: {self.posicion}\n-Velocidad: {self.velocidad}\n-Ataque: {self.ataque}"

class Campesino(Personaje):
  def __init__(self, vida: int, posicion: int, velocidad: float, cosecha: int):
    super().__init__(vida, posicion, velocidad)
    self.cosecha = cosecha
  @property
  def cosecha(self) -> int:
    return self._cosecha
  @cosecha.setter
  def cosecha(self, valor) -> None:
    self._cosecha = valor
  def cosechar(self) -> int:
    return self.cosecha
  def __str__(self):
    return f"Campesino\n-Vida: {self.vida}\n-Posicion: {self.posicion}\n-Velocidad: {self.velocidad}\n-Cosecha: {self.cosecha}"
class ConexionBD:
  def __new__(cls, ip: str, puerto: int):
    print(f"Reservando memoria para la instancia de {cls.__name__}...")
    instancia = super().__new__(cls)
    return instancia
  def __init__(self, ip: str, puerto: int):
    self.ip = ip
    self.puerto = puerto
  def __del__(self):
    print(f"Cerrando conexión y liberando recursos para {self.ip}:{self.puerto}")
  
  @property
  def ip(self) -> str:
    return self._ip
  @ip.setter
  def ip(self, valor: str) -> None:
    self._ip = valor
  @property
  def puerto(self) -> int:
    return self._puerto
  @puerto.setter
  def puerto(self, valor: int) -> None:
    self._puerto = valor
  
  def __str__(self) -> str:
    return f"Conexion={self.ip};Puerto={self.puerto}"
  def __eq__(self, otro: ConexionBD) -> bool:
    return (self.ip, self.puerto) == (otro.ip, otro.puerto)
  def __lt__(self, otro: ConexionBD) -> bool:
    return self.puerto < otro.puerto
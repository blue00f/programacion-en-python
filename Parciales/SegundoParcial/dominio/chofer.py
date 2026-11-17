class Chofer:
  def __init__(self, nombre: str, dni: str, licencia: str):
    self.nombre = nombre
    self.dni = dni
    self.licencia = licencia

  def __str__(self):
    return f"{self.nombre} (DNI: {self.dni})"
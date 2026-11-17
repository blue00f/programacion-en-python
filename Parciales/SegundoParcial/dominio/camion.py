from dominio.chofer import Chofer

class Camion:
  def __init__(self, patente: str, litros_disponibles: float, ciudad_actual: str, km_litro: float, vel_maxima: float, chofer: Chofer):
    self.patente = patente
    self.litros_disponibles = litros_disponibles
    self.ciudad_actual = ciudad_actual
    self.km_litro = km_litro
    self.vel_maxima = vel_maxima
    self.chofer = chofer
  def __str__(self):
    return (f"Camión [{self.patente}] - Ubicación: {self.ciudad_actual} | Chofer:" f" {self.chofer.nombre}")
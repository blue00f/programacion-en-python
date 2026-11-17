import csv
import os
from config.valores import ARCHIVO_ESTIMACIONES, DISTANCIAS_CONFIG
from dominio.camion import Camion

class Estimacion:

  def __init__(self, patente: str, ciudades: list, km_totales: float, tiempo_total_horas: float, combustible_suficiente: bool):
    self.patente = patente
    self.ciudades = ciudades
    self.km_totales = km_totales
    self.tiempo_total_horas = tiempo_total_horas
    self.combustible_suficiente = combustible_suficiente

  def __str__(self):
    estado_combustible = ("SÍ alcanza" if self.combustible_suficiente else "NO alcanza")
    return (
        f"--- Reporte de Estimación ---\n"
        f"Patente: {self.patente}\n"
        f"Ruta: {' -> '.join(self.ciudades)}\n"
        f"Distancia Total: {self.km_totales} km\n"
        f"Tiempo Total Estimado: {self.tiempo_total_horas} horas\n"
        f"Combustible: {estado_combustible}\n"
    )


def estimar_viaje(camion: Camion, ciudad_destino: list) -> Estimacion:
  try:
    if not isinstance(camion, Camion):
      raise TypeError("El primer argumento debe ser una instancia de Camion.")
    if not ciudad_destino:
      raise ValueError("La lista de ciudades destino no puede estar vacía.")

    ruta_completa = [camion.ciudad_actual] + list(ciudad_destino)
    km_totales = 0.0
    tiempo_viaje_horas = 0.0

    for i in range(len(ruta_completa) - 1):
      origen = ruta_completa[i]
      destino = ruta_completa[i + 1]

      if (origen not in DISTANCIAS_CONFIG or destino not in DISTANCIAS_CONFIG[origen]):
        raise ValueError(f"No existe ruta directa configurada entre {origen} y {destino}.")

      distancia = DISTANCIAS_CONFIG[origen][destino]
      km_totales += distancia
      tiempo_viaje_horas += distancia / camion.vel_maxima

    tiempo_paradas_horas = (len(ruta_completa) - 1) * 1.0
    tiempo_total_horas = tiempo_viaje_horas + tiempo_paradas_horas

    consumo_necesario = km_totales / camion.km_litro
    combustible_suficiente = camion.litros_disponibles >= consumo_necesario

    estimacion = Estimacion(camion.patente, ruta_completa, km_totales, round(tiempo_total_horas, 2), combustible_suficiente)

    _persistir_estimacion_csv(estimacion)
    return estimacion

  except (TypeError, ValueError) as e:
    print(f"[Error de validación]: {e}")
    raise
  except Exception as e:
    print(f"[Error inesperado en estimar_viaje]: {e}")
    raise


def _persistir_estimacion_csv(estimacion: Estimacion):
  try:
    archivo_existe = os.path.exists(ARCHIVO_ESTIMACIONES)
    with open(ARCHIVO_ESTIMACIONES, mode="a", newline="", encoding="utf-8") as f:
      fieldnames = ["patente","ciudades","km_totales","tiempo_total_horas","combustible_suficiente",]
      writer = csv.DictWriter(f, fieldnames=fieldnames)

      if not archivo_existe or os.path.getsize(ARCHIVO_ESTIMACIONES) == 0:
        writer.writeheader()

      writer.writerow({
          "patente": estimacion.patente,
          "ciudades": " -> ".join(estimacion.ciudades),
          "km_totales": estimacion.km_totales,
          "tiempo_total_horas": estimacion.tiempo_total_horas,
          "combustible_suficiente": estimacion.combustible_suficiente,
      })
  except IOError as e:
    print(f"[Error de E/S al escribir en el archivo CSV]: {e}")


def buscar_estimaciones_por_patente(patente_buscada: str):
  try:
    if not os.path.exists(ARCHIVO_ESTIMACIONES):
      print("Aún no existen registros de estimaciones guardados.")
      return

    registros = []
    with open(ARCHIVO_ESTIMACIONES, mode="r", encoding="utf-8") as f:
      reader = csv.DictReader(f)
      for row in reader:
        row["km_totales"] = float(row["km_totales"])
        row["tiempo_total_horas"] = float(row["tiempo_total_horas"])
        registros.append(row)

    estimaciones_filtradas = list(
        filter(lambda x: x["patente"].upper() == patente_buscada.upper(), registros)
    )

    if not estimaciones_filtradas:
      print(f"No se encontraron registros para la patente: {patente_buscada}")
      return

    print(f"\n==========================================")
    print(f" HISTORIAL DE ESTIMACIONES (CSV): {patente_buscada.upper()}")
    print(f"==========================================\n")

    for idx, est in enumerate(estimaciones_filtradas, 1):
      supera = (
          "SÍ superó los 1000 km de distancia"
          if est["km_totales"] > 1000
          else "NO superó los 1000 km de distancia"
      )
      print(f"Viaje #{idx}:")
      print(f" • Ruta: {est['ciudades']}")
      print(f" • Distancia total: {est['km_totales']} km ({supera})")
      print(f" • Tiempo estimado: {est['tiempo_total_horas']} horas")
      print(f" • Combustible suficiente: {est['combustible_suficiente']}")
      print("-" * 40)

  except Exception as e:
    print(f"[Error al leer el archivo CSV de búsqueda]: {e}")
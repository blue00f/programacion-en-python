from config.valores import DISTANCIAS_CONFIG
from dominio.camion import Camion
from dominio.chofer import Chofer
from dominio.estimacion import buscar_estimaciones_por_patente, estimar_viaje

chofer1 = Chofer("Gomer Pail", "11223344", "B2")
chofer2 = Chofer("Lionel Messi", "55442266", "A3")
flota = {
	"AA123BB": Camion("AA123BB", 150.0, "Buenos Aires", 4.0, 80.0, chofer1),
	"CC789DD": Camion("CC789DD", 300.0, "Cordoba", 3.5, 90.0, chofer2),
}

def main():
  print("=== SISTEMA DE GESTIÓN Y ESTIMACIÓN DE FLOTA ===")
  print("\nCamiones disponibles:")
  for patente, camion in flota.items():
    print(
			f" • [{patente}] - Ubicación: {camion.ciudad_actual} | Chofer:"
			f" {camion.chofer.nombre}"
    )
  patente_ingresada = (input("\nIngrese la patente del camión a utilizar: ").strip().upper())
  if patente_ingresada not in flota:
    print("[Error] La patente ingresada no existe en la flota.")
    return
  camion_seleccionado = flota[patente_ingresada]
  ciudades_disponibles = list(DISTANCIAS_CONFIG.keys())
  print(f"\nCiudades disponibles en la red: {', '.join(ciudades_disponibles)}")
  print(f"Ubicación actual del camión: {camion_seleccionado.ciudad_actual}")

  destino_input = input("Ingrese las ciudades destino separadas por coma (ej: Rosario, Cordoba): ")
  ciudades_a_recorrer = [c.strip() for c in destino_input.split(",") if c.strip()]

  if not ciudades_a_recorrer:
    print("[Error] Debe ingresar al menos una ciudad destino.")
    return

  print("\n--- Simulando Viaje ---")
  try:
    resultado = estimar_viaje(camion_seleccionado, ciudades_a_recorrer)
    print(resultado)
  except Exception:
    pass

  consultar = (input("¿Desea consultar el historial de esta patente en el CSV? (s/n): ").strip().lower())
  if consultar == "s":
    buscar_estimaciones_por_patente(patente_ingresada)
    
if __name__ == "__main__":
  main()
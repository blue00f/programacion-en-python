DISTANCIAS_CONFIG = {
    "Buenos Aires": {"Rosario": 300, "Mar del Plata": 400, "Cordoba": 700},
    "Rosario": {"Buenos Aires": 300, "Cordoba": 400},
    "Mar del Plata": {"Buenos Aires": 400},
    "Cordoba": {"Buenos Aires": 700, "Rosario": 400, "Mendoza": 600},
    "Mendoza": {"Cordoba": 600},
}
ARCHIVO_ESTIMACIONES = "estimaciones_flota.csv"
from enum import Enum

class TipoInmueble(Enum):
	CASA = ("Casa",)
	DEPARTAMENTO = ("Departamento",)
	TERRENO = ("Terreno",)
	LOCAL_COMERCIAL = ("Local Comercial",)
	def __init__(self, descripcion: str):
		self.descripcion = descripcion

class Moneda(Enum):
	ARS = ("ARS",)
	USD = ("USD",)
	def __init__(self, descripcion: str):
		self.descripcion = descripcion

class EstadoInmueble(Enum):
    DISPONIBLE = ("Disponible",)
    VENDIDO = ("Vendido",)
    ELIMINADO = ("Eliminado",)
    def __init__(self, descripcion: str):
        self.descripcion = descripcion

def validar_texto(valor: str) -> bool:
	rdo = False
	if valor.strip() != "" and "|" not in valor:
		rdo = True
	return rdo

def validar_precio(valor: str) -> bool:
    rdo = False
    try:
        precio = float(valor.replace(",", "."))
        if precio > 0:
            rdo = True
    except ValueError:
        rdo = False
    return rdo

def validar_numero(valor: str) -> bool:
    rdo = False
    try:
        numero = int(valor)
        if numero > 0:
            rdo = True
    except ValueError:
        rdo = False
    return rdo

def validar_id(valor: str) -> bool:
    rdo = False
    if validar_texto(valor):
        rdo = True
    return rdo

def validar_opcion(valor: str, opciones: list[str]) -> bool:
    rdo = False
    if valor in opciones:
        rdo = True
    return rdo

def obtener_opciones(enumeracion: type[Enum]) -> list[str]:
    opciones = []
    for e in enumeracion:
        opciones.append(e.value[0])
    return opciones
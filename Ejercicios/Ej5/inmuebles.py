
import persistencia
import validaciones

class Inmueble:
    def __init__(self, id: str, tipo: str, calle: str, numero: int, barrio: str, precio: float, moneda: str,estado: str = "Disponible"):
        self.id = id
        self.tipo = tipo
        self.calle = calle
        self.numero = numero
        self.barrio = barrio
        self.precio = precio
        self.moneda = moneda
        self.estado = estado
    def convertir_a_diccionario(self) -> dict:
        inmueble = {
            "id": self.id,
            "tipo": self.tipo,
            "calle": self.calle,
            "numero": str(self.numero),
            "barrio": self.barrio,
            "precio": str(float(str(self.precio).replace(",", "."))),
            "moneda": self.moneda,
            "estado": self.estado
        }
        return inmueble

def alta(inmueble: Inmueble) -> bool:
    rdo = False
    registros = persistencia.cargar_inmuebles()
    if validaciones.validar_id(inmueble.id):
        if not existe_id(inmueble.id, registros):
            if validar_inmueble(inmueble):
                rdo = persistencia.agregar_inmueble(inmueble.convertir_a_diccionario())
    return rdo

def baja_logica(id: str) -> bool:
    rdo = False
    registros = persistencia.cargar_inmuebles()
    for r in registros:
        if r["id"] == id:
            if r["estado"] != "Eliminado":
                r["estado"] = "Eliminado"
                rdo = persistencia.guardar_inmuebles(registros)
            break
    return rdo

def modificar(id: str, campo: str, valor: str) -> bool:
    rdo = False
    registros = persistencia.cargar_inmuebles()
    campos_modificables = ["tipo", "calle", "numero", "barrio", "precio", "moneda", "estado"]
    if campo in campos_modificables:
        for r in registros:
            if r["id"] == id:
                if r["estado"] != "Eliminado":
                    if validar_modificacion(campo, valor):
                        if campo == "precio":
                            valor = str(float(valor.replace(",", ".")))
                        elif campo == "numero":
                            valor = str(int(valor))
                        r[campo] = valor
                        rdo = persistencia.guardar_inmuebles(registros)
                break
    return rdo

def listar(tipo: str = "", precio_min: float = 0, precio_max: float = 0) -> list[dict]:
    resultado = []
    registros = persistencia.cargar_inmuebles()
    for r in registros:
        coincide = True
        if r["estado"] == "Eliminado":
            coincide = False
        if tipo != "" and r["tipo"] != tipo:
            coincide = False
        precio = float(r["precio"])
        if precio_min > 0 and precio < precio_min:
            coincide = False
        if precio_max > 0 and precio > precio_max:
            coincide = False
        if coincide:
            resultado.append(r)
    return resultado

def buscar_por_id(id: str) -> dict | None:
    encontrado = None
    registros = persistencia.cargar_inmuebles()
    for r in registros:
        if r["id"] == id:
            if r["estado"] != "Eliminado":
                encontrado = r
            break
    return encontrado

def existe_id(id: str, registros: list[dict]) -> bool:
    rdo = False
    for r in registros:
        if r["id"] == id:
            rdo = True
            break
    return rdo

def validar_inmueble(inmueble: Inmueble) -> bool:
    rdo = False
    tipos = validaciones.obtener_opciones(validaciones.TipoInmueble)
    monedas = validaciones.obtener_opciones(validaciones.Moneda)
    estados = validaciones.obtener_opciones(validaciones.EstadoInmueble)
    if (
        inmueble.tipo in tipos
        and validaciones.validar_texto(inmueble.calle)
        and validaciones.validar_numero(str(inmueble.numero))
        and validaciones.validar_texto(inmueble.barrio)
        and validaciones.validar_precio(str(inmueble.precio))
        and inmueble.moneda in monedas
        and inmueble.estado in estados
    ):
        rdo = True
    return rdo

def validar_modificacion(campo: str, valor: str) -> bool:
    rdo = False
    if campo == "tipo":
        opciones = validaciones.obtener_opciones(validaciones.TipoInmueble)
        rdo = validaciones.validar_opcion(valor, opciones)
    elif campo == "calle" or campo == "barrio":
        rdo = validaciones.validar_texto(valor)
    elif campo == "numero":
        rdo = validaciones.validar_numero(valor)
    elif campo == "precio":
        rdo = validaciones.validar_precio(valor)
    elif campo == "moneda":
        opciones = validaciones.obtener_opciones(validaciones.Moneda)
        rdo = validaciones.validar_opcion(valor, opciones)
    elif campo == "estado":
        opciones = [validaciones.EstadoInmueble.DISPONIBLE.value[0], validaciones.EstadoInmueble.VENDIDO.value[0]]
        rdo = validaciones.validar_opcion(valor, opciones)
    return rdo

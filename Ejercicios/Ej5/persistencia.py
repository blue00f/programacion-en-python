import os
ARCHIVO = "inmuebles.txt"

def inicializar_archivo() -> bool:
    rdo = False
    try:
        if not os.path.exists(ARCHIVO):
            with open(ARCHIVO, "w", encoding="utf-8"):
                pass
        rdo = True
    except OSError as error:
        print(f"Error al inicializar el archivo: {error}")
    return rdo

def cargar_inmuebles() -> list[dict]:
    inmuebles = []
    try:
        inicializar_archivo()
        with open(ARCHIVO, "r", encoding="utf-8") as archivo:
            for l in archivo:
                campos = l.rstrip("\n").split("|")

                if len(campos) == 8:
                    inmueble = {
                        "id": campos[0],
                        "tipo": campos[1],
                        "calle": campos[2],
                        "numero": campos[3],
                        "barrio": campos[4],
                        "precio": campos[5],
                        "moneda": campos[6],
                        "estado": campos[7]
                    }
                    inmuebles.append(inmueble)
    except OSError as error:
        print(f"Error al leer el archivo: {error}")
    return inmuebles

def agregar_inmueble(inmueble: dict) -> bool:
    rdo = False
    try:
        inicializar_archivo()
        with open(ARCHIVO, "a", encoding="utf-8") as archivo:
            campos = [
                inmueble["id"],
                inmueble["tipo"],
                inmueble["calle"],
                inmueble["numero"],
                inmueble["barrio"],
                str(inmueble["precio"]),
                inmueble["moneda"],
                inmueble["estado"]
            ]
            archivo.write("|".join(campos) + "\n")
        rdo = True

    except OSError as error:
        print(f"Error al guardar el inmueble: {error}")
    return rdo

def guardar_inmuebles(inmuebles: list[dict]) -> bool:
    rdo = False
    try:
        with open(ARCHIVO, "w", encoding="utf-8") as archivo:
            for inmueble in inmuebles:
                campos = [
                    inmueble["id"],
                    inmueble["tipo"],
                    inmueble["calle"],
                    inmueble["numero"],
                    inmueble["barrio"],
                    str(inmueble["precio"]),
                    inmueble["moneda"],
                    inmueble["estado"]
                ]
                archivo.write("|".join(campos) + "\n")
        rdo = True
    except OSError as error:
        print(f"Error al actualizar el archivo: {error}")
    return rdo

import inmuebles
import persistencia
import validaciones

def mostrar_menu() -> None:
    print("\n===== CATÁLOGO INMOBILIARIO =====")
    print("1. Alta de inmueble")
    print("2. Baja lógica")
    print("3. Modificar inmueble")
    print("4. Listar inmuebles")
    print("5. Buscar por ID")
    print("0. Salir")

def solicitar_inmueble() -> inmuebles.Inmueble:
    id = input("ID: ").strip()
    print("\nTipos disponibles:")
    tipos = validaciones.obtener_opciones(validaciones.TipoInmueble)
    
    for tipo in tipos:
        print(f"- {tipo}")

    tipo = input("Tipo: ").strip()
    calle = input("Calle: ").strip()
    numero = input("Número: ").strip()
    barrio = input("Barrio: ").strip()
    precio = input("Precio: ").strip()
    monedas = validaciones.obtener_opciones(validaciones.Moneda)
    print(f"Monedas disponibles: {monedas}")
    moneda = input("Moneda: ").strip()
    estado = "Disponible"
    inmueble = inmuebles.Inmueble(id, tipo, calle, int(numero), barrio, float(precio.replace(",", ".")), moneda, estado)
    return inmueble


def mostrar_inmuebles(registros: list[dict]) -> None:
    if len(registros) == 0:
        print("No hay inmuebles para mostrar.")
    else:
        print(f"\n{'ID':<10} {'TIPO':<20} {'DIRECCIÓN':<30} {'PRECIO':<15} {'MONEDA':<8} {'ESTADO':<12}")
        print("-" * 100)
        for r in registros:
            direccion = (
                f"{r['calle']} "
                f"{r['numero']}, {r['barrio']}"
            )
            print(
                f"{r['id']:<10} "
                f"{r['tipo']:<20} "
                f"{direccion:<30} "
                f"{r['precio']:<15} "
                f"{r['moneda']:<8} "
                f"{r['estado']:<12}"
            )

def ejecutar() -> None:
    opcion = ""
    persistencia.inicializar_archivo()
    while opcion != "0":
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()
        if opcion == "1":
            inmueble = solicitar_inmueble()
            if inmuebles.alta(inmueble):
                print("Inmueble registrado correctamente.")
            else:
                print("No se pudo registrar. Verifique los datos y que el ID no exista")
                
        elif opcion == "2":
            id = input("ID del inmueble a dar de baja: ").strip()
            registro = inmuebles.buscar_por_id(id)
            if registro is not None:
                mostrar_inmuebles([registro])
                confirmacion = input("¿Confirma la baja lógica? (S/N): ").strip().upper()

                if confirmacion == "S":
                    if inmuebles.baja_logica(id):
                        print("Inmueble marcado como eliminado.")
                    else:
                        print("No se pudo realizar la baja.")
                else:
                    print("Operación cancelada.")
            else:
                print("Inmueble inexistente.")

        elif opcion == "3":
            id = input("ID del inmueble a modificar: ").strip()
            registro = inmuebles.buscar_por_id(id)
            if registro is not None:
                mostrar_inmuebles([registro])
                campos = {
                    "1": "tipo",
                    "2": "calle",
                    "3": "numero",
                    "4": "barrio",
                    "5": "precio",
                    "6": "moneda",
                    "7": "estado"
                }

                print("\n¿Qué desea modificar?")
                for clave, campo in campos.items():
                    print(f"{clave}. {campo.capitalize()}")

                seleccion = input("Opción: ").strip()

                if seleccion in campos:
                    campo = campos[seleccion]

                    if campo == "tipo":
                        print(validaciones.obtener_opciones(validaciones.TipoInmueble))
                    elif campo == "moneda":
                        print(validaciones.obtener_opciones(validaciones.Moneda))
                    elif campo == "estado":
                        print(["Disponible", "Vendido"])
                    valor = input("Nuevo valor: ").strip()

                    if inmuebles.modificar(id, campo, valor):
                        print("Inmueble modificado correctamente.")
                    else:
                        print("No se pudo modificar. Verifique el valor ingresado.")
                else:
                    print("Opción inválida.")
            else:
                print("Inmueble inexistente.")

        elif opcion == "4":
            print("\n1. Listar todos los disponibles y vendidos")
            print("2. Filtrar por tipo")
            print("3. Filtrar por rango de precios")

            filtro = input("Seleccione un filtro: ").strip()

            if filtro == "1":
                registros = inmuebles.listar()

            elif filtro == "2":
                tipos = validaciones.obtener_opciones(validaciones.TipoInmueble)
                print(tipos)
                tipo = input("Tipo a buscar: ").strip()
                registros = inmuebles.listar(tipo=tipo)

            elif filtro == "3":
                minimo = input("Precio mínimo (0 para no limitar): ").strip()
                maximo = input("Precio máximo (0 para no limitar): ").strip()

                if (validaciones.validar_precio(minimo) or minimo == "0") and (validaciones.validar_precio(maximo) or maximo == "0"):
                    registros = inmuebles.listar(
                        precio_min=float(minimo.replace(",", ".")),
                        precio_max=float(maximo.replace(",", "."))
                    )
                else:
                    registros = []
                    print("Rango de precios inválido.")
            else:
                registros = []
                print("Filtro inválido.")
            mostrar_inmuebles(registros)

        elif opcion == "5":
            id = input("ID a buscar: ").strip()
            registro = inmuebles.buscar_por_id(id)

            if registro is not None:
                mostrar_inmuebles([registro])
            else:
                print("Inmueble inexistente.")

        elif opcion == "0":
            print("Saliendo del sistema...")

        else:
            print("Opción inválida.")


if __name__ == "__main__":
    ejecutar()

from comercio import Producto, ProductoFisico, Cliente, Orden

try:
    cliente1 = Cliente("Laura Gómez", "laura@gmail.com")

    prod_digital = Producto("E-Book Python", 1500.0)
    prod_fisico = ProductoFisico("Teclado Mecánico", 12000.0, 1.5)

    orden1 = Orden(cliente1)
    orden1.agregar_producto(prod_digital)
    orden1.agregar_producto(prod_fisico)

    print("=== ORDEN CREADA EXITOSAMENTE ===")
    print(orden1)
    print("\nDetalle de items:")
    for item in orden1.productos:
        print(f" - {item}")
except (ValueError, TypeError) as e:
    print(f"Error de validación: {e}")


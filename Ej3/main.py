from modelo import GeneradorFacturaA, GeneradorFacturaB

# Ejemplo del patrón creacional Factory Method

print("--- Factura A ---")
generador = GeneradorFacturaA()
print(generador.emitir_factura(2000))

print("--- Factura B ---")
generador = GeneradorFacturaB()
print(generador.emitir_factura(2500))
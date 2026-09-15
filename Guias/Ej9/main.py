from modelo import ConexionBD

print(f"\n=== Creación de objetos (__new__ e __init__) ===")
con1 = ConexionBD("192.168.0.10", 3306)
con2 = ConexionBD("192.168.0.10", 3306)
con3 = ConexionBD("192.168.0.30", 5432)

print(f"\n=== Impresión de objetos (__str__) ===")
print(con1)
print(con2)
print(con3)

# __cmp__ no de usa más en la versión 3, fue reemplazado por;
# __eq__ (==), __ne__ (!=), __lt__ (<), __gt__ (>), __le__ (<=), __ge__ (>=)
print(f"\n=== Comparaciones __eq__ y __lt__ (sustituto moderno de __cmp__) ===")
print(f"¿con1 == con2? -> {con1 == con2}")
print(f"¿con1 == con3? -> {con1 == con3}")
print(f"¿con1={con1.puerto} < con3={con3.puerto}? -> {con1 < con3}")

print(f"\n=== Eliminación de con1 (__del__) ===")
del con1

print("El programa continúa su ejecución...\n\n")
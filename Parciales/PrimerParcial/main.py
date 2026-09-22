from modelo import Soldado, Campesino

s1 = Soldado(100, 20, 130.5, 60)
s2 = Soldado(400, 100, 40, 400)
print("=== Datos del soldado 1 ===")
print(s1)
print("\n=== Datos del soldado 2 ===")
print(s2)

c1 = Campesino(20, 50, 5.5, 200)
print("\n=== Datos del campesino ===")
print(c1)
c1.mover(300, 6.5)
print("\n=== Datos del campesino luego de MOVERSE ===")
print(c1)


cantidad_cosecha = c1.cosechar()
print("\n=== Cantidad de cosechas del campesino ===")
print(f"El campesino tiene {cantidad_cosecha} cosechas")


print("\n=== Soldado 2 ataca al campesino ===")
s2.atacar(c1)

print("\n=== Soldado 2 ataca al soldado 1 ===")
s2.atacar(s1)

# No se ejecuta esta línea porque el campesino no puede atacar al soldado ni a otro campesino
# c1.atacar(s1) 
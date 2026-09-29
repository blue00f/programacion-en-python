from modelo import TipoVaso, Cerveza, Barril, AfterOffice
from functools import reduce

# 1. Instanciamos el sistema gestor
negocio = AfterOffice("Cervecería - After Office")

# 2. Creación de Cervezas
rubia_nac = Cerveza("Rubia", "Nacional", 50.0)
negra_nac = Cerveza("Negra", "Nacional", 58.0)
rubia_ext = Cerveza("Rubia", "Extranjero", 65.0)

# 3. Creación y adición de Barriles al gestor
barril1 = Barril(rubia_nac)
barril2 = Barril(negra_nac)
barril3 = Barril(rubia_ext)
barril4 = Barril(rubia_nac)

for b in [barril1, barril2, barril3, barril4]:
  negocio.agregar_barril(b)

# 4. Registro de ventas a través de la clase gestora
negocio.registrar_venta(barril1, TipoVaso.CHOPP)
negocio.registrar_venta(barril1, TipoVaso.JARRA)
negocio.registrar_venta(barril1, TipoVaso.VASO)
negocio.registrar_venta(barril2, TipoVaso.JARRA)
negocio.registrar_venta(barril2, TipoVaso.JARRA)
negocio.registrar_venta(barril3, TipoVaso.VASO)
negocio.registrar_venta(barril3, TipoVaso.CHOPP)
negocio.registrar_venta(barril3, TipoVaso.JARRA)
negocio.registrar_venta(barril4, TipoVaso.VASO)
negocio.registrar_venta(barril4, TipoVaso.VASO)


print(f"==================================================")
print(f" SISTEMA DE GESTIÓN - {negocio.nombre.upper()}")
print(f"==================================================\n")

print(f"1) Recaudación Total: ${negocio.recaudacion_total:,.2f}")

b_mas = negocio.barril_mas_sirvio()
b_menos = negocio.barril_menos_sirvio()
print(f"2) Barril MÁS sirvió: #{b_mas.id} ({b_mas.cerveza.nombre}) -> {b_mas.litros_servidos:.2f}L")
print(f"   Barril MENOS sirvió: #{b_menos.id} ({b_menos.cerveza.nombre}) -> {b_menos.litros_servidos:.2f}L")

b_rec = negocio.barril_mas_recaudo()
print(f"3) Barril con MÁS recaudación: #{b_rec.id} ({b_rec.cerveza.nombre}) -> ${b_rec.recaudacion_total:,.2f}")

c_ven = negocio.cerveza_mas_vendida()
print(f"4) Cerveza más vendida (transacciones): {c_ven.nombre}")

c_gan = negocio.cerveza_mas_ganancia()
print(f"5) Cerveza que generó MÁS ganancia: {c_gan.nombre}")

c_max_l = negocio.cerveza_mas_litros()
c_min_l = negocio.cerveza_menos_litros()
print(f"6) Cerveza con MAYOR volumen: {c_max_l.nombre}")
print(f"7) Cerveza con MENOR volumen: {c_min_l.nombre}")

vaso = negocio.vaso_mas_solicitado()
print(f"8) Vaso MÁS solicitado: {vaso.descripcion}")

print("\n9) % Venta (litros) por Cerveza:")
for c, pct in negocio.porcentaje_litros_por_cerveza():
  print(f"   - {c.nombre} ({c.origen}): {pct:.2f}%")

print("\n10) % Recaudación por Cerveza:")
for c, pct in negocio.porcentaje_recaudacion_por_cerveza():
  print(f"   - {c.nombre} ({c.origen}): {pct:.2f}%")

print("\n11) % Venta (litros) por Barril:")
for b, pct in negocio.porcentaje_litros_por_barril():
  print(f"   - Barril #{b.id} ({b.cerveza.nombre}): {pct:.2f}%")

print("\n12) % Recaudación por Barril:")
for b, pct in negocio.porcentaje_recaudacion_por_barril():
  print(f"   - Barril #{b.id} ({b.cerveza.nombre}): {pct:.2f}%")
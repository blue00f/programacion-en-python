from modelo import TipoVaso, Cerveza, Barril, Venta
from functools import reduce

rubia_nac = Cerveza("Rubia", "Nacional", 50.0)
negra_nac = Cerveza("Negra", "Nacional", 58.0)
rubia_ext = Cerveza("Rubia", "Extranjera", 65.0)

barril1 = Barril(rubia_nac)
barril2 = Barril(negra_nac)
barril3 = Barril(rubia_ext)
barril4 = Barril(rubia_nac)

barriles = [barril1, barril2, barril3, barril4]
cervezas = [rubia_nac, negra_nac, rubia_ext]

ventas = [
    Venta(barril1, TipoVaso.CHOPP),
    Venta(barril1, TipoVaso.JARRA),
    Venta(barril1, TipoVaso.VASO),
    Venta(barril2, TipoVaso.JARRA),
    Venta(barril2, TipoVaso.JARRA),
    Venta(barril3, TipoVaso.VASO),
    Venta(barril3, TipoVaso.CHOPP),
    Venta(barril3, TipoVaso.JARRA),
    Venta(barril4, TipoVaso.VASO),
    Venta(barril4, TipoVaso.VASO),
  ]

# Funciones auxiliares para filtrar datos
def sumar_montos_venta(acumulador: float, venta: Venta) -> float:
  return acumulador + venta.monto_total

def obtener_litros_servidos_barril(barril: Barril) -> float:
  return barril.litros_servidos

def obtener_recaudacion_barril(barril: Barril) -> float:
  return barril.recaudacion_total

def contar_transacciones_cerveza(cerveza: Cerveza, ventas: list[Venta]) -> int:
  def pertenece_a_cerveza(venta: Venta) -> bool:
    return venta.barril.cerveza == cerveza
  ventas_filtradas = filter(pertenece_a_cerveza, ventas)
  return len(list(ventas_filtradas))

def obtener_recaudacion_por_cerveza(cerveza: Cerveza, ventas: list[Venta]) -> float:
  def pertenece_a_cerveza(venta: Venta) -> bool:
    return venta.barril.cerveza == cerveza
  ventas_filtradas = filter(pertenece_a_cerveza, ventas)
  return sum(v.monto_total for v in ventas_filtradas)

def obtener_litros_por_cerveza(cerveza: Cerveza, ventas: list[Venta]) -> float:
  def pertenece_a_cerveza(venta: Venta) -> bool:
    return venta.barril.cerveza == cerveza
  ventas_filtradas = filter(pertenece_a_cerveza, ventas)
  return sum(v.litros_vendidos for v in ventas_filtradas)

# 1 Calcular la recaudación total del after.
recaudacion_total = reduce(sumar_montos_venta, ventas, 0.0)
total_litros_vendidos = sum(v.litros_vendidos for v in ventas)
print(f"\nRecaudación total: ${recaudacion_total}")

# 2 Obtener el barril que más y menos cerveza sirvió
barril_mas_vendido = max(barriles, key=obtener_litros_servidos_barril)
barril_menos_vendido = min(barriles, key=obtener_litros_servidos_barril)
print(f"\nEl barril que más sirvió:\n\t{barril_mas_vendido}\nEl barril que menos sirvió:\n\t{barril_menos_vendido}")

# 3 Obtener el barril que más dinero recaudó
barril_mas_recaudo = max(barriles, key=obtener_recaudacion_barril)
print(f"\nEl barril que más recaudó es:\n\t{barril_mas_recaudo}")

def criterio_ventas_cerveza(c: Cerveza) -> int:
  return contar_transacciones_cerveza(c, ventas)

def criterio_recaudacion_cerveza(c: Cerveza) -> float:
  return obtener_recaudacion_por_cerveza(c, ventas)

def criterio_litros_cerveza(c: Cerveza) -> float:
  return obtener_litros_por_cerveza(c, ventas)

# 4 Mostrar la cerveza más vendida (unidades)
cerveza_mas_vendida = max(cervezas, key=criterio_ventas_cerveza)
print(f"\nCerveza más vendida: {cerveza_mas_vendida} -> {contar_transacciones_cerveza(cerveza_mas_vendida, ventas)} transacciones")

# 5 Mostrar la cerveza que generó más ganancia
cerveza_mas_ganancia = max(cervezas, key=criterio_recaudacion_cerveza)
print(f"\nCerveza que generó más ganancia: {cerveza_mas_ganancia} -> {obtener_recaudacion_por_cerveza(cerveza_mas_vendida, ventas)}")

# 6 Cerveza que se vendió mayor cantidad de litros
cerveza_mas_litros = max(cervezas, key=criterio_litros_cerveza)
print(f"\nCerveza con mayor cantidad de litros vendida: {cerveza_mas_litros} -> {obtener_litros_por_cerveza(cerveza_mas_litros, ventas)}L")

# 7 Cerveza que se vendió menor cantidad de litros
cerveza_menos_litros = min(cervezas, key=criterio_litros_cerveza)
print(f"\nCerveza con menos cantidad de litros vendida: {cerveza_menos_litros} -> {obtener_litros_por_cerveza(cerveza_menos_litros, ventas)}L")

# 8 Obtener el tipo de vaso que más se solciitó
def contar_usos_vaso(tipo_vaso: TipoVaso) -> int:
  def es_mismo_vaso(v: Venta) -> bool:
    return v.tipo_vaso == tipo_vaso
  return len(list(filter(es_mismo_vaso, ventas)))

vaso_mas_solicitado = max(list(TipoVaso), key=contar_usos_vaso)
print(f"\nVaso más solicitado: {vaso_mas_solicitado.descripcion} -> {contar_usos_vaso(vaso_mas_solicitado)}")

# 9 Porcentaje de venta (litros) por tipo de cerveza 
def calcular_pct_litros_cerveza(c: Cerveza) -> tuple[Cerveza, float]:
  litros = obtener_litros_por_cerveza(c, ventas)
  pct = (litros / total_litros_vendidos * 100) if total_litros_vendidos > 0 else 0.0
  return (c, pct)  

print("\nPorcentaje de ventas (en L) por tipo de cerveza")
pct_litros_cerveza = list(map(calcular_pct_litros_cerveza, cervezas))
for cerveza, pct in pct_litros_cerveza:
  print(f"\t-{cerveza.nombre} {cerveza.origen}: {pct:.2f}%")

# 10 Porcentaje de reacudación por tipo de cerveza
def calcular_pct_recaudacion_cerveza(c: Cerveza) -> tuple[Cerveza, float]:
  recaudacion = obtener_recaudacion_por_cerveza(c, ventas)
  pct = (recaudacion / recaudacion_total * 100) if recaudacion_total > 0 else 0.0
  return (c, pct)

print("\nPorcentaje de recaudación por tipo de cerveza")
pct_recaudacion_cerveza = list(map(calcular_pct_recaudacion_cerveza, cervezas))
for cerveza, pct in pct_recaudacion_cerveza:
  print(f"\t{cerveza.nombre} {cerveza.origen}: {pct:.2f}%")

# 11 Porcentaje de venta (litros) por barril
def calcular_pct_litros_barril(b: Barril) -> tuple[Barril, float]:
  pct = (b.litros_servidos / total_litros_vendidos * 100) if total_litros_vendidos > 0 else 0.0
  return (b, pct)

print("\nPorcentaje de venta (en L) por barril")
pct_litros_barril = list(map(calcular_pct_litros_barril, barriles))
for barril, pct in pct_litros_barril:
  print(f"\tBarril #{barril.id} {barril.cerveza.nombre}: {pct:.2f}%")

# 12 Porcentaje de recaudación por barril
def calcular_pct_recaudacion_barril(b: Barril) -> tuple[Barril, float]:
  pct = (b.recaudacion_total / recaudacion_total * 100) if recaudacion_total > 0 else 0.0
  return (b, pct)

print("\nPorcentaje de recaudación por barril")
pct_recaudacion_barril = list(map(calcular_pct_recaudacion_barril, barriles))
for barril, pct in pct_recaudacion_barril:
  print(f"\tBarril #{barril.id} {barril.cerveza.nombre}: {pct:.2f}%")
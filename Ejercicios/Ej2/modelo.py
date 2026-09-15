from abc import ABC, abstractmethod

# Clase Abstracta
class ProcesadorPago(ABC):
  @abstractmethod
  def procesar(self, monto: float) -> bool:
    pass
  @abstractmethod
  def obtener_nombre_pasarela(self) -> str:
    pass

# Implementación concreta 1
class ProcesadorMercadoPago(ProcesadorPago):
  def procesar(self, monto: float) -> bool:
    print(f"Cobrando {monto} con MercadoPago...")
    return True
  def obtener_nombre_pasarela(self) -> str:
    return "MercadoPago"

# Implementación concreta 2
class ProcesadorStripe(ProcesadorPago):
  def procesar(self, monto: float) -> bool:
    print(f"Cobrando {monto} con Stripe...")
    return True
  def obtener_nombre_pasarela(self) -> str:
    return "Stripe"
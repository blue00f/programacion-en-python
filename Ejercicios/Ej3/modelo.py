from abc import ABC, abstractmethod

class Factura(ABC):
  @abstractmethod
  def generar_comprobante(self, monto: float) -> str:
    pass

class FacturaA(Factura):
  def generar_comprobante(self, monto: float) -> str:
    iva = monto * 0.21
    total = monto + iva
    return f"[Factura A - Resp. Inscripto] Subtotal: ${monto} | IVA (21%): ${iva:} | Total: ${total}"

class FacturaB(Factura):
  def generar_comprobante(self, monto: float) -> str:
    return f"[Factura B - Consumidor Final] Total Final: ${monto}"

class GeneradorFactura(ABC):
  @abstractmethod
  def crear_factura(self) -> Factura:
    pass
  def emitir_factura(self, monto: float) -> str:
    factura = self.crear_factura()
    resultado = f"{factura.generar_comprobante(monto)}"
    return resultado

class GeneradorFacturaA(GeneradorFactura):
  def crear_factura(self) -> Factura:
    return FacturaA()
  
class GeneradorFacturaB(GeneradorFactura):
  def crear_factura(self) -> Factura:
    return FacturaB()
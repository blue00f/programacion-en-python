from modelo import ProcesadorPago, ProcesadorMercadoPago, ProcesadorStripe

# No deja instanciar una clase abstracta
# pago = ProcesadorPago()

pago = ProcesadorMercadoPago()
pago.procesar(1400)

pago = ProcesadorStripe()
pago.procesar(1200)

def dividir_numeros(dividendo_str, divisor_str):
  try:
    dividendo = float(dividendo_str)
    divisor = float(divisor_str)
    res = dividendo/divisor
  except ValueError as e:
    print(f"[ERROR] ValueError: Debe ingresar valores numéricos. (Detalle: {e})")
  except ZeroDivisionError as e:
    print(f"[ERROR] ZeroDivisionError: No se puede dividir por cero. (Detalle: {e})")
  except Exception as e:
    print(f"[ERROR] Ocurrió un error inesperado: {e}")
  else:
    print(f"[ÉXITO] División realizada correctamente. Resultado: {res}")
  finally:
    print(f"Liberando posibles recursos...")


dividir_numeros("10","2")
dividir_numeros("10", "0")
dividir_numeros("bla", "2")

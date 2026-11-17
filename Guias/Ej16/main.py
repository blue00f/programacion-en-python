import time
import functools

def registrar_log(funcion_original):
  def envoltura(*args, **kwargs):
    print(f"[LOG] >>> Iniciando ejecución de la función")
    res = funcion_original(*args, **kwargs)
    print(f"[LOG] <<< Finalizó la ejecución de la función\n")
    return res
  return envoltura

def medir_tiempo(funcion_original):
  def envoltura(*args, **kwargs):
    inicio = time.time()
    res = funcion_original(*args, **kwargs)
    fin = time.time()
    tiempo_transcurrido = fin - inicio
    print(f"[TIEMPO] La función tomó {tiempo_transcurrido:.6f} segundos en ejecutarse.")
    return res
  return envoltura

@registrar_log
@medir_tiempo
def proceso_pesado(limite):
  print(" -> procesando datos...")
  suma = sum(x**2 for x in range(limite))
  return suma

print("=== Iniciando programa principal ===")
resultado_final = proceso_pesado(50000000)
print(f"Resultado obtenido: {resultado_final}")
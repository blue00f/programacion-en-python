import pickle

# Para archivos de texto
nombre_archivo_texto = "ejemplo.txt"
try:
  archivo_txt = open(nombre_archivo_texto, "w", encoding="utf-8")
  archivo_txt.write("Línea 1: Hola, mundo.\n")
  archivo_txt.write("Línea 2: Aprendiendo manejo de archivos en Python.\n")
except OSError as e:
  print(f"No se pudo abrir o escribir el archivo de texto: {e}")
else:
  print("Archivo de texto guardado correctamente.")
finally:
  try:
    archivo_txt.close()
  except NameError:
    pass

try:
  archivo_txt = open(nombre_archivo_texto, "r", encoding="utf-8")
  contenido_txt = archivo_txt.read()
except FileNotFoundError as e:
  print(f"[ERROR] El archivo '{nombre_archivo_texto}' no existe. Detalle: {e}")
except PermissionError as e:
  print(f"[ERROR] Sin permisos para leer el archivo. Detalle: {e}")
except OSError as e:
  print(f"[ERROR] Error de E/S al leer el archivo: {e}")
else:
  print("--- Archivo de Texto ---")
  print(contenido_txt)
finally:
  try:
    archivo_txt.close()
  except NameError:
    pass


# Para archivos binarios
nombre_archivo_binario = "datos.bin"
datos_complejos = {"usuario": "Ana", "puntaje": 95, "cursos": ["Python", "SQL"]}
try:
  archivo_bin = open(nombre_archivo_binario, "wb")
  pickle.dump(datos_complejos, archivo_bin)
except OSError as e:
  print(f"[ERROR] No se pudo escribir el archivo binario: {e}")
else:
  print("[ÉXITO] Archivo binario guardado correctamente.")
finally:
  try:
    archivo_bin.close()
  except NameError:
    pass

try:
  archivo_bin = open(nombre_archivo_binario, "rb")
  datos_recuperados = pickle.load(archivo_bin)
except FileNotFoundError as e:
  print(f"El archivo '{nombre_archivo_binario}' no existe. Detalle: {e}")
except pickle.UnpicklingError as e:
  print(f"El archivo binario está corrupto o no se pudo deserializar: {e}")
except OSError as e:
  print(f"Error de E/S al leer el archivo binario: {e}")
else:
  print("--- Archivo Binario ---")
  print(datos_recuperados)
  print(f"Tipo de datos recuperados: {type(datos_recuperados)}")
finally:
  try:
    archivo_bin.close()
  except NameError:
    pass
  
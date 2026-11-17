import pickle

nombre_archivo_texto = "ejemplo.txt"

# Creación, escritura y cierre
archivo_txt = open(nombre_archivo_texto, "w", encoding="utf-8")
archivo_txt.write("Línea 1: Hola, mundo.\n")
archivo_txt.write("Línea 2: Aprendiendo manejo de archivos en Python.\n")
archivo_txt.close()

# Apertura, lectura y cierre
archivo_txt = open(nombre_archivo_texto, "r", encoding="utf-8")
contenido_txt = archivo_txt.read()
archivo_txt.close()

print("--- Archivo de Texto ---")
print(contenido_txt)

# Archivo de datos binarios
nombre_archivo_binario = "datos.bin"
datos_complejos = {"usuario": "Ana", "puntaje": 95, "cursos": ["Python", "SQL"]}

# Creación, escritura y cierre (binario)
archivo_bin = open(nombre_archivo_binario, "wb")
pickle.dump(datos_complejos, archivo_bin)
archivo_bin.close()

# Apertura, lectura y cierre (binario)
archivo_bin = open(nombre_archivo_binario, "rb")
datos_recuperados = pickle.load(archivo_bin)
archivo_bin.close()

print("--- Archivo Binario ---")
print(datos_recuperados)
print(f"Tipo de datos recuperados: {type(datos_recuperados)}")
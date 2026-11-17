import re

# archivo simulado
nombre_origen = "registro.txt"
with open(nombre_origen, "w", encoding="utf-8") as f:
    f.write("Contacto 1: ana.gomez@gmail.com - Activa\n")
    f.write("Este es un texto sin correo electrónico.\n")
    f.write("Soporte técnico: soporte@empresa.org\n")
    f.write("Visita nuestra web oficial.\n")
    f.write("Contacto alternativo: carlos_99@yahoo.es\n")

nombre_coincidencias = "con_email.txt"
nombre_sin_coincidencias = "sin_email.txt"

# Expresión regular para buscar direcciones de correo electrónico
patron_email = r'[\w\.-]+@[\w\.-]+\.\w+'

try:
    # Apertura simultánea de los archivos de lectura y escritura
    with open(nombre_origen, "r", encoding="utf-8") as archivo_origen, \
         open(nombre_coincidencias, "w", encoding="utf-8") as archivo_match, \
         open(nombre_sin_coincidencias, "w", encoding="utf-8") as archivo_nomatch:
        for linea in archivo_origen:
            if re.search(patron_email, linea):
                archivo_match.write(linea)
            else:
                archivo_nomatch.write(linea)  
    print("[ÉXITO] Archivo procesado y líneas clasificadas correctamente.")
except OSError as e:
    print(f"[ERROR] Ocurrió un problema al gestionar los archivos: {e}")
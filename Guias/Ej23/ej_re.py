import re

def ejecutar():
    print("\n--- 2. RE (Expresiones Regulares) ---")
    texto = "Contactos: juan@email.com y maria.perez@empresa.org"
    patron = r'[\w\.-]+@[\w\.-]+\.\w+'
    emails = re.findall(patron, texto)
    print("Emails encontrados:", emails)
from PIL import Image

def ejecutar():
    print("\n--- 5. PILLOW (PIL) ---")
    img = Image.new("RGB", (100, 100), color="red")
    img.save("imagen_prueba.png")
    print("Imagen 'imagen_prueba.png' creada y guardada con éxito.")
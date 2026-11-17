from collections import Counter, namedtuple

def ejecutar():
    print("--- 1. COLLECTIONS ---")
    contador = Counter(["manzana", "banana", "manzana", "naranja", "banana", "manzana"])
    print("Conteo más común:", contador.most_common(1))
    
    Punto = namedtuple("Punto", ["x", "y"])
    p = Punto(10, 20)
    print(f"NamedTuple: x={p.x}, y={p.y}")
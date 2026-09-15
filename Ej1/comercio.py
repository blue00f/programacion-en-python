class Producto:
  _nombre: str # Se define para documentación, autocompletado y linters
  _precio: float
  def __init__(self, nombre: str, precio: float):
    self.nombre = nombre
    self.precio = precio

  # Getter y Setter para el campo _nombre
  @property
  def nombre(self) -> str:
    return self._nombre
  @nombre.setter
  def nombre(self, valor: str) -> None:
    if not valor or not valor.strip():
      raise ValueError("El nombre del producto no puede estar vacio")
    self._nombre = valor.strip()

  # Getter y Setter para el campo _precio
  @property
  def precio(self) -> float:
    return self._precio
  @precio.setter
  def precio(self, valor: float) -> None:
    if valor <= 0:
      raise ValueError("El precio del producto debe ser mayor a $0")
    self._precio = valor

  def __repr__(self) -> str:
    return f"Producto(nombre='{self.nombre}',precio=${self.precio})"

class ProductoFisico(Producto):
  peso_kg: float
  def __init__(self, nombre: str, precio: float, peso_kg: float):
    super().__init__(nombre, precio)
    self.peso_kg = peso_kg
  @property
  def peso_kg(self) -> float:
    return self._peso_kg
  @peso_kg.setter
  def peso_kg(self, valor: float) -> None:
    if valor <= 0:
      raise ValueError("El peso del producto debe ser mayor a 0 kg")
    self._peso_kg = valor

  def calcular_costo_envio(self) -> float:
    return self._peso_kg * 500
  def __repr__(self) -> str:
    return f"ProductoFisico(nombre='{self.nombre}',precio=${self.precio},peso={self.peso_kg} kg)"

class Cliente:
  _nombre: str
  _email: str
  def __init__(self, nombre: str, email: str):
    self.nombre = nombre
    self.email = email
  @property
  def nombre(self) -> str:
    return self._nombre
  @nombre.setter
  def nombre(self, valor: str) -> None:
    if not valor or len(valor.strip()) < 3:
      raise ValueError("El nombre del cliente debe tener al menos 3 caracteres")
    self._nombre = valor
  @property
  def email(self) -> str:
    return self._email
  @email.setter
  def email(self, valor: str) -> None:
    if "@" not in valor or "." not in valor:
      raise ValueError("El email proporcionado no tiene un formato válido")
    self._email = valor.lower().strip()
  def __repr__(self) -> str:
    return f"Cliente(nombre='{self.nombre}',email='{self.email}')"

class Orden:
  _cliente: Cliente
  _productos: list[Producto]
  def __init__(self, cliente: Cliente):
    self.cliente = cliente
    self._productos = []
  @property
  def cliente(self) -> Cliente:
    return self._cliente
  @cliente.setter
  def cliente(self, valor: Cliente) -> None:
    if not isinstance(valor, Cliente):
      raise ValueError("El titular de la orden debe ser una instancia de Cliente")
    self._cliente = valor

  @property
  def productos(self) -> list[Producto]:
    return list(self._productos)
  def agregar_producto(self, producto: Producto) -> None:
    if not isinstance(producto, Producto):
      raise ValueError("Solo se pueden agregar objetos de tipo Producto a la orden")
    self._productos.append(producto)

  def calcular_total(self) -> float:
    total_productos = sum(p.precio for p in self._productos)
    total_envio = sum(p.calcular_costo_envio() for p in self._productos if isinstance(p, ProductoFisico))
    return total_productos + total_envio
  def __repr__(self) -> str:
    return f"Orden(cliente='{self.cliente.nombre}',cantidad_items={len(self._productos)},total=${self.calcular_total()})"
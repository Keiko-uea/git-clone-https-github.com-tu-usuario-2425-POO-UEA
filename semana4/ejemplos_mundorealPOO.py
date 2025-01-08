# Clase que representa un producto en la tienda
class Producto:
    def __init__(self, nombre, precio, talla):
        self.nombre = nombre  # Nombre del producto
        self.precio = precio  # Precio del producto
        self.talla = talla  # Talla del producto

    def mostrar_info(self):
        """Muestra la información del producto."""
        return f"Producto: {self.nombre}, Precio: ${self.precio}, Talla: {self.talla}"

# Clase que representa un cliente
class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre  # Nombre del cliente
        self.pedido_actual = []  # Lista para almacenar productos en el pedido

    def agregar_producto(self, producto):
        """Agrega un producto al pedido actual."""
        self.pedido_actual.append(producto)

    def mostrar_pedido(self):
        """Muestra los productos en el pedido actual."""
        return [producto.mostrar_info() for producto in self.pedido_actual]

# Clase que representa un pedido
class Pedido:
    def __init__(self, cliente):
        self.cliente = cliente  # Cliente que realiza el pedido
        self.total = 0  # Total del pedido

    def calcular_total(self):
        """Calcula el total del pedido."""
        self.total = sum(producto.precio for producto in self.cliente.pedido_actual)
        return self.total

# Ejemplo de uso
if __name__ == "__main__":
    # Crear productos
    camiseta = Producto("Camiseta Infantil", 15.99, "XS")
    pantalon = Producto("Pantalón Infantil", 25.50, "S")

    # Crear cliente
    cliente1 = Cliente("ALEJANDRO GONZALEZ")

    # Agregar productos al pedido del cliente
    cliente1.agregar_producto(camiseta)
    cliente1.agregar_producto(pantalon)

    # Mostrar pedido
    print(f"Pedido de {cliente1.nombre}:")
    for info in cliente1.mostrar_pedido():
        print(info)

    # Crear y calcular el total del pedido
    pedido1 = Pedido(cliente1)
    total_pedido = pedido1.calcular_total()
    print(f"Total del pedido: ${total_pedido:.2f}")

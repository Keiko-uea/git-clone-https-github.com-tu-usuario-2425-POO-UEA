class Producto:
    """
    Representa un producto en el inventario.
    """

    def __init__(self, id_producto, nombre, cantidad, precio):
        """
        Inicializa un nuevo producto.

        Args:
            id_producto (int): Identificador único del producto.
            nombre (str): Nombre del producto.
            cantidad (int): Cantidad disponible en el inventario.
            precio (float): Precio unitario del producto.
        """
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # Getters
    def get_id(self):
        return self.id_producto

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    # Setters
    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"

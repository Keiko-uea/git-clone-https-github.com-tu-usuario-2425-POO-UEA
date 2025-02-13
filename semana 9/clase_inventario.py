class Inventario:
    """
    Gestiona la lista de productos en el inventario.
    """

    def __init__(self):
        """
        Inicializa un inventario vacío.
        """
        self.productos = []

    def agregar_producto(self, producto):
        """
        Agrega un nuevo producto al inventario, verificando que el ID sea único.

        Args:
            producto (Producto): El producto a agregar.

        Returns:
            bool: True si el producto se agregó correctamente, False si el ID ya existe.
        """
        if any(p.get_id() == producto.get_id() for p in self.productos):
            print("Error: Ya existe un producto con este ID.")
            return False
        self.productos.append(producto)
        return True

    def eliminar_producto(self, id_producto):
        """
        Elimina un producto del inventario por su ID.

        Args:
            id_producto (int): El ID del producto a eliminar.

        Returns:
            bool: True si el producto se eliminó correctamente, False si no se encontró.
        """
        for i, producto in enumerate(self.productos):
            if producto.get_id() == id_producto:
                del self.productos[i]
                return True
        print("Error: No se encontró ningún producto con este ID.")
        return False

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        """
        Actualiza la cantidad y/o el precio de un producto por su ID.

        Args:
            id_producto (int): El ID del producto a actualizar.
            cantidad (int, optional): La nueva cantidad (si se va a actualizar).
            precio (float, optional): El nuevo precio (si se va a actualizar).

        Returns:
            bool: True si el producto se actualizó correctamente, False si no se encontró.
        """
        for producto in self.productos:
            if producto.get_id() == id_producto:
                if cantidad is not None:
                    producto.set_cantidad(cantidad)
                if precio is not None:
                    producto.set_precio(precio)
                return True
        print("Error: No se encontró ningún producto con este ID.")
        return False

    def buscar_producto(self, nombre):
        """
        Busca productos por nombre (puede haber nombres similares).

        Args:
            nombre (str): El nombre o parte del nombre a buscar.

        Returns:
            list[Producto]: Una lista de productos que coinciden con la búsqueda.
        """
        resultados = [producto for producto in self.productos if nombre.lower() in producto.get_nombre().lower()]
        return resultados

    def mostrar_inventario(self):
        """
        Muestra todos los productos en el inventario.
        """
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for producto in self.productos:
                print(producto)

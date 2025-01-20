class Producto:
    def __init__(self, nombre, precio):
        self.__nombre = nombre  # Atributo privado
        self.__precio = precio  # Atributo privado

    def obtener_nombre(self):
        return self.__nombre

    def obtener_precio(self):
        return self.__precio

    def mostrar_info(self):
        return f"Producto: {self.__nombre}, Precio: {self.__precio}"

class ProductoPerecedero(Producto):
    def __init__(self, nombre, precio, fecha_expiracion):
        super().__init__(nombre, precio)  # Llamada al constructor de la clase base
        self.fecha_expiracion = fecha_expiracion

    def mostrar_info(self):
        return f"{super().mostrar_info()}, Fecha de Expiración: {self.fecha_expiracion}"

class ProductoElectronico(Producto):
    def __init__(self, nombre, precio, garantia):
        super().__init__(nombre, precio)
        self.garantia = garantia

    def mostrar_info(self):
        return f"{super().mostrar_info()}, Garantía: {self.garantia} años"

# Creación de instancias
producto1 = ProductoPerecedero("Leche", 1.50, "2025-01-30")
producto2 = ProductoElectronico("Televisor", 300.00, 2)

# Uso de los métodos
print(producto1.mostrar_info())
print(producto2.mostrar_info())

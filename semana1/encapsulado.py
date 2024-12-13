class Producto:
    def __init__(self, nombre, precio, cantidad):
        self._nombre = nombre          # Atributo privado
        self._precio = precio          # Atributo privado
        self._cantidad = cantidad      # Atributo privado

    def establecer_precio(self, precio):
        if precio >= 0:
            self._precio = precio
        else:
            print("El precio no puede ser negativo.")

    def obtener_precio(self):
        return self._precio

    def establecer_cantidad(self, cantidad):
        if cantidad >= 0:
            self._cantidad = cantidad
        else:
            print("La cantidad no puede ser negativa.")

    def obtener_cantidad(self):
        return self._cantidad

    def vender(self, cantidad):
        if 0 < cantidad <= self._cantidad:
            self._cantidad -= cantidad
            print(f"Se han vendido {cantidad} de {self._nombre}.")
        else:
            print("Cantidad no válida o insuficiente.")

# Creación de una instancia de Producto
producto1 = Producto("Leche", 1.50, 100)

# Uso de los métodos
print(f"Nombre: {producto1._nombre}, Precio: {producto1.obtener_precio()}, Cantidad: {producto1.obtener_cantidad()}")
# Salida: Nombre: Leche, Precio: 1.5, Cantidad: 100

producto1.vender(10)  # Salida: Se han vendido 10 de Leche.
print(f"Nueva cantidad de {producto1._nombre}: {producto1.obtener_cantidad()}")  # Salida: Nueva cantidad de Leche: 90

producto1.establecer_precio(2.00)
print(f"Nuevo precio de {producto1._nombre}: {producto1.obtener_precio()}")  # Salida: Nuevo precio de Leche: 2.0

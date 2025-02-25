class Producto:
    def __init__(self, producto_id, nombre, cantidad, precio):
        self.id = producto_id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

class Inventario:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, producto):
        self.productos[producto.id] = producto

    def eliminar_producto(self, id):
        if id in self.productos:
            del self.productos[id]

    def actualizar_producto(self, id, cantidad=None, precio=None):
        if id in self.productos:
            if cantidad is not None:
                self.productos[id].cantidad = cantidad
            if precio is not None:
                self.productos[id].precio = precio

    def buscar_producto(self, nombre):
        resultados = []
        for producto in self.productos.values():
            if producto.nombre.lower() == nombre.lower():
                resultados.append({
                    "nombre": producto.nombre,
                    "cantidad": producto.cantidad,
                    "precio": producto.precio
                })
        return resultados

    def mostrar_productos(self):
        for producto in self.productos.values():
            print(f"ID: {producto.id}, Nombre: {producto.nombre}, Cantidad: {producto.cantidad}, Precio: {producto.precio}")

    def guardar_inventario(self):
        # Aquí iría la lógica para guardar el inventario en un archivo
        pass

    def cargar_inventario(self):
        # Aquí iría la lógica para cargar el inventario desde un archivo
        pass

def main():
    inventario = Inventario()

    while True:
        print("\nMenú de Gestión de Inventario:")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto")
        print("5. Mostrar todos los productos")
        print("6. Guardar inventario")
        print("7. Cargar inventario")
        print("8. Salir")

        opcion = input("Ingrese su opción: ")

        if opcion == "1":
            producto_id = input("Ingrese el ID del producto: ")
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad del producto: "))
            precio = float(input("Ingrese el precio del producto: "))
            producto = Producto(producto_id, nombre, cantidad, precio)
            inventario.agregar_producto(producto)
        elif opcion == "2":
            producto_id = input("Ingrese el ID del producto a eliminar: ")
            inventario.eliminar_producto(producto_id)
        elif opcion == "3":
            producto_id = input("Ingrese el ID del producto a actualizar: ")
            cantidad = input("Ingrese la nueva cantidad (dejar vacío para no cambiar): ")
            precio = input("Ingrese el nuevo precio (dejar vacío para no cambiar): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(producto_id, cantidad, precio)
        elif opcion == "4":
            nombre = input("Ingrese el nombre del producto a buscar: ")
            resultados = inventario.buscar_producto(nombre)
            if resultados:
                for resultado in resultados:
                    print(f"Nombre: {resultado['nombre']}, Cantidad: {resultado['cantidad']}, Precio: {resultado['precio']}")
            else:
                print("No se encontraron productos con ese nombre.")
        elif opcion == "5":
            inventario.mostrar_productos()
        elif opcion == "6":
            inventario.guardar_inventario()
            print("Inventario guardado correctamente.")
        elif opcion == "7":
            inventario.cargar_inventario()
            print("Inventario cargado correctamente.")
        elif opcion == "8":
            break
        else:
            print("Opción inválida. Por favor, intente nuevamente.")

if __name__ == "__main__":
    main()

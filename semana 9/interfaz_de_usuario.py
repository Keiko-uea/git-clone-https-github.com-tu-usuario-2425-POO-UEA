from inventario import Inventario
from producto import Producto

def main():
    """
    Función principal que ejecuta la interfaz de usuario en la consola.
    """
    inventario = Inventario()

    while True:
        print("\n--- Menú de Inventario ---")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto")
        print("5. Mostrar inventario")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            try:
                id_producto = int(input("ID del producto: "))
                nombre = input("Nombre del producto: ")
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))
                producto = Producto(id_producto, nombre, cantidad, precio)
                if inventario.agregar_producto(producto):
                    print("Producto agregado correctamente.")
            except ValueError:
                print("Error: Ingrese valores válidos para ID, cantidad y precio.")

        elif opcion == '2':
            try:
                id_producto = int(input("ID del producto a eliminar: "))
                if inventario.eliminar_producto(id_producto):
                    print("Producto eliminado correctamente.")
            except ValueError:
                print("Error: Ingrese un ID válido.")

        elif opcion == '3':
            try:
                id_producto = int(input("ID del producto a actualizar: "))
                cantidad = input("Nueva cantidad (dejar en blanco para no cambiar): ")
                precio = input("Nuevo precio (dejar en blanco para no cambiar): ")

                cantidad = int(cantidad) if cantidad else None
                precio = float(precio) if precio else None

                if cantidad is None and precio is None:
                    print("Error: Debe ingresar una nueva cantidad o precio para actualizar.")
                else:
                    if inventario.actualizar_producto(id_producto, cantidad, precio):
                        print("Producto actualizado correctamente.")
            except ValueError:
                print("Error: Ingrese valores válidos para cantidad y precio.")

        elif opcion == '4':
            nombre = input("Nombre del producto a buscar: ")
            resultados = inventario.buscar_producto(nombre)
            if resultados:
                print("Resultados de la búsqueda:")
                for producto in resultados:
                    print(producto)
            else:
                print("No se encontraron productos con ese nombre.")

        elif opcion == '5':
            inventario.mostrar_inventario()

        elif opcion == '6':
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()

import os

def mostrar_codigo(ruta_script):
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r') as archivo:
            print(f"\n--- Código de {ruta_script} ---\n")
            print(archivo.read())
    except FileNotFoundError:
        print("El archivo no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")

def mostrar_menu():
    ruta_base = os.path.dirname(__file__)

    opciones = {
        '1': ['semana1/abstracto.py', 'semana1/encapsulado.py', 'semana1/herencia.py', 'semana1/polimorfismo.py'],
        '3': ['semana3/P tradicional.py', 'semana3/POO.py'],
        '4': ['semana4/ejemplo_mundorealPOO.py'],
        '5': ['semana5/tipos_de_datos_identificadores.py'],
        '6': ['semana6/aplicacion_de_conceptos_POO.py'],
        '7': ['semana7/implementacion_constructores_destructores.py'],
        # Agrega aquí el resto de las rutas de los scripts
    }

    while True:
        print("\n********Menu Principal - Dashboard*************")
        for key in opciones:
            print(f"{key} - {', '.join(opciones[key])}")
        print("0 - Salir")

        eleccion = input("Elige un script para ver su código o '0' para salir: ")
        if eleccion == '0':
            break
        elif eleccion in opciones:
            for script in opciones[eleccion]:
                ruta_script = os.path.join(ruta_base, script)
                mostrar_codigo(ruta_script)
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

if __name__ == "__main__":
    mostrar_menu()

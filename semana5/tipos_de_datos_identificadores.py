# Este programa gestiona las citas de los pacientes en una clínica veterinaria.
# Permite agregar una nueva cita, mostrar la lista de citas y verificar si una cita está programada.

def agregar_cita(citas):
    """
    Esta función solicita al usuario que ingrese los detalles de una nueva cita
    y la agrega a la lista de citas.
    """
    nombre_dueño = input("Ingrese el nombre del dueño: ")  # String
    nombre_mascota = input("Ingrese el nombre de la mascota: ")  # String
    fecha_cita = input("Ingrese la fecha de la cita (DD/MM/AAAA): ")  # String
    hora_cita = input("Ingrese la hora de la cita (HH:MM): ")  # String
    motivo = input("Ingrese el motivo de la cita: ")  # String

    # Crear un diccionario con la información de la cita
    cita = {
        'nombre_dueño': nombre_dueño,
        'nombre_mascota': nombre_mascota,
        'fecha_cita': fecha_cita,
        'hora_cita': hora_cita,
        'motivo': motivo
    }

    citas.append(cita)  # Agregar la cita a la lista

def mostrar_citas(citas):
    """
    Esta función muestra todas las citas programadas.
    """
    if not citas:
        print("\nNo hay citas programadas.")
        return

    print("\n--- Lista de Citas ---")
    for i, cita in enumerate(citas, start=1):
        print(f"Cita {i}:")
        print(f"  Dueño: {cita['nombre_dueño']}")
        print(f"  Mascota: {cita['nombre_mascota']}")
        print(f"  Fecha: {cita['fecha_cita']}")
        print(f"  Hora: {cita['hora_cita']}")
        print(f"  Motivo: {cita['motivo']}\n")

def verificar_cita(citas):
    """
    Esta función verifica si hay una cita programada para una mascota específica.
    """
    nombre_mascota = input("Ingrese el nombre de la mascota para verificar su cita: ")  # String
    for cita in citas:
        if cita['nombre_mascota'].lower() == nombre_mascota.lower():
            print("\n--- Cita Encontrada ---")
            print(f"Dueño: {cita['nombre_dueño']}")
            print(f"Fecha: {cita['fecha_cita']}")
            print(f"Hora: {cita['hora_cita']}")
            print(f"Motivo: {cita['motivo']}\n")
            return

    print("\nNo se encontró ninguna cita para esa mascota.")

# Programa principal
if __name__ == "__main__":
    citas_programadas = []  # Lista para almacenar las citas

    while True:
        print("Bienvenido al sistema de gestión de citas veterinarias.")
        print("1. Agregar nueva cita")
        print("2. Mostrar todas las citas")
        print("3. Verificar cita por mascota")
        print("4. Salir")

        opcion = input("Seleccione una opción (1-4): ")

        if opcion == '1':
            agregar_cita(citas_programadas)
        elif opcion == '2':
            mostrar_citas(citas_programadas)
        elif opcion == '3':
            verificar_cita(citas_programadas)
        elif opcion == '4':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, intente nuevamente.")

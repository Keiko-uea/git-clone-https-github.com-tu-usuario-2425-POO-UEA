# Función para ingresar las temperaturas diarias
def ingresar_temperaturas():
    temperaturas = []  # Lista para almacenar las temperaturas
    for i in range(7):  # Ciclo para 7 días
        # Solicitar al usuario que ingrese la temperatura
        temp = float(input(f"Ingrese la temperatura del día {i + 1}: "))
        temperaturas.append(temp)  # Agregar la temperatura a la lista
    return temperaturas  # Retornar la lista de temperaturas

# Función para calcular el promedio de las temperaturas
def calcular_promedio(temperaturas):
    return sum(temperaturas) / len(temperaturas)  # Calcular y retornar el promedio

# Función principal que organiza la ejecución del programa
def main():
    print("Ingreso de Temperaturas Semanales")  # Mensaje inicial
    temperaturas = ingresar_temperaturas()  # Llamar a la función para ingresar temperaturas
    promedio = calcular_promedio(temperaturas)  # Calcular el promedio
    print(f"El promedio semanal de temperaturas es: {promedio:.2f} °C")  # Mostrar el resultado

if __name__ == "__main__":
    main()  # Ejecutar la función principal al correr el script
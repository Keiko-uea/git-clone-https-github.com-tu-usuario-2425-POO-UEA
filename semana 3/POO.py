class ClimaDiario:
    def __init__(self):
        self.temperaturas = []  # Inicializar una lista vacía para las temperaturas del día

    def ingresar_temperatura(self, temp):
        """Método para ingresar una temperatura diaria."""
        self.temperaturas.append(temp)  # Agregar la temperatura a la lista

    def calcular_promedio(self):
        """Método para calcular el promedio de las temperaturas."""
        if not self.temperaturas:  # Verificar si hay temperaturas ingresadas
            return 0  # Retornar 0 si no hay datos
        return sum(self.temperaturas) / len(self.temperaturas)  # Calcular y retornar el promedio


class ClimaSemanal:
    def __init__(self):
        self.dias = []  # Inicializar una lista vacía para almacenar los días

    def agregar_dia(self, clima_diario):
        """Método para agregar un objeto ClimaDiario a la lista de días."""
        self.dias.append(clima_diario)  # Agregar el objeto ClimaDiario a la lista

    def calcular_promedio_semanal(self):
        """Método para calcular el promedio semanal de todas las temperaturas."""
        total_temperaturas = []  # Lista para almacenar todas las temperaturas de la semana
        for dia in self.dias:  # Recorrer cada día en la lista
            total_temperaturas.extend(dia.temperaturas)  # Agregar las temperaturas del día a la lista total
        if not total_temperaturas:  # Verificar si hay temperaturas ingresadas
            return 0  # Retornar 0 si no hay datos
        return sum(total_temperaturas) / len(total_temperaturas)  # Calcular y retornar el promedio semanal


# Función principal que organiza la ejecución del programa
def main():
    clima_semanal = ClimaSemanal()  # Crear un objeto ClimaSemanal

    print("Ingreso de Temperaturas Semanales")  # Mensaje inicial

    for i in range(7):  # Ciclo para ingresar datos durante una semana
        clima_diario = ClimaDiario()  # Crear un nuevo objeto ClimaDiario
        temp = float(input(f"Ingrese la temperatura del día {i + 1}: "))  # Solicitar temperatura al usuario
        clima_diario.ingresar_temperatura(temp)  # Ingresar la temperatura en el objeto ClimaDiario
        clima_semanal.agregar_dia(clima_diario)  # Agregar el objeto ClimaDiario a ClimaSemanal

    promedio_semanal = clima_semanal.calcular_promedio_semanal()  # Calcular el promedio semanal
    print(f"El promedio semanal de temperaturas es: {promedio_semanal:.2f} °C")  # Mostrar el resultado


if __name__ == "__main__":
    main()  # Ejecutar la función principal al correr el script


# Clase base
class Vehiculo:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

    def info(self):
        return f"Vehículo: {self.marca} {self.modelo}, Año: {self.año}"

# Clase derivada: Coche
class Coche(Vehiculo):
    def __init__(self, marca, modelo, año, consumo):
        super().__init__(marca, modelo, año)
        self.consumo = consumo  # Consumo en litros cada 100 km

    def calcular_consumo(self, distancia):
        # Calcula el combustible necesario para una distancia dada
        return (distancia / 100) * self.consumo

# Clase derivada: Bicicleta
class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, año, tiene_cambios):
        super().__init__(marca, modelo, año)
        self.tiene_cambios = tiene_cambios

    def info(self):
        base_info = super().info()
        cambios_info = "Con cambios" if self.tiene_cambios else "Sin cambios"
        return f"{base_info}. {cambios_info}"

# Creación de instancias
coche1 = Coche("Toyota", "Corolla", 2020, 6.5)
bicicleta1 = Bicicleta("Giant", "Escape", 2022, True)

# Uso de los métodos
print(coche1.info())  # Salida: Vehículo: Toyota Corolla, Año: 2020
print(f"Consumo para 150 km: {coche1.calcular_consumo(150)} litros")  # Salida: Consumo para 150 km: 9.75 litros

print(bicicleta1.info())  # Salida: Vehículo: Giant Escape, Año: 2022. Con cambios


from abc import ABC, abstractmethod


# Clase abstracta
class Figura(ABC):
    @abstractmethod
    def calcular_area(self):
        pass


# Clase concreta que implementa la abstracción
class Cuadrado(Figura):
    def _init_(self, lado):
        self.lado = lado

    def calcular_area(self):
        return self.lado ** 2


class Circulo(Figura):
    def _init_(self, radio):
        self.radio = radio

    def calcular_area(self):
        return 3.1416 * (self.radio ** 2)


# Uso
figuras = [Cuadrado(4), Circulo(3)]
for figura in figuras:
    print(f"Área: {figura.calcular_area()}")
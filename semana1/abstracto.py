from abc import ABC, abstractmethod

# Clase abstracta
class Planta(ABC):
    @abstractmethod
    def nombre(self):
        pass

    @abstractmethod
    def tipo(self):
        pass

    @abstractmethod
    def fotosintesis(self):
        pass

# Clase derivada: Arbol
class Arbol(Planta):
    def __init__(self, nombre_arbol):
        self._nombre = nombre_arbol

    def nombre(self):
        return self._nombre

    def tipo(self):
        return "Árbol"

    def fotosintesis(self):
        return f"{self._nombre} realiza la fotosíntesis utilizando sus hojas grandes y verdes."

# Clase derivada: Flor
class Flor(Planta):
    def __init__(self, nombre_flor):
        self._nombre = nombre_flor

    def nombre(self):
        return self._nombre

    def tipo(self):
        return "Flor"

    def fotosintesis(self):
        return f"{self._nombre} realiza la fotosíntesis a través de sus pétalos coloridos."

# Creación de instancias
arbol1 = Arbol("Roble")
flor1 = Flor("Rosa")

# Uso de los métodos
print(f"Nombre: {arbol1.nombre()}, Tipo: {arbol1.tipo()}, {arbol1.fotosintesis()}")
# Salida: Nombre: Roble, Tipo: Árbol, Roble realiza la fotosíntesis utilizando sus hojas grandes y verdes.

print(f"Nombre: {flor1.nombre()}, Tipo: {flor1.tipo()}, {flor1.fotosintesis()}")
# Salida: Nombre: Rosa, Tipo: Flor, Rosa realiza la fotosíntesis a través de sus pétalos coloridos.

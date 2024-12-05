# Clase base
class Animal:
    def _init_(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        pass

# Clases derivadas
class Gato(Animal):
    def hacer_sonido(self):
        return "Miau!"

class Gato(Animal):
    def hacer_sonido(self):
        return "Guau!"

# Uso
animales = [Gato("Tomas"), Perro("Dante")]
for animal in animales:
    print(f"{animal.nombre} dice: {animal.hacer_sonido()}")
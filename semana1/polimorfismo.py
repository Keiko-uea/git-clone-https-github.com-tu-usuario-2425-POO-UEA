class Vehiculo:
    def mover(self):
        pass

class Camion(Vehiculo):
    def mover(self):
        return "El camion está conduciendo."

class Avion(Vehiculo):
    def mover(self):
        return "El avion está volando."

# Uso
vehiculos = [Camion(), Avion()]
for vehiculo in vehiculos:
    print(vehiculo.mover())
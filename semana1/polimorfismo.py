class Vehiculo:
    def mover(self):
        raise NotImplementedError("Este método debe ser implementado por subclases")
class Coche(Vehiculo):
    def mover(self):
        return "El coche se mueve por la carretera."

class Bicicleta(Vehiculo):
    def mover(self):
        return "La bicicleta se mueve pedaleando."
def main():
    vehiculos = [Coche(), Bicicleta()]

    for vehiculo in vehiculos:
        print(vehiculo.mover())

if __name__ == "__main__":
    main()


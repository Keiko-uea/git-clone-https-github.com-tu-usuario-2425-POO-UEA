class CuentaBancaria:
    def _init_(self, titular, saldo):
        self.titular = titular  # Público
        self.__saldo = saldo    # Privado

    # Métodos para acceder al saldo
    def depositar(self, monto):
        self.__saldo += monto
        print(f"Se han depositado ${monto}. Saldo actual: ${self.__saldo}")

    def retirar(self, monto):
        if monto <= self.__saldo:
            self.__saldo -= monto
            print(f"Se han retirado ${monto}. Saldo actual: ${self.__saldo}")
        else:
            print("Fondos insuficientes")

# Uso
cuenta = CuentaBancaria("Juan", 2000)
cuenta.depositar(100)
cuenta.retirar(400)
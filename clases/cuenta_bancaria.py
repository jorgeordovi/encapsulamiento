class CuentaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.__titular = titular # Usando __ dos guiones bajos hacemos privado el atributo
        self.__saldo = saldo_inicial

    #setter de (editor, conofiguracion)
    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            print(f"Deposito de ${cantidad} exitoso")
        else:
            print("Error. no se puede depositar un saldo negativo")

    def retirar(self, cantidad):
        if 0 < cantidad <= self.__saldo:
            self.__saldo -= cantidad
            print(f"Se ha retirado ${cantidad} exitosamente")
        else:
            print("Fondos insuficientes o cantidad invalida")

#getter (obtener informacion provada ateravez de un metodo puvblico)

    def obtener_saldo(self):
        return f"El saldo actual de la cuenta es {self.__saldo}"
    
    
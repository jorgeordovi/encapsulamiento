from clases.cuenta_bancaria import CuentaBancaria


# instancia 
cuenta = CuentaBancaria("Jorge Codes", 1000)

#intentar acceder a datos privados

cuenta.__titular = "Ricardito"
cuenta.__saldo = 10000000000

cuenta.depositar(500)
print(cuenta.obtener_saldo())


cuenta.retirar(1500)
print(cuenta.obtener_saldo())
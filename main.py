from banco import Banco
from cliente import Cliente
from conta import ContaCorrente, ContaPoupanca

banco = Banco()

cliente1 = Cliente('Luis', 30)
cliente2 = Cliente('Maria', 18)
cliente3 = Cliente('Carlos', 35)

conta1 = ContaPoupanca(1111, 78356, 0)
conta1 = ContaPoupanca(2222, 78357, 0)
conta1 = ContaPoupanca(2222, 78358, 0)

cliente1.inserir_conta(conta1)
cliente2.inserir_conta(conta2)
cliente3.inserir_conta(conta3)

cliente1.conta.depositar(40)
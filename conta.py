from abc import ABC, abstractmethod

class Conta:
    def __int__(self, agencia, conta, saldo):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        self.detalhes()

    def detalhes(self):
        print(f'Agência:{self.agencia} '
              f'Conta: {self.conta} '
              f'saldo: {self.saldo}')

    @abstractmethod
    def sacar(self, valor): pass

class ContaPoupanca(Conta):
    def sacar(self, valor):
        if self.saldo < valor:
            print('Saldo insuficiente')
            return
        self.saldo -= valor
        self.detalhes()

class ContaCorrente(Conta):
    def __int__(self, agencia, conta, saldo, limite=100):
        super().__int__(agencia, conta, saldo)
        self.limite = limite

    def sacar(self, valor):
        if (self.saldo +self.limite) < valor:
            print('Saldo insuficiente')

        self.saldo -= valor
        self.detalhes()

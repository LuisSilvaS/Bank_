
class Pessoa:
    def __int__(self, nome, idade):
        self._nome = nome
        self.idade = idade

    @property
    def nome(self):
        return self._nome

    @property
    def idade(self):
        return self._idade

class Cliente(Pessoa):
    def __int__(self, nome, idade):
        super().__int__(nome, idade)
        self.conta = None

    def inserir_conta(self, conta):
        self.conta = conta


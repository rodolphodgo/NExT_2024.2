"""Enunciado:
Crie uma classe ContaBancaria que tenha os atributos titular (str), saldo (float) e os métodos depositar(valor), sacar(valor) e exibir_saldo()."""

"""Requisitos:
- O método depositar deve aumentar o saldo pelo valor informado.
- O método sacar deve diminuir o saldo pelo valor informado, apenas se houver saldo suficiente. Caso contrário, exiba uma mensagem de saldo insuficiente.
- O método exibir_saldo deve imprimir o saldo atual da conta."""

class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo = self.saldo + valor

    def sacar(self, valor):
        if (self.saldo >= valor):
            self.saldo = self.saldo - valor
        else:
            print("O valor não pode ser sacado")

    def exibir_saldo(self):
        print(self.saldo)

conta123 = ContaBancaria("Julia", 2000.0)
conta123.exibir_saldo()
conta123.depositar(100)
conta123.exibir_saldo()
conta123.sacar(2200)
conta123.exibir_saldo()

conta456 = ContaBancaria("Roberto", 30000.0)
conta456.exibir_saldo()
conta456.depositar(7000)
conta456.exibir_saldo()
conta456.sacar(3000)
conta456.exibir_saldo()
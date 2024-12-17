"""Crie uma classe Produto que possui nome, preco e estoque.

Implemente um método adicionar_estoque(quantidade) que adiciona ao estoque a quantidade fornecida.
Implemente outro método remover_estoque(quantidade) que só remove se houver estoque suficiente; caso contrário, exiba uma mensagem informando que não há estoque suficiente.
Crie um método exibir_produto() que mostra as informações do produto (nome, preço e estoque)."""

class Produto:
    def __init__(self, nome,preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    def adcionar_estoque(self, quantidade):
        self.estoque = self.estoque + quantidade

    def remover_estoque(self, quantidade):
        if (self.estoque >= quantidade):
            self.estoque = self.estoque - quantidade
        else:
            print("A quantidade para remover e superior a que tem no estoque")

    def exibir_produto(self):
        print(f"O {self.nome} custa {self.preco} reais e tem {self.estoque} no estoque")

produto1 = Produto("Amaciante", 15.5, 100)
produto1.exibir_produto()
produto1.adcionar_estoque(50)
produto1.exibir_produto()
produto1.remover_estoque(99)
produto1.exibir_produto()
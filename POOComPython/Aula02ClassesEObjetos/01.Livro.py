"""Enunciado:
Crie uma classe Livro com atributos titulo e autor e um método exibir_informacoes() que imprime o título e o autor."""

"""Requisitos:
- Crie três objetos dessa classe, cada um representando um livro diferente, e chame o método exibir_informacoes() para cada um."""

class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def exibir_inormacoes(self):
        print(f"O livro {self.titulo} tem como autor {self.autor}")

peixeGrande = Livro("Peixe Grande", "Daniel Walace")
robisonCrusoe = Livro("Robinson Crusoé", "Daniel Defoe")
principe = Livro("O Príncipe", "Nicolau Maqueavel")

peixeGrande.exibir_inormacoes()
robisonCrusoe.exibir_inormacoes()
principe.exibir_inormacoes()
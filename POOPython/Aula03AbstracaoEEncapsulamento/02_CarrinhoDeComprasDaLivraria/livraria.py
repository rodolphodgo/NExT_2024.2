class Livro:
    def __init__(self, titulo, autor, preco):
        self.titulo = titulo
        self.autor = autor
        self.preco = preco

    def exibir_detalhes(self):
        return f"Título: {self.titulo}, Autor: {self.autor}, Preço: {self.preco:.2f}"


class CarrinhoDeCompras:
    def __init__(self):
        self.lista_livros = []

    def adcionar_livro(self, livro):
        self.lista_livros.append(livro)

    def remover_livro(self, titulo):
        for i in range(len(self.lista_livros)):
            if self.lista_livros[i].titulo == titulo:
                self.lista_livros.pop(i)

    def calcular_total(self):
        total = 0
        for i in self.lista_livros:
            total = total + i.preco
        print(total)

    def exibir_itens(self):
        for i in self.lista_livros:
            print(i.exibir_detalhes())


if __name__ == "__main__":
    livro1 = Livro("titulo", "autor", 30)
    livro2 = Livro("titulo", "autor", 330)
    carrinho = CarrinhoDeCompras()
    carrinho.adcionar_livro(livro1)
    carrinho.calcular_total()
    carrinho.adcionar_livro(livro2)
    carrinho.calcular_total()
    carrinho.exibir_itens()


from livraria import Livro, CarrinhoDeCompras

livro1 = Livro("Robison Crusoè", "Daniel Defoe", 45.5)
livro2 = Livro("Peixe Grande", "Daniel Wallace", 27)
livro3 = Livro("O Corvo", "Edgar Allan Poe", 57.9)

carrinho = CarrinhoDeCompras()

carrinho.adcionar_livro(livro1)
carrinho.adcionar_livro(livro2)
carrinho.adcionar_livro(livro3)

carrinho.calcular_total()

carrinho.exibir_itens()
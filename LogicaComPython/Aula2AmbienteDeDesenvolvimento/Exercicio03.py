'''Dada a lista original de nomes do exercício 1, crie uma nova lista que contenha apenas os nomes com mais de 5 caracteres.'''

nomes = ["Ana", "Bruno", "Carlos", "Daniela", "Eduardo", "Fernanda", "Gustavo"]

nomes_maiorque5 = []

nomes_maiorque5 = [nome for nome in nomes if len(nome) > 5]

print(nomes_maiorque5)
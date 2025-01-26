'''Produto de uma lista de números

Utilize a função reduce para calcular o produto (multiplicação) de todos os números na lista numeros = [1, 2, 3, 4, 5].'''

from functools import reduce

numeros = [1, 2, 3, 4, 5]

multiplicador = reduce(lambda a, b: a * b, numeros)

print(multiplicador)
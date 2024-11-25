from functools import reduce

numeros = [1, 2, 3, 4, 5]

produto = reduce(lambda a, b: a * b, numeros)

print(produto)
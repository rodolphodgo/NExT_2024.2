from functools import reduce

numeros = [1, 2, 3, 4]

quadrado = list(map(lambda n: n ** 2, numeros))
soma = reduce(lambda x, y: x + y, quadrado)

print(soma)
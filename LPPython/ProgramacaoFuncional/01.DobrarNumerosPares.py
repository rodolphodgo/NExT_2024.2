numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

pares = list(filter(lambda x: x % 2 == 0, numeros))
dobro = list(map(lambda a: a * 2, pares))

print(dobro)
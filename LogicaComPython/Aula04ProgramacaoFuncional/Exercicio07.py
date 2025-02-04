"""Maior palavra em uma lista

Utilize reduce para encontrar a palavra mais longa na lista palavras = ["sol", "montanha", "mar", "universo"]."""

from functools import reduce

lista = ["sol", "montanha", "mar", "universo"]

maior_palavra = reduce(lambda x, y: x if len(x) > len(y) else y, lista)
print(maior_palavra)






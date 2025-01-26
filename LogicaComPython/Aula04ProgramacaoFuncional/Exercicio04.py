'''Listar os comprimentos das palavras

Dada a lista palavras = ["maçã", "banana", "cereja", "damasco"], use map para criar uma lista com os comprimentos de cada palavra.'''

palavras = ["maçã", "banana", "cereja", "damasco"]

comprimento = list(map(lambda p: len(p), palavras))

print(comprimento)
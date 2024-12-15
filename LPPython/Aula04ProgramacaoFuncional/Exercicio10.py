'''Contar ocorrências de uma letra

Dada a lista palavras = ["banana", "abacate", "morango", "abacaxi"], use map para contar quantas vezes a letra "a" aparece em cada palavra, resultando em uma lista de contagens.'''

palavras = ["banana", "abacate", "morango", "abacaxi"]

letra_a = list(map(lambda a: a.count("a"), palavras))

print(letra_a)
print(sum(letra_a))
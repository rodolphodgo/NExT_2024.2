"""Receba do usuário 4 notas de uma única vez, em uma única linha.
Exiba a média dessas notas e se o estudante foi aprovado ou não (nota maior ou igual a 7).

Exemplo de entrada: 10.0 8.0 4.5 3.0"""

notas = input()
lista  = notas.split(' ')
nota1 = float(lista[0])
nota2 = float(lista[1])
nota3 = float(lista[2])
nota4 = float(lista[3])

media = (nota1 + nota2 + nota3 + nota4) / 4

print(media)
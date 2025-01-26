'''Use o módulo random para criar um jogo onde o programa escolhe um número aleatório entre 0 e 10 e o usuário deve tentar adivinhar o valor. Quando a pessoa acertar, deve ser apresentado uma pontuação (se acertar de primeira, 10 pontos, na segunda tentativa, 9 pontos...)'''

import random

numero = random.randint(1,10)


for x in range(10):
    tentativa = int(input(f"Tentativa {x + 1}: "))
    if tentativa == numero:
        print(f"Acertou! Pontuação: {10 - x}")
        break
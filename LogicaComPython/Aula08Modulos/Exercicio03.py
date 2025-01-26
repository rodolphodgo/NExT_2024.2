'''Crie uma função que atue como um simulador de dado 🎲 (valor entre 1 e 6). Se o valor for igual a 6, exiba a mensagem: "Dano Crítico!".'''

import random

def dado():
    dado = random.randint(1,6)
    print(dado)
    if dado == 6:
        print("Dano crítico!")

dado()
"""Faça uma função que receba um valor inteiro e positivo e calcule o seu fatorial."""

import math

entrada = int(input())

def fatorial(x):
    if x > 0:
        print(math.factorial(x))
    else:
        print("A entrada tem que ser positiva")

fatorial(entrada)
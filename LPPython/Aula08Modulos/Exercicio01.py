'''A partir do valor do raio informado pelo usuário, calcule a area da circunferência utilizando funções e π (pi) do modulo math.'''

from math import pi

r = float(input())

def circunferencia(param):
    resultado = 2 * pi * param
    print(f"{resultado:.2f}")

circunferencia(r)

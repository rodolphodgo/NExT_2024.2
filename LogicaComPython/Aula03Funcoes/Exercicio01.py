'''Crie um programa que receba um valor inteiro e avalie se ele é positivo ou negativo. Essa avaliação deve ocorrer dentro de uma função que retorna um valor booleano.'''

numero = int(input())

def positivo_negativo():
    if numero > 0:
        return True
    elif numero < 0:
        return False
    else:
        return "Nulo"

print(positivo_negativo())
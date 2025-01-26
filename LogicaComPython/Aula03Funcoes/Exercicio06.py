'''Crie um programa que tenha uma função que receba uma lista de números inteiros e exiba todos os seus valores em ordem invertida. Obs.: Sem usar invert ou o fatiador com passo -1.'''

def entrada():
    valor = list(input().split(" "))
    valor_inteiro = [int(x) for x in valor]
    valor_inteiro.reverse()
    print(valor_inteiro)

entrada()
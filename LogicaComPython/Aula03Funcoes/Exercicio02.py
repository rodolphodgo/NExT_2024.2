'''Crie um programa que tenha uma função que receba uma lista de números inteiros e exiba todos os valores multiplicados por um valor inserido pelo usuário.'''

valor = list(input().split(" "))
valor_inteiro = [int(x) for x in valor]
multiplicador = int(input())

def multiplicados():
    for x in valor_inteiro:
        x = x * multiplicador
        print(x)

multiplicados()
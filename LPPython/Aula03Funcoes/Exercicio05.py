'''Crie um programa que receba do usuário 5 números inteiros e os exiba na tela na ordem contrária a que foi inserido. A leitura dos números deve ser feita em uma função e a exibição dos valores em ordem contrária deve ocorrer em outra função.'''

def entrada():
    lista = []
    for x in range(5):
        lista.append(int(input()))
    return lista

def invertida(lista):
    lista.reverse()
    print(lista)

lista = entrada()

invertida(lista)
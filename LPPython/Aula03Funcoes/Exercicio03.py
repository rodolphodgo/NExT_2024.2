'''Crie um programa que possua uma lista de nomes. Peça que o usuário insira um nome que será buscado nesta lista. A busca deve ser implementada em uma função que retorna os valores lógicos verdadeiro ou falso.'''

lista = ["Bruna", "Jurandir", "Ivete", "Cláudia", "Rafael"]

busca = input()

def buscador():
    if busca in lista:
        return True
    else:
        return False

print(buscador())
'''Escreva um programa que leia dois números do usuário e calcule a divisão entre eles. Use exceções para tratar:

Erros de entrada (ValueError);
Divisão por zero (ZeroDivisionError).'''

try:
    n1 = int(input())
    n2 = int(input())
    print(n1 / n2)

except ValueError:
    print('Erro: Você deve digitar um número.')
except ZeroDivisionError:
    print('Erro: Não é possível dividir por zero.')
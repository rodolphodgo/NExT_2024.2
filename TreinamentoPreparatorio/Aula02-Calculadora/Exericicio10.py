"""Tendo como dado de entrada a altura ( h ) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:

Para homens:  (72.7×h)−58
Para mulheres:  (62.1×h)−44.7"""

sexo = input('Qual o seu sexo? H|M ')
altura = float(input('Qual é a sua altura? '))

homem = (72.7 * altura) - 58
mulher = (62.1 * altura) - 44.7

if sexo == 'H':
  print('Seu peso idial é ', homem)
else:
  print('Seu peso ideal é ', mulher)
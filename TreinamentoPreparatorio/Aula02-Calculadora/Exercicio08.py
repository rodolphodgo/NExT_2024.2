"""Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax² + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:

a - Se o usuário informar o valor de a igual a zero, a equação não é do segundo grau e o programa não deve pedir os demais valores, sendo encerrado;

b - Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;

c - Se o delta calculado for igual a zero a equação possui apenas uma raiz real; Informe-a ao usuário;

d - Se o delta for positivo, a equação possui duas raiz reais; Informe-as ao usuário;"""

a = float(input('Valor de a: '))
b = float(input('Valor de b: '))
c = float(input('Valor de c: '))

delta = b**2 - 4 * a * c

if a == 0:
  print('A equação não é do segundo grau')
elif delta < 0:
  print('A equação não possui raízes')
elif delta == 0:
  print('A equação possui apenas uma raíz')
else:
  print('A equação possui duas raízes')
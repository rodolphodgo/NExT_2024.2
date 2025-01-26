"""Faça um programa que converta o valor da temperatura de graus Celsius para graus Fahrenheit:

Fórmula para converter graus Fahrenheit para Celsius:

°C=5×((°F−32)/9)"""

celsius = float(input('Qual a temperatura em ºC: ' ))

fahrenheit = (celsius * 9 / 5) + 32

print('A temperatura digitada em fahrenheit é ', fahrenheit)
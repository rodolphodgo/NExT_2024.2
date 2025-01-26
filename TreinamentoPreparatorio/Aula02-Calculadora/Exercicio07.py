"""Faça um programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

°F=(°C×9/5)+32"""

fahrenheit = float(input('Qual a temperatura em ºC: ' ))

celsius = 5 * ((fahrenheit - 32) / 9)

print('A temperatura digitada em celsius é ', celsius)
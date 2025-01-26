#Faça um programa que recebe um número de 1 a 10 do usuário e imprime a tabuada de multiplicação desse número

numero = int(input())
x = 1

while x <= 10:
    print(f'{x} x {numero} = {x * numero}')
    x += 1
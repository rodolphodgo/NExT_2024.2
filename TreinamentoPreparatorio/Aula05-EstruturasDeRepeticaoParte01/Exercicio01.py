#Faça um programa que leia 5 números e informe o maior número.

n = 1
numeros = []

while n <= 5:
  numeros.append(int(input(f"Insira {n}° número: ")))
  n += 1

print(f"O maior número inserido é: {max(numeros)}")

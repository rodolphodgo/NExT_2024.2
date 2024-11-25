numeros = []

for x in range(6):
  entrada = float(input())
  if entrada > 0 :
    numeros.append(entrada)
  x = x + 1

print(f'{len(numeros)} valores positivos')